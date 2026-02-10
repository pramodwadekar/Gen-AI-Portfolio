### 1. Backend Setup
**- Go inside backend folder:**
>  cd backend

**- Create virtual environment:**
>  python -m venv venv

**- Activate virtual environment:**
  **Windows:**
>  venv\Scripts\activate
  **Mac/Linux:**
>  source venv/bin/activate

**- Install dependencies:**
>  pip install -r requirements.txt


### - 🔑 Groq API Key Setup (FREE)

**Step 1: Create Groq Account**

**Go to:**
> https://console.groq.com

**Step 2: Create API Key**

 - Go to API Keys

 - Click Create Key

 - Copy the key

**Step 3: Create .env**

 Inside backend/ folder create:

 - 📄 backend/.env

>  GROQ_API_KEY=your_groq_api_key_here


**- Create .env file (Groq API Key)**
  **Inside:**
>  backend/.env
  **Add this:**
>  GROQ_API_KEY=your_groq_api_key_here


### - Project Structure

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

### - After adding all folder and codes
  
**2️⃣ Run Backend**

**Inside backend folder run:**

>  uvicorn app.main:app --reload


**Backend will start at:**
👉 http://127.0.0.1:8000


**3️⃣ Run Frontend**

**Open a new terminal.**

**Go to project root:**

>  cd ..


**Run Streamlit:**

>  streamlit run frontend/app.py


**Frontend will start at:**
👉 http://localhost:8501

