# helper.py
from test_case_generator import generate_test_cases
import json

def call_api(prompt, options, context):
    """
    promptfoo will send `prompt` (we'll pack user_story+acceptance_criteria there)
    and expect JSON back.
    """
    user_story = context.get("vars", {}).get("user_story", "")
    acceptance_criteria = context.get("vars", {}).get("acceptance_criteria", "")
    result = generate_test_cases(user_story, acceptance_criteria)
    # Return as text; Promptfoo will see it as `output`
    pretty = json.dumps(result, indent=2, ensure_ascii=False)

    return {
        "output": pretty
    }
