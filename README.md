# 🤖 AI Chatbot — Claude Powered

<div align="center">

![AI Chatbot](https://img.shields.io/badge/AI%20Chatbot-Claude%20Powered-00e5a0?style=for-the-badge&logo=python&logoColor=white)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io)
[![Claude](https://img.shields.io/badge/Claude-Sonnet-orange?style=flat-square)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**A production-ready AI chatbot with multiple personas, built using Claude API and Streamlit**

</div>

---

## 🧩 Problem Statement

Most chatbot demos are basic and don't show real-world features like persona switching, conversation memory, or clean UI. This project builds a **fully functional AI chatbot** that can be used for learning, interview prep, career guidance, and general Q&A — all in one app.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎭 **Multiple Personas** | Switch between Assistant, DS Tutor, Python Expert, Career Coach, Interview Prep |
| 🧠 **Conversation Memory** | Full multi-turn chat history maintained |
| 💬 **Quick Suggestions** | One-click starter questions |
| 📊 **Session Stats** | Live message & turn count |
| 🎨 **Dark UI** | Professional dark-themed chat interface |
| 🔄 **Clear Chat** | Reset conversation anytime |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **AI Model** | Anthropic Claude (claude-sonnet-4) |
| **Language** | Python 3.11 |
| **API Client** | anthropic SDK |
| **Config** | python-dotenv |

---

## 📁 Project Structure

```
ai-chatbot/
├── app.py                  # 🎨 Main Streamlit chatbot UI
├── requirements.txt        # 📦 Dependencies
├── .env.example            # 🔑 API key template
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚡ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/gaurav837/ai-chatbot.git
cd ai-chatbot
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup .env file
```bash
copy .env.example .env      # Windows
cp .env.example .env        # Mac/Linux
```
Edit `.env` and add your API key:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

### 5. Run the app
```bash
streamlit run app.py
```
Open **http://localhost:8501** 🎉

---

## 💬 Sample Conversation

```
You        → "How do I become a Data Scientist?"

Claude AI  → Great question! Here's a structured roadmap:

             📚 Step 1 - Master the Basics
             • Python (pandas, numpy, matplotlib)
             • Statistics & Probability
             • SQL for data querying

             🤖 Step 2 - Learn Machine Learning
             • Supervised: Linear/Logistic Regression, Random Forest
             • Unsupervised: K-Means, PCA
             • Tools: scikit-learn, XGBoost

             🚀 Step 3 - Build Projects
             • Start with Kaggle datasets
             • Build 3-4 end-to-end projects
             • Deploy at least one on cloud

             💼 Step 4 - Get Job Ready
             • Practice SQL interview questions
             • Learn Git & GitHub
             • Build LinkedIn profile with projects

             Start with Python if you haven't already!

You        → "Which Python libraries should I learn first?"

Claude AI  → For Data Science, learn in this order:
             1. NumPy — array operations
             2. Pandas — data manipulation
             3. Matplotlib/Seaborn — visualization
             4. Scikit-learn — machine learning
             5. Streamlit — build AI apps fast!
```

---

## 🎓 Key Learnings

- **Claude API integration** — multi-turn conversation with system prompts
- **Streamlit session state** — maintaining chat history across reruns
- **Persona engineering** — crafting system prompts for different use cases
- **Production UI** — building clean, responsive chat interfaces
- **API key management** — secure config with python-dotenv

---

## 🤝 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-gaurav837-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/gaurav837)
[![GitHub](https://img.shields.io/badge/GitHub-gaurav837-181717?style=flat-square&logo=github)](https://github.com/gaurav837)

---

⭐ **Star this repo if it helped you!**
