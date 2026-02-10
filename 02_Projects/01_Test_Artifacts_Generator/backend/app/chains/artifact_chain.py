import json
import re
from typing import List, Dict, Any

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from app.config import GROQ_API_KEY
from .prompts import SCENARIO_PROMPT, TESTCASE_PROMPT, BDD_PROMPT, TESTDATA_PROMPT


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=GROQ_API_KEY
)


def _extract_json(text: str) -> str:
    """
    Extract first JSON array/object from model output.
    Handles cases where model adds explanation or markdown.
    """
    text = text.strip()

    # remove markdown fences
    text = text.replace("```json", "").replace("```", "").strip()

    # find first { or [
    match = re.search(r"(\[|\{)", text)
    if not match:
        raise ValueError("No JSON start found in response")

    start = match.start()

    # find last ] or }
    end_arr = text.rfind("]")
    end_obj = text.rfind("}")

    end = max(end_arr, end_obj)
    if end == -1:
        raise ValueError("No JSON end found in response")

    return text[start:end + 1].strip()


def _safe_json_load(text: str):
    json_text = _extract_json(text)
    return json.loads(json_text)


def _ensure_scenario_schema(scenarios: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    fixed = []
    for i, sc in enumerate(scenarios, start=1):
        if not isinstance(sc, dict):
            continue

        fixed.append({
            "id": int(sc.get("id", i)),
            "title": str(sc.get("title", f"Scenario {i}")).strip(),
            "type": str(sc.get("type", "Positive")).strip()
        })
    return fixed


def _ensure_testcase_schema(testcases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    fixed = []
    for i, tc in enumerate(testcases, start=1):
        if not isinstance(tc, dict):
            continue

        steps = tc.get("steps", [])
        if isinstance(steps, str):
            steps = [steps]
        if not isinstance(steps, list):
            steps = []

        fixed.append({
            "id": int(tc.get("id", i)),
            "scenario_id": int(tc.get("scenario_id", 1)),
            "title": str(tc.get("title", f"Test Case {i}")).strip(),
            "precondition": str(tc.get("precondition", "")).strip(),
            "steps": [str(s).strip() for s in steps if str(s).strip()],
            "expected_result": str(tc.get("expected_result", "")).strip(),
            "priority": str(tc.get("priority", "P1")).strip()
        })
    return fixed


def _ensure_bdd_schema(bdd: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(bdd, dict):
        return {"feature_name": "", "description": "", "scenarios": []}

    scenarios = bdd.get("scenarios", [])
    if isinstance(scenarios, str):
        scenarios = [scenarios]
    if not isinstance(scenarios, list):
        scenarios = []

    return {
        "feature_name": str(bdd.get("feature_name", "")).strip(),
        "description": str(bdd.get("description", "")).strip(),
        "scenarios": [str(s).strip() for s in scenarios if str(s).strip()]
    }


def _ensure_testdata_schema(test_data: Any) -> List[Dict[str, Any]]:
    if not isinstance(test_data, list):
        return []

    fixed = []
    for row in test_data:
        if isinstance(row, dict):
            fixed.append(row)
    return fixed


def generate_scenarios(requirement: str):
    prompt = PromptTemplate.from_template(SCENARIO_PROMPT)
    resp = llm.invoke(prompt.format(requirement=requirement))
    scenarios = _safe_json_load(resp.content)
    return _ensure_scenario_schema(scenarios)


def generate_testcases(requirement: str, scenarios):
    prompt = PromptTemplate.from_template(TESTCASE_PROMPT)
    resp = llm.invoke(prompt.format(requirement=requirement, scenarios=json.dumps(scenarios)))
    testcases = _safe_json_load(resp.content)
    return _ensure_testcase_schema(testcases)


def generate_bdd(requirement: str):
    prompt = PromptTemplate.from_template(BDD_PROMPT)
    resp = llm.invoke(prompt.format(requirement=requirement))
    bdd = _safe_json_load(resp.content)
    return _ensure_bdd_schema(bdd)


def generate_testdata(requirement: str):
    prompt = PromptTemplate.from_template(TESTDATA_PROMPT)
    resp = llm.invoke(prompt.format(requirement=requirement))
    test_data = _safe_json_load(resp.content)
    return _ensure_testdata_schema(test_data)


def generate_all_artifacts(requirement: str):
    scenarios = generate_scenarios(requirement)
    test_cases = generate_testcases(requirement, scenarios)
    bdd = generate_bdd(requirement)
    test_data = generate_testdata(requirement)

    return {
        "scenarios": scenarios,
        "test_cases": test_cases,
        "bdd": bdd,
        "test_data": test_data
    }
