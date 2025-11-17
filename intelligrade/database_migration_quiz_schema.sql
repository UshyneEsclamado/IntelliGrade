quiz database scheme new
 -- ============================================
-- QUIZ MANAGEMENT SYSTEM - SIMPLIFIED SCHEMA
-- ============================================

-- Enable UUID extension (if not already enabled)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================
-- ENUM TYPES
-- ============================================

DO $$ BEGIN
    CREATE TYPE quiz_status AS ENUM ('draft', 'published', 'archived');
EXCEPTION
    WHEN duplicate_object THEN NULL;
END $$;

DO $$ BEGIN
    CREATE TYPE question_type AS ENUM ('multiple_choice', 'true_false', 'fill_blank');
EXCEPTION
    WHEN duplicate_object THEN NULL;
END $$;

DO $$ BEGIN
    CREATE TYPE attempt_status AS ENUM ('in_progress', 'submitted', 'graded', 'reviewed');
EXCEPTION
    WHEN duplicate_object THEN NULL;
END $$;

DO $$ BEGIN
    CREATE TYPE result_status AS ENUM ('not_taken', 'in_progress', 'completed', 'pending_review', 'graded');
EXCEPTION
    WHEN duplicate_object THEN NULL;
END $$;

-- ============================================
-- MAIN TABLES
-- ============================================

-- Table 1: Quizzes (Section-specific)
CREATE TABLE IF NOT EXISTS quizzes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_id UUID NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    section_id UUID NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
    teacher_id UUID NOT NULL REFERENCES teachers(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    number_of_questions INT NOT NULL CHECK (number_of_questions > 0),
    
    -- Quiz Settings
    has_time_limit BOOLEAN DEFAULT FALSE,
    time_limit_minutes INT CHECK (time_limit_minutes IS NULL OR time_limit_minutes > 0),
    attempts_allowed INT DEFAULT 1 CHECK (attempts_allowed > 0),
    shuffle_questions BOOLEAN DEFAULT FALSE,
    shuffle_options BOOLEAN DEFAULT FALSE,
    
    -- Schedule
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    
    -- Status
    status quiz_status DEFAULT 'draft',
    
    -- Quiz Code
    quiz_code VARCHAR(6) UNIQUE,
    
    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT valid_date_range CHECK (end_date IS NULL OR start_date IS NULL OR end_date > start_date)
);

CREATE INDEX IF NOT EXISTS idx_quizzes_subject_id ON quizzes(subject_id);
CREATE INDEX IF NOT EXISTS idx_quizzes_section_id ON quizzes(section_id);
CREATE INDEX IF NOT EXISTS idx_quizzes_teacher_id ON quizzes(teacher_id);
CREATE INDEX IF NOT EXISTS idx_quizzes_status ON quizzes(status);

-- Table 2: Quiz Questions
CREATE TABLE IF NOT EXISTS quiz_questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    question_number INT NOT NULL CHECK (question_number > 0),
    question_type question_type NOT NULL,
    question_text TEXT NOT NULL,
    points DECIMAL(5, 2) DEFAULT 1.00 CHECK (points > 0),
    
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(quiz_id, question_number)
);

CREATE INDEX IF NOT EXISTS idx_questions_quiz_id ON quiz_questions(quiz_id);

-- Table 3: Question Options (for multiple choice)
CREATE TABLE IF NOT EXISTS question_options (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    question_id UUID NOT NULL REFERENCES quiz_questions(id) ON DELETE CASCADE,
    option_number INT NOT NULL CHECK (option_number > 0),
    option_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(question_id, option_number)
);

CREATE INDEX IF NOT EXISTS idx_options_question_id ON question_options(question_id);

-- Table 4: Question Answers (for true/false and fill-in-blank)
CREATE TABLE IF NOT EXISTS question_answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    question_id UUID NOT NULL UNIQUE REFERENCES quiz_questions(id) ON DELETE CASCADE,
    correct_answer TEXT NOT NULL,
    case_sensitive BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_answers_question_id ON question_answers(question_id);

-- Table 5: Quiz Attempts
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    student_id UUID NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    attempt_number INT NOT NULL DEFAULT 1 CHECK (attempt_number > 0),
    
    started_at TIMESTAMPTZ DEFAULT NOW(),
    submitted_at TIMESTAMPTZ,
    time_taken_minutes INT,
    
    total_score DECIMAL(5, 2) DEFAULT 0.00,
    max_score DECIMAL(5, 2) NOT NULL,
    percentage DECIMAL(5, 2) DEFAULT 0.00 CHECK (percentage >= 0 AND percentage <= 100),
    
    status attempt_status DEFAULT 'in_progress',
    
    auto_graded BOOLEAN DEFAULT FALSE,
    manually_reviewed BOOLEAN DEFAULT FALSE,
    teacher_feedback TEXT,
    graded_by UUID REFERENCES teachers(id) ON DELETE SET NULL,
    graded_at TIMESTAMPTZ,
    
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(quiz_id, student_id, attempt_number)
);

CREATE INDEX IF NOT EXISTS idx_attempts_quiz_id ON quiz_attempts(quiz_id);
CREATE INDEX IF NOT EXISTS idx_attempts_student_id ON quiz_attempts(student_id);
CREATE INDEX IF NOT EXISTS idx_attempts_status ON quiz_attempts(status);

-- Table 6: Student Answers
CREATE TABLE IF NOT EXISTS student_answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    attempt_id UUID NOT NULL REFERENCES quiz_attempts(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES quiz_questions(id) ON DELETE CASCADE,
    
    selected_option_id UUID REFERENCES question_options(id) ON DELETE SET NULL,
    answer_text TEXT,
    
    is_correct BOOLEAN DEFAULT FALSE,
    points_earned DECIMAL(5, 2) DEFAULT 0.00,
    points_possible DECIMAL(5, 2) NOT NULL,
    
    teacher_comment TEXT,
    
    answered_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(attempt_id, question_id),
    CONSTRAINT answer_provided CHECK (
        selected_option_id IS NOT NULL OR answer_text IS NOT NULL
    )
);

CREATE INDEX IF NOT EXISTS idx_answers_attempt_id ON student_answers(attempt_id);
CREATE INDEX IF NOT EXISTS idx_answers_question_id ON student_answers(question_id);

-- Table 7: Quiz Results (aggregated for grade management)
CREATE TABLE IF NOT EXISTS quiz_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    student_id UUID NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    
    best_attempt_id UUID REFERENCES quiz_attempts(id) ON DELETE SET NULL,
    best_score DECIMAL(5, 2) DEFAULT 0.00,
    best_percentage DECIMAL(5, 2) DEFAULT 0.00,
    
    total_attempts INT DEFAULT 0,
    latest_attempt_date TIMESTAMPTZ,
    
    status result_status DEFAULT 'not_taken',
    finalized BOOLEAN DEFAULT FALSE,
    visible_to_student BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(quiz_id, student_id)
);

CREATE INDEX IF NOT EXISTS idx_results_quiz_id ON quiz_results(quiz_id);
CREATE INDEX IF NOT EXISTS idx_results_student_id ON quiz_results(student_id);

-- ============================================
-- SIMPLE FUNCTIONS (No complex triggers)
-- ============================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply triggers
DROP TRIGGER IF EXISTS update_quizzes_updated_at ON quizzes;
CREATE TRIGGER update_quizzes_updated_at BEFORE UPDATE ON quizzes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_quiz_questions_updated_at ON quiz_questions;
CREATE TRIGGER update_quiz_questions_updated_at BEFORE UPDATE ON quiz_questions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_quiz_attempts_updated_at ON quiz_attempts;
CREATE TRIGGER update_quiz_attempts_updated_at BEFORE UPDATE ON quiz_attempts
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_student_answers_updated_at ON student_answers;
CREATE TRIGGER update_student_answers_updated_at BEFORE UPDATE ON student_answers
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_quiz_results_updated_at ON quiz_results;
CREATE TRIGGER update_quiz_results_updated_at BEFORE UPDATE ON quiz_results
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Simple function to generate quiz code
CREATE OR REPLACE FUNCTION generate_quiz_code()
RETURNS TEXT AS $$
DECLARE
    characters TEXT := 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    result TEXT := '';
    i INTEGER;
    code_exists BOOLEAN;
BEGIN
    LOOP
        result := '';
        FOR i IN 1..6 LOOP
            result := result || substr(characters, floor(random() * length(characters) + 1)::int, 1);
        END LOOP;
        
        SELECT EXISTS(SELECT 1 FROM quizzes WHERE quiz_code = result) INTO code_exists;
        
        IF NOT code_exists THEN
            EXIT;
        END IF;
    END LOOP;
    
    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- Trigger to auto-generate quiz code
CREATE OR REPLACE FUNCTION set_quiz_code()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.quiz_code IS NULL THEN
        NEW.quiz_code := generate_quiz_code();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trigger_set_quiz_code ON quizzes;
CREATE TRIGGER trigger_set_quiz_code
    BEFORE INSERT ON quizzes
    FOR EACH ROW
    EXECUTE FUNCTION set_quiz_code();

-- ============================================
-- RLS POLICIES
-- ============================================

ALTER TABLE quizzes ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE question_options ENABLE ROW LEVEL SECURITY;
ALTER TABLE question_answers ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_attempts ENABLE ROW LEVEL SECURITY;
ALTER TABLE student_answers ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_results ENABLE ROW LEVEL SECURITY;

-- Quizzes policies
DROP POLICY IF EXISTS "Teachers can CRUD their own quizzes" ON quizzes;
CREATE POLICY "Teachers can CRUD their own quizzes"
    ON quizzes FOR ALL TO authenticated
    USING (
        teacher_id IN (
            SELECT t.id FROM teachers t
            JOIN profiles p ON t.profile_id = p.id
            WHERE p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Students can view published quizzes in their sections" ON quizzes;
CREATE POLICY "Students can view published quizzes in their sections"
    ON quizzes FOR SELECT TO authenticated
    USING (
        status = 'published'
        AND section_id IN (
            SELECT e.section_id FROM enrollments e
            JOIN students s ON e.student_id = s.id
            JOIN profiles p ON s.profile_id = p.id
            WHERE p.auth_user_id = auth.uid()
            AND e.status = 'active'
        )
    );

-- Quiz questions policies
DROP POLICY IF EXISTS "Teachers can manage questions for their quizzes" ON quiz_questions;
CREATE POLICY "Teachers can manage questions for their quizzes"
    ON quiz_questions FOR ALL TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quizzes q
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE q.id = quiz_questions.quiz_id 
            AND p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Students can view questions for their published quizzes" ON quiz_questions;
CREATE POLICY "Students can view questions for their published quizzes"
    ON quiz_questions FOR SELECT TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quizzes q
            JOIN enrollments e ON q.section_id = e.section_id
            JOIN students s ON e.student_id = s.id
            JOIN profiles p ON s.profile_id = p.id
            WHERE q.id = quiz_questions.quiz_id 
            AND q.status = 'published'
            AND e.status = 'active'
            AND p.auth_user_id = auth.uid()
        )
    );

-- Question options policies
DROP POLICY IF EXISTS "Teachers manage options for their questions" ON question_options;
CREATE POLICY "Teachers manage options for their questions"
    ON question_options FOR ALL TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quiz_questions qq
            JOIN quizzes q ON qq.quiz_id = q.id
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE qq.id = question_options.question_id 
            AND p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Students view options for their published quizzes" ON question_options;
CREATE POLICY "Students view options for their published quizzes"
    ON question_options FOR SELECT TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quiz_questions qq
            JOIN quizzes q ON qq.quiz_id = q.id
            JOIN enrollments e ON q.section_id = e.section_id
            JOIN students s ON e.student_id = s.id
            JOIN profiles p ON s.profile_id = p.id
            WHERE qq.id = question_options.question_id 
            AND q.status = 'published'
            AND e.status = 'active'
            AND p.auth_user_id = auth.uid()
        )
    );

-- Question answers policies (Teachers only)
DROP POLICY IF EXISTS "Teachers manage answers for their questions" ON question_answers;
CREATE POLICY "Teachers manage answers for their questions"
    ON question_answers FOR ALL TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quiz_questions qq
            JOIN quizzes q ON qq.quiz_id = q.id
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE qq.id = question_answers.question_id 
            AND p.auth_user_id = auth.uid()
        )
    );

-- Quiz attempts policies
DROP POLICY IF EXISTS "Students manage their own attempts" ON quiz_attempts;
CREATE POLICY "Students manage their own attempts"
    ON quiz_attempts FOR ALL TO authenticated
    USING (
        student_id IN (
            SELECT s.id FROM students s
            JOIN profiles p ON s.profile_id = p.id
            WHERE p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Teachers view attempts for their quizzes" ON quiz_attempts;
CREATE POLICY "Teachers view attempts for their quizzes"
    ON quiz_attempts FOR SELECT TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quizzes q
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE q.id = quiz_attempts.quiz_id 
            AND p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Teachers can update attempts for grading" ON quiz_attempts;
CREATE POLICY "Teachers can update attempts for grading"
    ON quiz_attempts FOR UPDATE TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quizzes q
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE q.id = quiz_attempts.quiz_id 
            AND p.auth_user_id = auth.uid()
        )
    );

-- Student answers policies
DROP POLICY IF EXISTS "Students manage their own answers" ON student_answers;
CREATE POLICY "Students manage their own answers"
    ON student_answers FOR ALL TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quiz_attempts qa
            JOIN students s ON qa.student_id = s.id
            JOIN profiles p ON s.profile_id = p.id
            WHERE qa.id = student_answers.attempt_id 
            AND p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Teachers view answers for their quizzes" ON student_answers;
CREATE POLICY "Teachers view answers for their quizzes"
    ON student_answers FOR SELECT TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quiz_attempts qa
            JOIN quizzes q ON qa.quiz_id = q.id
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE qa.id = student_answers.attempt_id 
            AND p.auth_user_id = auth.uid()
        )
    );

DROP POLICY IF EXISTS "Teachers can update answers for grading" ON student_answers;
CREATE POLICY "Teachers can update answers for grading"
    ON student_answers FOR UPDATE TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quiz_attempts qa
            JOIN quizzes q ON qa.quiz_id = q.id
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE qa.id = student_answers.attempt_id 
            AND p.auth_user_id = auth.uid()
        )
    );

-- Quiz results policies
DROP POLICY IF EXISTS "Students view their own visible results" ON quiz_results;
CREATE POLICY "Students view their own visible results"
    ON quiz_results FOR SELECT TO authenticated
    USING (
        student_id IN (
            SELECT s.id FROM students s
            JOIN profiles p ON s.profile_id = p.id
            WHERE p.auth_user_id = auth.uid()
        )
        AND visible_to_student = TRUE
    );

DROP POLICY IF EXISTS "Teachers view results for their quizzes" ON quiz_results;
CREATE POLICY "Teachers view results for their quizzes"
    ON quiz_results FOR ALL TO authenticated
    USING (
        EXISTS (
            SELECT 1 FROM quizzes q
            JOIN teachers t ON q.teacher_id = t.id
            JOIN profiles p ON t.profile_id = p.id
            WHERE q.id = quiz_results.quiz_id 
            AND p.auth_user_id = auth.uid()
        )
    );

-- ============================================
-- END OF SIMPLIFIED QUIZ SCHEMA
-- ============================================
t.id
