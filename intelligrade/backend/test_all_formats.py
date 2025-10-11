# Comprehensive test for all user-provided formats
import sys
import os
sys.path.append('c:\\Users\\Administrator\\Desktop\\INTELLIGRADE\\intelligrade\\backend')

from app.api.endpoints.assessments import parse_answer_key_flexible

def test_format(name, content):
    print(f"\n🧪 Testing {name}")
    print("=" * 50)
    
    try:
        result = parse_answer_key_flexible(content)
        
        print(f"✅ Successfully parsed {len(result['questions'])} questions")
        print(f"📊 Format detected: {result['format_type']}")
        
        if len(result['questions']) > 0:
            print("\n📋 Questions found:")
            for q in result['questions']:
                print(f"   Q{q['id']}: {q['answer']} ({q['type']})")
        else:
            print("⚠️ No questions found!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

# Test Format 1: T/F with answer at start
test_format("True/False - Answer at Start", """
T 1. The earth orbits the sun.
F 2. Fish can live without water.
T 3. Plants need sunlight to grow.
F 4. The moon is made of cheese.
T 5. Water freezes at 0°C.
""")

# Test Format 2: T/F with answer at end
test_format("True/False - Answer at End", """
1. The sky is blue. T
2. Humans can breathe underwater unaided. F
3. Fire is hot. T
4. Ice is warm. F
5. The sun rises in the east. T
""")

# Test Format 3: Multiple Choice with answer at start
test_format("Multiple Choice - Answer at Start", """
B 1. What is the capital of Japan?
   A. Seoul
   B. Tokyo
   C. Beijing
   D. Bangkok

A 2. Which is a fruit?
   A. Apple
   B. Carrot
   C. Potato
   D. Lettuce
""")

# Test Format 4: Multiple Choice with Answer: keyword
test_format("Multiple Choice - Answer Keyword", """
1. What is the largest planet?
   A. Earth
   B. Mars
   C. Jupiter
   D. Venus
Answer: C

2. What color is the sun?
   A. Blue
   B. Green
   C. Yellow
   D. Purple
Answer: C
""")

# Test Format 5: Simple answer-only format
test_format("Simple Answer List", """
1. A
2. B
3. T
4. F
5. C
""")

# Test Format 6: Mixed with sections
test_format("Mixed Format with Sections", """
Grade 7 Quiz

True or False
1. The Earth is round. T
2. Water boils at 100°C. T

Multiple Choice
1. What is 2+2?
   A. 3
   B. 4
   C. 5
Answer: B
""")

print("\n" + "=" * 60)
print("🎉 All format tests completed!")