SCENARIO_PROMPT = """
You are a Senior QA Engineer.

Requirement:
{requirement}

Generate test scenarios.

Return ONLY valid JSON array.
Each object MUST contain ALL keys.

JSON schema:
[
  {{
    "id": 1,
    "title": "Scenario title",
    "type": "Positive|Negative|Edge"
  }}
]

IMPORTANT:
- Return ONLY JSON.
- No markdown.
- No explanation.
"""

TESTCASE_PROMPT = """
You are a Senior QA Engineer.

Requirement:
{requirement}

Scenarios:
{scenarios}

Generate detailed test cases.

Return ONLY valid JSON array.
Each object MUST contain ALL keys.

JSON schema:
[
  {{
    "id": 1,
    "scenario_id": 1,
    "title": "Test case title",
    "precondition": "Precondition text",
    "steps": ["Step 1", "Step 2"],
    "expected_result": "Expected result",
    "priority": "P0|P1|P2"
  }}
]

IMPORTANT:
- Return ONLY JSON.
- No markdown.
- No explanation.
"""

BDD_PROMPT = """
You are a Senior QA Engineer.

Requirement:
{requirement}

Generate BDD feature file.

Return ONLY valid JSON object.

JSON schema:
{{
  "feature_name": "Feature name",
  "description": "Short description",
  "scenarios": [
    "Scenario: ...\\nGiven ...\\nWhen ...\\nThen ..."
  ]
}}

IMPORTANT:
- Return ONLY JSON.
- No markdown.
- No explanation.
"""

TESTDATA_PROMPT = """
You are a Senior QA Engineer.

Requirement:
{requirement}

Generate test data.

Return ONLY valid JSON array of objects.
Each object MUST contain ALL keys.

JSON schema example:
[
  {{"email":"valid@gmail.com","password":"Pass@123","type":"valid"}},
  {{"email":"invalid@gmail.com","password":"wrong","type":"invalid"}}
]

IMPORTANT:
- Return ONLY JSON.
- No markdown.
- No explanation.
"""
