#  Life Insurance AI Assistant

An intelligent **Life Insurance Recommendation & Conversation System** built with a Python backend (Flask), a smart agent module, and a clean HTML/CSS/JS frontend. This project helps users understand and select the right insurance plan through natural, interactive conversations.

---

##  Project Structure

```
life_insurance/
├── backend/
│   ├── app.py                
│   ├── agent.py             
│   ├── insurance_data.py    
│   ├── db.py                 
│   ├── conversation.db       
│   ├── requirements.txt     
│   └── .env                 
│
├── frontend/
│   ├── index.html            
│   ├── style.css            
│   └── script.js           
│
└── ven/                     
```

---
<img width="795" height="847" alt="Image" src="https://github.com/user-attachments/assets/24562df3-4768-4eae-bd8c-d777e8df4827" />
##  Project Overview

This project is designed to make **life insurance selection simple and interactive**.
Instead of giving users long documents to read, the system provides a **chat-based interface** where users can ask questions and be guided to the right insurance policy.

Your AI agent handles:

* Understanding customer intent
* Asking relevant questions (age, income, dependents, budget, etc.)
* Recommending the most appropriate insurance plan
* Explaining insurance terms in friendly language
* Storing and retrieving conversation history

It works perfectly for **banks**, **insurance call centers**, or **web-based self-service portals**.

---

##  Backend (Flask + AI Agent)

The backend is built with **Python/Flask** and includes:

### ✔ `agent.py`

Handles natural language understanding and response generation.
It reads user messages, checks conditions, fetches the right insurance data, and produces meaningful replies.

###  `insurance_data.py`

Contains structured information about different life insurance plans such as:

* Term Life
* Whole Life
* Endowment
* Child Education Plan
* Retirement Plan

Each plan includes **benefits, premium ranges, eligibility, and ideal customer type**.

###  `db.py`

A tiny SQLite wrapper used to store:

* User conversation logs
* Query histories
* Analysis patterns

###  `app.py`

The main server that connects frontend → AI agent → output.
Exposes clean REST APIs for communication.

---

##  Frontend (HTML, CSS, JavaScript)

The frontend provides a modern chat interface.

### Features:

* Clean UI for conversation
* Smooth message bubbles
* API integration to the backend
* Auto-scrolling chat window
* Loading animations ✨

Files:

* **index.html** – Chat layout
* **style.css** – Gradient theme and chat styling
* **script.js** – Sends user messages to `/api/message` and shows the response

---

##  Installation & Setup

###  Create and activate virtual environment

```bash
python -m venv ven
source ven/bin/activate    # On Windows: ven\Scripts\activate
```

###  Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

###  Add environment variables

Create `.env` file with:

```
API_KEY=your_key_here
MODEL_NAME=your_model_here
```

###  Run backend server

```bash
python app.py
```

###  Open the frontend

Just open `frontend/index.html` in your browser.

---

##  How It Works (Simple Explanation)

1. User sends a message from the frontend.
2. Backend receives it and forwards to the AI agent.
3. AI agent analyzes the user's need.
4. Using `insurance_data.py`, it finds matching plans.
5. It generates a helpful explanation and recommendation.
6. Conversation is stored for future reference.



---
## Final Output : 
<img width="782" height="855" alt="Image" src="https://github.com/user-attachments/assets/571035fc-d1d2-4ef2-866b-779f5e41744d" />

##  Future Improvements

* Integration with real insurance APIs
* Voice-based assistant
* Bengali/Multilingual support �️
* Dynamic premium calculation
* Admin dashboard for analytics

---

