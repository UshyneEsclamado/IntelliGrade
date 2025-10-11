# Test the specific format from the user's document
import sys
import os
sys.path.append('c:\\Users\\Administrator\\Desktop\\INTELLIGRADE\\intelligrade\\backend')

from app.api.endpoints.assessments import parse_answer_key_flexible

# Test with the user's exact format
test_content = """Grade 7
True or False
1.	The Earth is the third planet from the Sun.  T 
2.	The water cycle includes evaporation, condensation, and precipitation.  T
3.	The process of photosynthesis occurs in the roots of plants.  T
4.	The number of chromosomes in a human body cell is 46.  T
5.	A parallelogram has two pairs of parallel sides.  T

Multiple Choice
1.	What is the main purpose of the heart in the circulatory system? B
a) To produce oxygen
b) To pump blood throughout the body
c) To digest food
d) To filter waste
2.	Which of the following is NOT a primary color of light? D
a) Red
b) Green
c) Blue
d) Yellow
3.	What is the process of a liquid turning into a gas called? C
a) Freezing
b) Melting
c) Evaporation
d) Condensation
4.	Which of the following is an example of a non-renewable resource? A
a) Wind
b) Solar energy
c) Coal
d) Geothermal energy"""

print("🧪 Testing User's Exact Format")
print("=" * 50)

try:
    result = parse_answer_key_flexible(test_content)
    
    print(f"✅ Successfully parsed {len(result['questions'])} questions")
    print(f"📊 Format detected: {result['format_type']}")
    print()
    
    print("📋 Questions found:")
    for q in result['questions']:
        print(f"   Q{q['id']}: {q['answer']} ({q['type']}) - {q.get('text', 'No text')[:50]}...")
    
    if len(result['questions']) >= 9:
        print("\n🎉 SUCCESS! All 9 questions should be detected")
    else:
        print(f"\n⚠️ ISSUE: Only {len(result['questions'])} questions found, expected 9")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("Test completed!")