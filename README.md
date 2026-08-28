 # Multi-Agent Hiring System

An AI-powered candidate evaluation system that uses multiple specialized AI agents to analyze candidates from resumes, transcripts, and job descriptions.

The system combines **independent agent evaluation, evidence extraction, multi-agent debate, and final decision analysis** to provide a structured hiring assessment.

---

## 🚀 Overview

Traditional candidate screening can be time-consuming and may rely heavily on a single evaluator's perspective.

The **Multi-Agent Hiring System** approaches candidate evaluation through multiple independent perspectives.

Each AI agent focuses on a different aspect of the candidate:

* 🔧 **Technical Agent** — evaluates technical skills and role readiness
* 👥 **HR / Culture Agent** — evaluates communication, teamwork, and professional fit
* 💼 **Hiring Manager Agent** — evaluates overall suitability for the role
* 🔎 **Skeptic Agent** — identifies evidence gaps, risks, and unsupported claims

The agents then participate in a **multi-agent debate**, allowing different assessments to be compared before generating a final recommendation.

---

## ✨ Key Features

### 📄 Multi-Document Input

Upload candidate information such as:

* Resume
* Academic transcript
* Job description

### 🤖 Multi-Agent Evaluation

Independent AI agents analyze the candidate from different perspectives.

### 📚 Evidence-Based Assessment

The system identifies supporting evidence from the provided candidate information.

### ⚔️ Multi-Agent Debate

Agent opinions are compared to identify disagreements, concerns, and areas of consensus.

### ⚖️ Final Decision

A final evaluation combines the agent assessments and evidence into a structured recommendation.

### 📊 Visual Analytics

Candidate scores and agent evaluations are presented through interactive charts.

### 📥 Evaluation Export

The completed evaluation can be downloaded for further review.

---

## 🧠 System Architecture

```text
                ┌─────────────────────┐
                │   Candidate Input   │
                │                     │
                │ Resume              │
                │ Transcript          │
                │ Job Description     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Candidate Profile   │
                │      Builder        │
                └──────────┬──────────┘
                           │
                           ▼
          ┌─────────────────────────────────┐
          │        Independent Agents       │
          │                                 │
          │ 🔧 Technical                    │
          │ 👥 HR / Culture                 │
          │ 💼 Hiring Manager               │
          │ 🔎 Skeptic                      │
          └───────────────┬─────────────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   Evidence Analysis │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Multi-Agent       │
                │      Debate         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Final Decision    │
                │                     │
                │ Recommendation      │
                │ Confidence          │
                │ Score               │
                └─────────────────────┘
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **OpenAI API**
* **AI Multi-Agent Architecture**
* **Pandas**
* **Matplotlib**
* **Python-dotenv**

---

## 📁 Project Structure

```text
Multi-Agent-Hiring-System/
│
├── app.py
├── agents.py
├── debate.py
├── decision.py
├── profile_builder.py
├── llm.py
├── config.py
│
├── utils/
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abdulhamzabaig008/Multi-Agent-Hiring-System.git
cd Multi-Agent-Hiring-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the project without activating the environment by using the Python executable inside `venv`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

**Never commit your `.env` file or API key to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔄 Evaluation Workflow

```text
Upload Candidate Documents
          ↓
Build Candidate Profile
          ↓
Run Independent AI Agents
          ↓
Extract Supporting Evidence
          ↓
Compare Agent Assessments
          ↓
Multi-Agent Debate
          ↓
Generate Final Decision
          ↓
Display Results & Export Evaluation
```

---

## 🎯 Why Multi-Agent Evaluation?

A single AI evaluation can overlook important information or produce overly optimistic conclusions.

This system introduces multiple perspectives:

| Agent                 | Primary Focus              |
| --------------------- | -------------------------- |
| 🔧 Technical Agent    | Technical readiness        |
| 👥 HR / Culture Agent | Professional and team fit  |
| 💼 Hiring Manager     | Overall hiring suitability |
| 🔎 Skeptic            | Risks and evidence gaps    |

The debate stage allows these perspectives to challenge one another before the final recommendation is generated.

---

## 🔐 Security

API credentials are stored using environment variables.

Sensitive files such as:

```text
.env
venv/
__pycache__/
```

are excluded through `.gitignore`.

**Never expose API keys in source code or public repositories.**

---

## 📌 Project Status

**Working Prototype**

The system currently supports:

* Candidate document input
* AI-powered agent evaluation
* Evidence analysis
* Multi-agent debate
* Candidate scoring
* Final recommendation
* Visual evaluation
* Report export

---

## 🔮 Future Improvements

Potential future enhancements include:

* Candidate comparison
* Job-role matching scores
* More specialized evaluation agents
* Persistent evaluation history
* Authentication and user accounts
* Improved document parsing
* Bias detection and fairness analysis
* Human-in-the-loop review
* Deployment as a production web application

---

## 👨‍💻 Project

**Multi-Agent Hiring System**

Built as an AI-powered candidate evaluation prototype demonstrating how multiple specialized AI agents can collaborate to support structured decision-making.
