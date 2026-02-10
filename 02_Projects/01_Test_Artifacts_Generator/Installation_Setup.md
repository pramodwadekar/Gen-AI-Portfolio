1. Backend Setup
- Go inside backend folder:
  cd backend

- Create virtual environment:
  python -m venv venv

- Activate virtual environment:
  Windows:
  venv\Scripts\activate
  Mac/Linux:
  source venv/bin/activate

- Install dependencies:
  pip install -r requirements.txt

- Create .env file (Groq API Key)
  Inside:
  backend/.env
  Add this:
  GROQ_API_KEY=your_groq_api_key_here


- Project Structure
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

