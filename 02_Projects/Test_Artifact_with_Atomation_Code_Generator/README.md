# 🧪 Test Artifacts Generation App (Gemini + Streamlit)

A Streamlit-based Generative AI application that helps QA / SDET teams quickly create **test planning artifacts** and **starter automation scripts** by calling **Google Gemini**.

This project is designed to be:
- Simple to run locally
- Easy to extend (add more artifact types, export formats, better parsing)
- Suitable for assignments / portfolio demos

---

## ✅ What We Built (Features)

### 1) Project / Testing Context (Tab 1)
You enter the project details:

- Project Name  
- Short Description  
- Key Features / Modules  
- Target Platforms (web / mobile / api)  
- Non-functional Concerns (performance, security, usability)  
- Testing Scope & Constraints (time, tools, resources)

Then click:

✅ **Generate Baseline Context**  
This creates a reusable **Baseline Context** that is used in every prompt.

Also included:

🧹 **Clear Form**  
Clears all input fields + baseline context safely using Streamlit rerun logic.

---

### 2) Generate Test Artifacts (Tab 2)
Using the baseline context, you can generate:

- **Test Strategy**
- **Test Plan**
- **Test Scenarios**
- **Test Cases** (requires Feature Name)

The output is displayed in a readable Markdown format (tables where needed).

---

### 3) Automation Script Generator (Tab 3)
You can generate **starter automation code** (not full production framework) using:

- Language: Java / JavaScript / Python  
- Framework:
  - Selenium + TestNG (Java)
  - Playwright (JavaScript)
  - Pytest (Python)
  - Cypress (JavaScript)

You paste a scenario/test case and click:

🤖 **Generate Automation Code**

Output is shown in a code block with syntax highlighting + download button.

---

### 4) Scenario Dropdown (No Copy Paste Needed)
If you generate **Test Scenarios** in Tab 2:

- The app automatically extracts scenario text
- Tab 3 shows a dropdown
- You can pick a scenario directly and generate automation code

---

## 🧩 Recommended Folder Structure

```
test-artifacts-app/
│
├─ app.py
├─ requirements.txt
├─ .env                 # never commit this
├─ README.md
│
└─ utils/
   ├─ llm_client.py
   ├─ prompts.py
   └─ context_builder.py
```

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Streamlit** (UI)
- **Google Gemini API** (LLM)
- **google-genai** (official new Gemini SDK)
- (Optional) **LangChain** structure in prompts (we kept it simple)

---

## 🔑 Gemini API (Free or Paid?)

We are using a Google AI Studio API key.

✅ Gemini provides a free tier  
⚠️ But it has usage limits (quota / rate limits)

Recommended model for this project:

✅ `models/gemini-2.5-flash` (fast + quota friendly)

---

# 🚀 Setup Guide (Step-by-Step)

Follow these steps on any new laptop.

---

## 1) Install Python

Install **Python 3.10+** (recommended: Python 3.11).

Verify:

```bash
python --version
```

---

## 2) Create Project Folder

Example:

```bash
mkdir test-artifacts-app
cd test-artifacts-app
```

---

## 3) Create Virtual Environment

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4) Install Dependencies

Create `requirements.txt` with:

```txt
streamlit
python-dotenv
google-genai
```

Now install:

```bash
pip install -r requirements.txt
```

---

## 5) Create `.env` File

Create a file named:

`.env`

Inside it:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

⚠️ IMPORTANT:
- Do NOT commit `.env` to GitHub
- Keep it private

---

## 6) Get Gemini API Key (AI Studio)

1. Open Google AI Studio
2. Create API key
3. Copy it
4. Paste into `.env`

---

## 7) Create `utils/` Folder

```bash
mkdir utils
```

---

# 🧠 Code Files (What Each File Does)

---

## 1) `utils/llm_client.py`

Responsible for:
- Reading API key
- Calling Gemini model
- Returning response text

Example structure:

```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def generate_with_gemini(prompt: str, model_name: str):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "ERROR: GOOGLE_API_KEY not found in .env"

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text or ""
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"
```

---

## 2) `utils/context_builder.py`

Responsible for:
- Taking user input fields
- Building a reusable project context string

Example:

```python
def build_project_context(data: dict) -> str:
    return f"""
Project Name: {data.get('project_name')}

Short Description:
{data.get('project_description')}

Key Features / Modules:
{data.get('features')}

Target Platforms:
{data.get('platforms')}

Non-functional Concerns:
{data.get('nfr')}

Testing Scope & Constraints:
{data.get('scope')}
""".strip()
```

---

## 3) `utils/prompts.py`

Contains:
- Base system prompt
- Prompt templates for each artifact type
- Automation code prompt

Example:

```python
BASE_SYSTEM_PROMPT = """
You are a senior QA architect and test automation engineer.
Generate outputs in clean Markdown.
Do not use HTML tags.
""".strip()
```

---

## 4) `app.py`

Responsible for:
- Streamlit UI
- Tabs
- Session state
- Calling prompt builders + Gemini client
- Rendering output

Tabs:
1. Project Context
2. Test Artifacts
3. Automation Generator

---

# 🧪 How to Run the App

Inside the project folder:

```bash
streamlit run app.py
```

Streamlit will open:

```
http://localhost:8501
```

---

# 🧪 How to Use the App (User Flow)

---

## Step 1: Generate Baseline Context
Go to **Tab 1**.

Fill inputs:

- Project Name
- Short Description
- Key Features
- Platforms
- NFR
- Scope

Click:

✅ Generate Baseline Context

---

## Step 2: Generate Test Artifacts
Go to **Tab 2**.

Select:

- Test Strategy OR
- Test Plan OR
- Test Scenarios OR
- Test Cases

If you choose **Test Cases**, you must enter:

📌 Feature Name  
Example: `Login`, `User Registration`, `Money Transfer`

Click:

🚀 Generate Artifact

---

## Step 3: Generate Automation Code
Go to **Tab 3**.

Pick:

- Language
- Framework

Then either:
- Paste scenario manually, OR
- Pick from scenario dropdown (if generated in Tab 2)

Click:

🤖 Generate Automation Code

---

# 🧹 Clear Form Button (Tab 1)

Streamlit does not allow changing widget keys directly after instantiation.

So we implemented a safe clear flow:

- Clear button sets a flag: `do_clear = True`
- `st.rerun()` triggers rerun
- On rerun, values are cleared BEFORE widgets are created

This avoids StreamlitAPIException.

---

# 🧾 Example Inputs (Copy-Paste)

### Example Project Name
```
E-Commerce Web App
```

### Short Description
```
An online shopping platform where users can browse products, add items to cart, and place orders.
```

### Key Features
```
Login, Registration, Product Search, Add to Cart, Checkout, Payment, Order History
```

### Platforms
```
Web + API
```

### Non-functional
```
Performance, Security, Usability
```

### Scope
```
UI + API testing. Automation using Selenium and Playwright. Limited time: 2 weeks.
```

---

# 🛠 Troubleshooting

---

## 1) Model Not Found (404 NOT_FOUND)

If you see:

`models/gemini-1.5-flash is not found`

It means your API key does not support that model.

Use one of these (verified working):

- `models/gemini-2.5-flash`
- `models/gemini-2.5-pro`
- `models/gemini-2.0-flash`

---

## 2) API Key Missing
If you see:

`ERROR: GOOGLE_API_KEY not found`

Fix:
- Ensure `.env` exists
- Ensure it contains:
  `GOOGLE_API_KEY=...`

---

## 3) Rate Limit / Quota
If you see quota errors:
- Switch to `models/gemini-2.5-flash`
- Wait some time
- Reduce generation frequency

---

# 🔥 Future Improvements (Optional)

If you want to extend this project later:

- Export outputs as PDF / DOCX
- Save artifacts per project
- Add login to app
- Add history view
- Add JSON output mode for structured parsing
- Add better scenario parsing (extract ID + priority + type)
- Add “Regenerate” options (conservative vs detailed)
- Add multiple artifact generation in one click

---

# ✅ Final Notes

This project is perfect for:
- SDET portfolio
- GenAI assignment submission
- Internal QA productivity tool demo

If you want, we can also add:
- GitHub-ready `.gitignore`
- Screenshots folder
- Deployment guide (Streamlit Cloud)

---

Happy Testing 🚀
