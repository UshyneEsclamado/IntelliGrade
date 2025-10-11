# Direct test of regex patterns
import re

def test_pattern(pattern, test_string):
    match = re.match(pattern, test_string, re.IGNORECASE)
    return match.groups() if match else None

# Test cases from your document
test_lines = [
    "1. The Earth is the third planet from the Sun. T",
    "2. The water cycle includes evaporation, condensation, and precipitation. T",
    "1. What is the main purpose of the heart in the circulatory system? B"
]

# The main pattern that should work
pattern = r'^(\d+)\.\s+(.+?)\s+([A-E]|T|F|TRUE|FALSE|True|False)\s*$'

print("🔍 Testing Regex Pattern")
print("=" * 40)
print(f"Pattern: {pattern}")
print()

for line in test_lines:
    result = test_pattern(pattern, line)
    print(f"Line: '{line}'")
    print(f"Match: {result}")
    print()

# Test the normalize function
def normalize_answer(answer: str) -> str:
    answer = answer.upper().strip()
    if answer in ['T', 'TRUE']:
        return 'TRUE'
    elif answer in ['F', 'FALSE']:
        return 'FALSE'
    if answer in ['A', 'B', 'C', 'D', 'E']:
        return answer
    return answer

print("🔄 Testing Normalization")
print("=" * 30)
test_answers = ['T', 'F', 'B', 'A', 'C']
for ans in test_answers:
    normalized = normalize_answer(ans)
    print(f"'{ans}' -> '{normalized}'")