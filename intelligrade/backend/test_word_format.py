# Test with the exact format from the Word document
import sys
import os
sys.path.append('c:\\Users\\Administrator\\Desktop\\INTELLIGRADE\\intelligrade\\backend')

from app.api.endpoints.assessments import parse_answer_key_flexible

# Your exact format from the Word document
your_format = """Grade 7
True or False
1. The Earth is the third planet from the Sun. T
2. The water cycle includes evaporation, condensation, and precipitation. T
3. The process of photosynthesis occurs in the roots of plants. T
4. The number of chromosomes in a human body cell is 46. T
5. A parallelogram has two pairs of parallel sides. T

Multiple Choice
1. What is the main purpose of the heart in the circulatory system? B
a) To produce oxygen
b) To pump blood throughout the body
c) To digest food
d) To filter waste
2. Which of the following is NOT a primary color of light? D
a) Red
b) Green
c) Blue
d) Yellow
3. What is the process of a liquid turning into a gas called? C
a) Freezing
b) Melting
c) Evaporation
d) Condensation
4. Which of the following is an example of a non-renewable resource? C
a) Wind
b) Solar energy
c) Coal
d) Geothermal energy"""

print("🧪 Testing Your Exact Word Document Format")
print("=" * 50)

try:
    result = parse_answer_key_flexible(your_format)
    print(f"✅ Successfully parsed {len(result['questions'])} questions")
    
    for q in result['questions']:
        print(f"   Q{q['id']}: {q['answer']} ({q['type']}) - {q['text'][:50]}...")
        
    if len(result['questions']) == 0:
        print("❌ No questions found! Debug info should be above.")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print(f"\n🎯 Expected: 9 questions (5 T/F + 4 MC)")
print(f"🎯 Got: {len(result['questions']) if 'result' in locals() else 0} questions")