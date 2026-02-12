BASE_SYSTEM_PROMPT = """
You are a Senior QA Architect.
You generate test artifacts in clean structured Markdown.

Rules:
- Do not hallucinate features.
- If assumptions are needed, list them.
- Use professional QA language.
"""

def test_strategy_prompt(project_context: str, detail_level: str):
    return f"""
{BASE_SYSTEM_PROMPT}

Project Context:
{project_context}

Task:
Create a complete Test Strategy.

Detail Level: {detail_level}

Output Format (Markdown):
- Overview
- Scope
- In Scope
- Out of Scope
- Test Types
- Test Approach
- Test Environment
- Tools
- Entry Criteria
- Exit Criteria
- Risks & Mitigation
- Assumptions
"""

def test_plan_prompt(project_context: str, detail_level: str):
    return f"""
{BASE_SYSTEM_PROMPT}

Project Context:
{project_context}

Task:
Create a complete Test Plan.

Detail Level: {detail_level}

Output Format (Markdown):
- Objective
- Scope
- Test Deliverables
- Test Approach
- Test Schedule (high level)
- Roles & Responsibilities
- Environment
- Test Data Strategy
- Defect Management
- Entry/Exit Criteria
- Risks & Mitigation
- Assumptions
"""

def test_scenarios_prompt(project_context: str, detail_level: str):
    return f"""
{BASE_SYSTEM_PROMPT}

Project Context:
{project_context}

Task:
Generate test scenarios.

Detail Level: {detail_level}

Output Format:
Return a Markdown table:

ID | Scenario | Priority | Type(UI/API) | Notes
"""

def test_cases_prompt(project_context: str, feature: str, detail_level: str):
    return f"""
{BASE_SYSTEM_PROMPT}

Project Context:
{project_context}

Feature:
{feature}

Task:
Generate detailed test cases.

Detail Level: {detail_level}

IMPORTANT RULES:
- Do NOT use HTML tags like <br>, <b>, <i>.
- Do NOT use newline breaks inside table cells.
- Keep Steps in one line using "1) ... 2) ... 3) ..." format.
- Keep Expected Result in one line.

Output Format:
Return ONLY a Markdown table:

ID | Title | Preconditions | Steps | Expected Result | Priority
"""


def automation_code_prompt(project_context: str, scenario: str, language: str, framework: str):
    return f"""
{BASE_SYSTEM_PROMPT}

Project Context:
{project_context}

Scenario/Test Case to Automate:
{scenario}

Task:
Generate STARTER automation code (not full production framework).

Must Follow:
- Use {language}
- Use {framework}
- Use Arrange-Act-Assert OR Given-When-Then style
- Add meaningful assertions
- Use clean naming
- Do NOT add HTML tags
- Output ONLY code (no explanation)
- Include comments where required

Return:
Only one code block.
"""
