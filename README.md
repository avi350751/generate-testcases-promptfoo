### Generate Test Cases Automatically from User Stories & Acceptance Criteria

This project demonstrates how to use LangChain, OpenAI GPT models, and structured output parsers to automatically generate high-quality test cases for manual and automation QA workflows. Use Promptfoo to evaluate the responses.

It follows a simple architecture:

User Story + Acceptance Criteria
        ↓
LangChain Prompt Template
        ↓
LLM (GPT-4.1-mini)
        ↓
JsonOutputParser
        ↓
Structured Test Cases in JSON
        ↓
Evaluate response using Promptfoo

🔥 Features

Convert any user story into structured test cases.
Uses LangChain Expression Language (LCEL) for clean chaining.
Enforces strict JSON output using JsonOutputParser.

Produces:

- Happy path test cases
- Negative scenarios
- Edge case scenarios
- Easy to integrate into CI/CD, Promptfoo evaluation, or Auto-Test pipelines.

📂 Project Structure
project3-promptfoo/
|--dataset
  |__ stories_ac.yaml
│── helper.py
│── test_case_generator.py
|-- promptfooconfig.yaml
│── requirements.txt
│── README.md
│── .env
│── .gitignore

# Getting started
python3 -m venv myenv
source myenv/bin/activate      # macOS / Linux
myenv\Scripts\activate         # Windows

pip install -r requirements.txt

promptfoo eval --no-cache