# 🧪 TestCraft AI – Test Artifacts Generator (Groq + LangChain)

TestCraft AI is a GenAI-powered application that converts a plain English requirement/user story into complete QA test artifacts such as:

- ✅ Test Scenarios

- 🧪 Detailed Test Cases

- 📌 BDD Feature (Gherkin)

- 🧾 Test Data

- ⬇️ Test Cases Excel Export

- ⬇️ .feature File Download

This project is designed for QA/SDET engineers to speed up manual test design and documentation using LLMs.

- Real-world QA artifact generation

- Backend + Frontend architecture

- LLM integration

- Robust JSON parsing

- Excel export capability

---

## 🚀 Why This Project?

In real QA projects, writing test artifacts manually takes time:

- Understanding requirements
- Creating test scenarios
- Writing detailed test cases
- Preparing BDD scenarios
- Creating test data combinations

This tool automates that process using LLMs and generates structured output in seconds.

---

## 🎯 Key Features

✅ Requirement → Test Scenarios (JSON)  
✅ Requirement + Scenarios → Detailed Test Cases (JSON)  
✅ Requirement → BDD Feature File (JSON → Gherkin)  
✅ Requirement → Test Data (JSON)  
✅ Excel Export
✅ .feature File Download

### ⭐ UI Features
- Clean Streamlit UI
- Tabs view:
  - Scenarios
  - Test Cases
  - BDD
  - Test Data

### 📥 Export Features
- Download Test Cases as **Excel (.xlsx)**
- Download BDD as **.feature file**

---

## 🏗️ Tech Stack

### Backend
- **FastAPI** – REST API server
- **LangChain** – Prompt + LLM orchestration
- **Groq API** – Free LLM inference
- **Pydantic** – Request validation
- **Uvicorn** – Server for FastAPI
- **python-dotenv** – Environment variable management

### Frontend
- **Streamlit** – UI for requirement input and output display
- **Pandas** – Display tables + prepare Excel export
- **OpenPyXL** – Excel export formatting

### 📌 Why These Libraries?

| Library        | Why Used                                                 |
| -------------- | -------------------------------------------------------- |
| fastapi        | To build a clean and fast backend API                    |
| uvicorn        | To run FastAPI server                                    |
| python-dotenv  | To load Groq API key from `.env`                         |
| pydantic       | For validating incoming JSON request                     |
| langchain      | For clean prompt handling + LLM calls                    |
| langchain-groq | Groq integration for LangChain                           |
| pandas         | Display tables + Excel export                            |
| openpyxl       | Format Excel: wrap text, auto column width, bold headers |


---

## 📂 Project Structure

01_Test_Artifacts_Generator/
│

├── backend/

│ ├── app/

│ │ ├── main.py

│ │ ├── config.py

│ │ └── chains/

│ │ ├── artifact_chain.py

│ │ └── prompts.py

│ │

│ ├── requirements.txt

│ └── .env

│
├── frontend/

│ └── app.py

│

├── Projects_Evidence/

│ ├── screenshots/

│ └── demo-video/

│

└── README.md



### 🧪 How to Use

**1. Open Streamlit UI**

**2. Paste requirement / user story**

**3. Click Generate 🚀**

**4. View results in tabs**

**5. Download:**

**- Test Cases Excel**

**- BDD .feature file**


**🧠 LLM Model Used**

This project uses Groq LLM:

- llama-3.3-70b-versatile

**Configured in:**

backend/app/chains/artifact_chain.py

**📌 Notes / Important Points**

- The model sometimes returns extra text or markdown.

- To handle this, backend includes a robust JSON extractor:

  - Removes markdown code fences

  - Extracts first valid JSON block

  - Fixes missing keys with schema validation

**🔥 Future Improvements (Planned)**

✅ Add Playwright Automation Skeleton Generator
✅ Add Selenium Java Automation Skeleton Generator
✅ Add Export for:

- Scenarios Excel

- Test Data Excel

- Full QA Pack ZIP

✅ Deploy to cloud (Render / Railway)


### Project Explaination:

✅ “I built an AI-powered test artifact generator”
✅ “It converts requirements into structured test scenarios, test cases, BDD and test data”
✅ “It includes robust JSON extraction and schema enforcement”
✅ “It supports Excel export and feature file download”
✅ “It uses FastAPI + Streamlit + LangChain + Groq”

**👨‍💻 Author**

Pramod Wadekar

