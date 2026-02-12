def build_project_context(data: dict) -> str:
    return f"""
Project Name: {data.get("project_name")}

Short Description:
{data.get("project_description")}

Key Features / Modules:
{data.get("features")}

Target Platform(s):
{data.get("platforms")}

Non-Functional Concerns:
{data.get("nfr")}

Testing Scope & Constraints:
{data.get("scope")}
""".strip()
