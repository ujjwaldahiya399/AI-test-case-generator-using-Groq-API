from groq import Groq
import os

# Load API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Load the requirement file
with open("sample_requirement.txt", "r") as f:
    requirement = f.read()

# Build the prompt
prompt = f"""
You are an expert QA Engineer and SDET.
Based on the following requirements, generate detailed test cases.

For each test case include:
- Test Case ID
- Test Title
- Preconditions
- Test Steps
- Expected Result
- Test Type (Positive / Negative / Edge Case)

Requirements:
{requirement}
"""

# Call Groq
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Print results
print("\n---- GENERATED TEST CASES -----\n")
print(response.choices[0].message.content)

# Save to file
with open("test_cases_output.txt", "w") as f:
    f.write(response.choices[0].message.content)

print("\n Test cases saved to test_cases_output.txt")