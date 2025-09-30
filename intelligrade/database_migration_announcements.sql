-- Migration: Create announcements table for teacher-to-student announcements
-- Run this in your Supabase SQL Editor

CREATE TABLE IF NOT EXISTS announcements (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    section_id UUID NOT NULL,
    teacher_id UUID NOT NULL,
    teacher_name VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    
    -- Foreign key constraints (adjust based on your existing table structure)
    CONSTRAINT fk_announcements_section
        FOREIGN KEY (section_id) 
        REFERENCES sections(id) 
        ON DELETE CASCADE,
        
    CONSTRAINT fk_announcements_teacher
        FOREIGN KEY (teacher_id) 
        REFERENCES profiles(auth_user_id) 
        ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_announcements_section_id ON announcements(section_id);
CREATE INDEX IF NOT EXISTS idx_announcements_teacher_id ON announcements(teacher_id);
CREATE INDEX IF NOT EXISTS idx_announcements_created_at ON announcements(created_at DESC);

-- Enable RLS (Row Level Security)
ALTER TABLE announcements ENABLE ROW LEVEL SECURITY;

-- RLS Policies

-- Teachers can read all announcements from their sections
CREATE POLICY "Teachers can view announcements from their sections" ON announcements
    FOR SELECT
    USING (
        teacher_id = auth.uid()
        OR
        section_id IN (
            SELECT id FROM sections 
            WHERE teacher_id = auth.uid()
        )
    );

-- Teachers can insert announcements to their sections
CREATE POLICY "Teachers can create announcements in their sections" ON announcements
    FOR INSERT
    WITH CHECK (
        teacher_id = auth.uid()
        AND
        section_id IN (
            SELECT id FROM sections 
            WHERE teacher_id = auth.uid()
        )
    );

-- Teachers can update their own announcements
CREATE POLICY "Teachers can update their own announcements" ON announcements
    FOR UPDATE
    USING (teacher_id = auth.uid())
    WITH CHECK (teacher_id = auth.uid());

-- Teachers can delete their own announcements
CREATE POLICY "Teachers can delete their own announcements" ON announcements
    FOR DELETE
    USING (teacher_id = auth.uid());

-- Students can read announcements from sections they're enrolled in
CREATE POLICY "Students can view announcements from their sections" ON announcements
    FOR SELECT
    USING (
        section_id IN (
            SELECT se.section_id 
            FROM student_enrollments se
            JOIN students s ON se.student_id = s.id
            WHERE s.profile_id = auth.uid()
        )
    );

-- Create trigger to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_announcements_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = timezone('utc'::text, now());
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_announcements_updated_at_trigger
    BEFORE UPDATE ON announcements
    FOR EACH ROW
    EXECUTE FUNCTION update_announcements_updated_at();

-- Optional: Add a table comment
COMMENT ON TABLE announcements IS 'Stores announcements sent by teachers to students in specific sections';