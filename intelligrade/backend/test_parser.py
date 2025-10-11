# Test the flexible parser with all formats
import sys
import os
sys.path.append('c:\\Users\\Administrator\\Desktop\\INTELLIGRADE\\intelligrade\\backend')

from app.api.endpoints.assessments import parse_answer_key_flexible, extract_student_answers

# Format 1: Answer at end "1. Question? T"
format1 = """Grade 7
True or False
1. The Earth is the third planet from the Sun. T 
2. The water cycle includes evaporation, condensation, and precipitation. T
3. The process of photosynthesis occurs in the roots of plants. T

Multiple Choice
1. What is the main purpose of the heart in the circulatory system? B
a) To produce oxygen
b) To pump blood throughout the body
2. Which of the following is NOT a primary color of light? D
a) Red
b) Green"""

# Format 2: Answer at beginning "T 1. Question"
format2 = """Grade 7
True or False
T 1. The Earth is the third planet from the Sun.   
T 2. The water cycle includes evaporation, condensation, and precipitation.  

Multiple Choice
B 1. What is the main purpose of the heart in the circulatory system? 
a) To produce oxygen
b) To pump blood throughout the body
D 2. Which of the following is NOT a primary color of light?"""

# Format 3: Answer with "Answer:" 
format3 = """Grade 7
True or False
1. The Earth is the third planet from the Sun. True 
2. The water cycle includes evaporation, condensation, and precipitation. True

Multiple Choice
1. What is the main purpose of the heart in the circulatory system? Answer :B
2. Which of the following is NOT a primary color of light? Answer: D"""

# Format 4: "TRUE" at beginning
format4 = """Grade 7
True or False
TRUE 1. The Earth is the third planet from the Sun.  
TRUE 2. The water cycle includes evaporation, condensation, and precipitation.  

Multiple Choice
1. What is the main purpose of the heart in the circulatory system? Answer :B
2. Which of the following is NOT a primary color of light? Answer: D"""

# Format 5: Simple list with numbered placeholders
format5 = """T or F
1.
2.
3.
4.
5.

Multiple Choice
1.
2.
3.
4."""

# Format 6: Just answers in order
format6 = """True
False
True
True
False
A
B
C
D
A"""

# Format 7: Mixed simple format
format7 = """True or False
T
F
T
F

Multiple Choice  
A
B
C
D"""

# Test all formats
formats = [
    ("Format 1 (Answer at end)", format1),
    ("Format 2 (Answer at beginning)", format2), 
    ("Format 3 (Answer: format)", format3),
    ("Format 4 (TRUE at beginning)", format4),
    ("Format 5 (Simple list with numbers)", format5),
    ("Format 6 (Just answers in order)", format6),
    ("Format 7 (Mixed simple format)", format7)
]

print("🧪 Testing Flexible Parser with All Formats")
print("=" * 50)

for name, text in formats:
    print(f"\n📋 Testing {name}")
    print("-" * 30)
    
    try:
        result = parse_answer_key_flexible(text)
        print(f"✅ Parsed {len(result['questions'])} questions")
        
        for q in result['questions']:
            print(f"   Q{q['id']}: {q['answer']} ({q['type']})")
            
    except Exception as e:
        print(f"❌ Error: {e}")

print(f"\n🎯 Testing complete!")