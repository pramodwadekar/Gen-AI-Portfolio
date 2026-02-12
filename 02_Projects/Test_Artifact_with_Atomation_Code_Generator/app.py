import streamlit as st

from utils.context_builder import build_project_context
from utils.llm_client import generate_with_gemini
from utils.prompts import (
    test_strategy_prompt,
    test_plan_prompt,
    test_scenarios_prompt,
    test_cases_prompt,
    automation_code_prompt
)

st.set_page_config(page_title="Test Artifacts Generation App", layout="wide")

st.title("🧪 Test Artifacts Generation App (Gemini + Streamlit)")

# ---------------------------
# Session state
# ---------------------------
if "baseline_context" not in st.session_state:
    st.session_state.baseline_context = ""

if "generated_output" not in st.session_state:
    st.session_state.generated_output = ""

if "scenario_list" not in st.session_state:
    st.session_state.scenario_list = []

if "do_clear" not in st.session_state:
    st.session_state.do_clear = False

# ---------------------------
# Sidebar settings
# ---------------------------
st.sidebar.header("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Gemini Model",
    [
        "models/gemini-2.5-flash",
        "models/gemini-2.5-pro",
        "models/gemini-2.0-flash"
    ]
)

detail_level = st.sidebar.radio(
    "Detail Level",
    ["Conservative", "Balanced", "Detailed"],
    index=1
)

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2, tab3 = st.tabs(["📌 Project Context", "📄 Test Artifacts", "🤖 Automation Generator"])

# ---------------------------
# TAB 1: Project Context
# ---------------------------
with tab1:
    st.header("1️⃣ Enter Project / Testing Context")

    # ✅ Clear must happen BEFORE widgets are created
    if st.session_state.do_clear:
        st.session_state.project_name = ""
        st.session_state.project_description = ""
        st.session_state.features = ""
        st.session_state.platforms = ""
        st.session_state.nfr = ""
        st.session_state.scope = ""
        st.session_state.baseline_context = ""
        st.session_state.do_clear = False

    # Inputs
    project_name = st.text_input("Project Name", key="project_name")
    project_description = st.text_area("Short Description", height=100, key="project_description")
    features = st.text_area("Key Features / Modules", height=120, key="features")
    platforms = st.text_input("Target Platforms (web/mobile/api)", key="platforms")
    nfr = st.text_area("Non-functional Concerns", height=100, key="nfr")
    scope = st.text_area("Testing Scope & Constraints", height=100, key="scope")

    # Buttons side-by-side
    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Generate Baseline Context"):
            data = {
                "project_name": project_name,
                "project_description": project_description,
                "features": features,
                "platforms": platforms,
                "nfr": nfr,
                "scope": scope
            }

            st.session_state.baseline_context = build_project_context(data)
            st.success("Baseline context generated successfully!")

    with col2:
        if st.button("🧹 Clear Form"):
            st.session_state.do_clear = True
            st.rerun()

    # Output
    st.subheader("📌 Baseline Context (Reusable)")
    st.text_area("Baseline Context", st.session_state.baseline_context, height=250)


# ---------------------------
# TAB 2: Test Artifacts
# ---------------------------
with tab2:
    st.header("2️⃣ Generate Test Artifacts")

    if not st.session_state.baseline_context:
        st.warning("⚠️ Please generate Baseline Context first (Tab 1).")
    else:
        artifact = st.selectbox(
            "Select Artifact",
            ["Test Strategy", "Test Plan", "Test Scenarios", "Test Cases"]
        )

        feature_name = ""
        if artifact == "Test Cases":
            feature_name = st.text_input("Enter Feature Name (for Test Cases)")

        if st.button("🚀 Generate Artifact"):
            if artifact == "Test Strategy":
                prompt = test_strategy_prompt(st.session_state.baseline_context, detail_level)

            elif artifact == "Test Plan":
                prompt = test_plan_prompt(st.session_state.baseline_context, detail_level)

            elif artifact == "Test Scenarios":
                prompt = test_scenarios_prompt(st.session_state.baseline_context, detail_level)

            else:
                if not feature_name.strip():
                    st.error("❌ Please enter Feature Name for Test Cases.")
                    st.stop()

                prompt = test_cases_prompt(st.session_state.baseline_context, feature_name, detail_level)

            with st.spinner("Generating..."):
                output = generate_with_gemini(prompt, model_name)

            st.session_state.generated_output = output
            # ✅ Save scenarios for Tab 3 dropdown
            if artifact == "Test Scenarios":
                lines = output.split("\n")
                extracted = []
            
                for line in lines:
                    if line.strip().startswith("|") and "Scenario" not in line and "---" not in line:
                        parts = [p.strip() for p in line.split("|") if p.strip()]
                        if len(parts) >= 2:
                            extracted.append(parts[1])  # Scenario column
            
                st.session_state.scenario_list = extracted

        st.subheader("📄 Output")
        st.markdown(st.session_state.generated_output)
        

        if st.session_state.generated_output:
            st.download_button(
                "⬇️ Download Output (.md)",
                data=st.session_state.generated_output,
                file_name=f"{artifact.replace(' ', '_')}.md",
                mime="text/markdown"
            )

# ---------------------------
# TAB 3: Placeholder (Next Phase)
# ---------------------------
with tab3:
    st.header("3️⃣ Automation Script Generator")

    if not st.session_state.baseline_context:
        st.warning("⚠️ Please generate Baseline Context first (Tab 1).")
    else:
        col1, col2 = st.columns(2)

        with col1:
            language = st.selectbox(
                "Target Language",
                ["Java", "JavaScript", "Python"]
            )

        with col2:
            framework = st.selectbox(
                "Framework",
                [
                    "Selenium + TestNG (Java)",
                    "Playwright (JavaScript)",
                    "Pytest (Python)",
                    "Cypress (JavaScript)"
                ]
            )

        st.subheader("📌 Pick Scenario (From Generated Scenarios)")

        if len(st.session_state.scenario_list) == 0:
            st.info("ℹ️ Generate 'Test Scenarios' in Tab 2 first, then scenarios will appear here.")
            scenario_text = st.text_area(
                "Enter Scenario / Test Case to Automate",
                height=180,
                placeholder="Example: User should be able to login..."
            )
        else:
            selected_scenario = st.selectbox(
                "Select a Scenario",
                st.session_state.scenario_list
            )
        
            scenario_text = st.text_area(
                "Scenario/Test Case to Automate",
                value=selected_scenario,
                height=150
            )
        

        if st.button("🤖 Generate Automation Code"):
            if not scenario_text.strip():
                st.error("❌ Please enter a Scenario/Test Case first.")
                st.stop()

            prompt = automation_code_prompt(
                project_context=st.session_state.baseline_context,
                scenario=scenario_text,
                language=language,
                framework=framework
            )

            with st.spinner("Generating automation code..."):
                output = generate_with_gemini(prompt, model_name)

            st.session_state.generated_output = output

        st.subheader("💻 Generated Automation Code")

        # Better syntax highlight
        code_lang = "text"
        if "Java" in language:
            code_lang = "java"
        elif "JavaScript" in language:
            code_lang = "javascript"
        elif "Python" in language:
            code_lang = "python"

        st.code(st.session_state.generated_output, language=code_lang)

        if st.session_state.generated_output:
            st.download_button(
                "⬇️ Download Code (.txt)",
                data=st.session_state.generated_output,
                file_name="automation_script.txt",
                mime="text/plain"
            )

