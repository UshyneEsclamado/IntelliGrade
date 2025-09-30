-- Fix for missing section_enrollments table
-- This creates the table that's causing the database error in GradeManagement

-- Create section_enrollments table if it doesn't exist
CREATE TABLE IF NOT EXISTS public.section_enrollments (
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    section_id uuid NOT NULL,
    student_id uuid NOT NULL,
    enrollment_date timestamp with time zone DEFAULT now(),
    status text DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'dropped')),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    
    -- Foreign key constraints
    CONSTRAINT fk_section_enrollments_section_id 
        FOREIGN KEY (section_id) 
        REFERENCES public.sections(id) 
        ON DELETE CASCADE,
        
    CONSTRAINT fk_section_enrollments_student_id 
        FOREIGN KEY (student_id) 
        REFERENCES public.users(id) 
        ON DELETE CASCADE,
    
    -- Unique constraint to prevent duplicate enrollments
    CONSTRAINT unique_section_student 
        UNIQUE (section_id, student_id)
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_section_enrollments_section_id 
    ON public.section_enrollments(section_id);

CREATE INDEX IF NOT EXISTS idx_section_enrollments_student_id 
    ON public.section_enrollments(student_id);

CREATE INDEX IF NOT EXISTS idx_section_enrollments_status 
    ON public.section_enrollments(status);

-- Insert sample data if the table is empty (optional)
INSERT INTO public.section_enrollments (section_id, student_id, status)
SELECT 
    s.id as section_id,
    u.id as student_id,
    'active' as status
FROM 
    public.sections s,
    public.users u
WHERE 
    u.role = 'student'
    AND NOT EXISTS (
        SELECT 1 FROM public.section_enrollments se 
        WHERE se.section_id = s.id AND se.student_id = u.id
    )
LIMIT 50; -- Limit to prevent too many sample records

-- Enable RLS (Row Level Security)
ALTER TABLE public.section_enrollments ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
CREATE POLICY "Teachers can view enrollments for their sections" ON public.section_enrollments
    FOR SELECT USING (
        section_id IN (
            SELECT id FROM public.sections 
            WHERE teacher_id = auth.uid()
        )
    );

CREATE POLICY "Teachers can manage enrollments for their sections" ON public.section_enrollments
    FOR ALL USING (
        section_id IN (
            SELECT id FROM public.sections 
            WHERE teacher_id = auth.uid()
        )
    );

CREATE POLICY "Students can view their own enrollments" ON public.section_enrollments
    FOR SELECT USING (student_id = auth.uid());

-- Create trigger for updated_at timestamp
CREATE OR REPLACE FUNCTION update_section_enrollments_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_section_enrollments_updated_at
    BEFORE UPDATE ON public.section_enrollments
    FOR EACH ROW
    EXECUTE FUNCTION update_section_enrollments_updated_at();

-- Add helpful comments
COMMENT ON TABLE public.section_enrollments IS 'Manages student enrollments in sections';
COMMENT ON COLUMN public.section_enrollments.section_id IS 'References the section';
COMMENT ON COLUMN public.section_enrollments.student_id IS 'References the enrolled student';
COMMENT ON COLUMN public.section_enrollments.status IS 'Enrollment status: active, inactive, dropped';
COMMENT ON COLUMN public.section_enrollments.enrollment_date IS 'When the student enrolled';