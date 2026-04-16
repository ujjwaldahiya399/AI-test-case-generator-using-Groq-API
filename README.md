#  AI Test Case Generator

An AI-powered tool that automatically generates detailed test cases from plain-English requirement documents — built for SDETs who want to move faster with AI.

---

##  What Problem Does It Solve?

Writing test cases manually from requirements is one of the most time-consuming tasks for any QA/SDET engineer. This tool takes a requirements document and instantly generates structured, comprehensive test cases including positive, negative, and edge cases — in seconds.

---

##  How It Works

1. You provide a `.txt` file with feature requirements
2. The tool sends it to an LLM (LLaMA 3 via Groq API)
3. AI generates detailed test cases with steps, preconditions, and expected results
4. Output is saved to `test_cases_output.txt`

---

##  Tech Stack

- **Python 3.14**
- **Groq API** (Free tier)
- **LLaMA 3.3 70B** model
- **pytest** (for future test execution integration)

---

##  Setup and Installation

### 1. Clone the repository
git clone https://github.com/your-username/ai-test-case-generator.git
cd ai-test-case-generator

### 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set your Groq API key
Get a free API key from https://console.groq.com

export GROQ_API_KEY="your-api-key-here"

### 5. Add your requirements
Edit sample_requirement.txt with your feature requirements

### 6. Run the generator
python3 generator.py

---

## Sample Input (sample_requirement.txt)

Feature: User Login

A user should be able to log in to the application using their 
email and password.

Requirements:
- Email field must accept valid email format only
- Password must be at least 8 characters
- If credentials are correct, user is redirected to dashboard
- After 5 failed attempts, lock the account for 30 minutes

---

##  Sample Output (test_cases_output.txt)

Test Case ID: TC_001
Title: Successful login with valid credentials
Preconditions: User has a registered account
Test Steps:
