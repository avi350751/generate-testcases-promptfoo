# test_case_generator.py
import os
from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

# --- Pydantic schema to enforce structure ---

class TestCase(BaseModel):
    id: str = Field(description="Unique test case ID, e.g., TC-001")
    title: str
    type: str  # happy | negative | edge
    preconditions: List[str]
    steps: List[str]
    expected_result: str

class TestCaseResponse(BaseModel):
    test_cases: List[TestCase]


parser = JsonOutputParser(pydantic_object=TestCaseResponse)

prompt = ChatPromptTemplate.from_template("""
You are a senior QA engineer.

Given the user story and acceptance criteria, generate manual test cases
in the following JSON format that exactly matches this schema:

{format_instructions}

User story:
{user_story}

Acceptance criteria:
{acceptance_criteria}

Rules:
- Ensure every acceptance criterion is covered by at least one test case.
- Use clear, numbered steps.
- Use type as one of: "happy", "negative", "edge".
- Do not include any fields outside the specified JSON schema.
""")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

chain = prompt | llm | parser


def generate_test_cases(user_story: str, acceptance_criteria: str) -> Dict[str, Any]:
    return chain.invoke({
        "user_story": user_story,
        "acceptance_criteria": acceptance_criteria,
        "format_instructions": parser.get_format_instructions()
    })


if __name__ == "__main__":
    
    import yaml
    
    with open("dataset/stories_ac.yaml", "r") as f:
        data = yaml.safe_load(f)
    
    # Assuming the YAML has user_story and acceptance_criteria keys
    us = data["user_story"]
    ac = data["acceptance_criteria"]
    result = generate_test_cases(us, ac)
    print(result)
