#!/usr/bin/env python3
"""
Database migration script to fix missing section_enrollments table
"""

import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

def run_migration():
    """Run the SQL migration to create section_enrollments table"""
    
    # Get database connection details from environment
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url:
        print("Error: DATABASE_URL not found in environment variables")
        print("Please set your Supabase database URL in a .env file")
        return False
    
    try:
        # Connect to the database
        print("Connecting to database...")
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        
        # Read and execute the SQL migration file
        print("Reading migration SQL file...")
        with open('fix_section_enrollments_table.sql', 'r') as f:
            migration_sql = f.read()
        
        print("Executing migration...")
        cur.execute(migration_sql)
        
        # Commit the changes
        conn.commit()
        print("✅ Migration completed successfully!")
        
        # Verify the table was created
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'section_enrollments'
        """)
        
        if cur.fetchone():
            print("✅ Table 'section_enrollments' created successfully!")
        else:
            print("❌ Table 'section_enrollments' was not found after migration")
            
    except psycopg2.Error as e:
        print(f"❌ Database error: {e}")
        return False
    except FileNotFoundError:
        print("❌ Migration file 'fix_section_enrollments_table.sql' not found")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
        print("Database connection closed.")
    
    return True

if __name__ == "__main__":
    print("🚀 Starting database migration...")
    print("This will create the missing 'section_enrollments' table")
    print("-" * 50)
    
    success = run_migration()
    
    print("-" * 50)
    if success:
        print("🎉 Migration completed successfully!")
        print("The GradeManagement component should now work properly.")
    else:
        print("💥 Migration failed. Please check the errors above.")
        print("Make sure your DATABASE_URL is set correctly in the .env file.")