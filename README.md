# ❄️📧 Cold Email Generator

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-✓-orange?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-vikasgautam2003-black?style=for-the-badge&logo=github)](https://github.com/vikasgautam2003/cold-email-generator)

---

## 🚀 About
A **Cold Email Generator** that leverages AI & LangChain to help you craft personalized emails quickly. Perfect for outreach, marketing, and networking!  

💡 Features:  
- 🔹 Generates cold emails based on your inputs  
- 🔹 Stores vectorized data for better personalization  
- 🔹 Easy to run locally or deploy  

---

## 🛠️ Technologies
- Python 🐍  
- Streamlit 🌊  
- LangChain 🤖  
- Chroma Vector Store 🗄️  
- Git & GitHub 🐙  

---

## ⚡ Installation
```bash
# Clone the repo
git clone https://github.com/vikasgautam2003/cold-email-generator.git
cd cold-email-generator

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt


🏃‍♂️ Running the App
# Run Streamlit app
streamlit run app/main.py


Open your browser and go to http://localhost:8501 🌐

📝 Batch Commands (💻 one-liner)
# Clone, setup, and run (all in one)
git clone https://github.com/vikasgautam2003/cold-email-generator.git && \
cd cold-email-generator && \
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
streamlit run app/main.py

🔐 Secrets & Environment Variables

⚠️ Never commit .env files with API keys!

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here

📦 Folder Structure
cold-email-generator/
├── app/                  # Streamlit app code
├── vectorstore/          # Chroma vector DB
├── requirements.txt      # Python dependencies
├── Dockerfile            # Optional containerization
├── .env                  # Secrets (not tracked)
└── README.md             # This file

🎯 Usage

Add your contacts or inputs

Generate cold emails with AI 💌

Copy, send, and impress 🚀

❤️ Contributions

Feel free to open an issue or submit a pull request! 🌟
