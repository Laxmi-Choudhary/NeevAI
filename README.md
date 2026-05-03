# 🌱 NeevAI — AI-Powered Government Schemes Assistant

NeevAI is a full-stack AI-powered web application that helps citizens discover and understand government welfare schemes and programs. It bridges the gap between citizens and the benefits they deserve by making information accessible, multilingual, and interactive.

---

## 🌐 Live Demo : https://neevai-frontend-294690858332.asia-south1.run.app/

- **Frontend:** https://neev-ai.vercel.app
- **Backend API:** https://neevai-backend.onrender.com

---

## ✨ Features

- 🤖 **AI Chat Assistant** — Ask questions about government schemes and get instant answers powered by Google Gemini
- ✅ **Eligibility Checker** — Find out which schemes you qualify for based on your profile
- 📝 **Quiz Section** — Interactive quiz to discover relevant government programs
- 📅 **Timeline & Calendar** — Track important dates and deadlines for schemes
- 🌍 **Multi-language Translation** — Access information in your preferred language
- 🎥 **Video Resources** — Watch explainer videos for better understanding
- 📍 **Booth Locator** — Find nearby government service booths

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose |
|---|---|
| React + Vite | UI Framework |
| Tailwind CSS | Styling |
| Vercel | Deployment |

### Backend
| Technology | Purpose |
|---|---|
| Python FastAPI | REST API |
| Google Gemini API | AI Chat & Translation |
| Firebase | Database & Hosting |
| Render | Deployment |

---

## 📁 Project Structure

NeevAI/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── ...
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── vercel.json
│
└── backend/
    ├── main.py
    ├── requirements.txt
    ├── Dockerfile
    ├── core/
    │   ├── config.py
    │   └── database.py
    ├── routes/
    │   ├── chat.py
    │   ├── eligibility.py
    │   ├── quiz.py
    │   ├── timeline.py
    │   ├── calendar.py
    │   ├── translate.py
    │   ├── videos.py
    │   └── booth.py
    └── services/
        └── gemini.py

---

## 🚀 Getting Started

### Frontend Setup

git clone https://github.com/Laxmi-Choudhary/NeevAI.git
cd NeevAI/frontend
npm install
npm run dev

### Backend Setup

cd NeevAI/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

---

## 🌍 Deployment

### Frontend → Vercel
1. Push code to GitHub
2. Import repo on vercel.com
3. Set Root Directory to frontend
4. Add environment variable: VITE_API_URL=https://your-render-url.onrender.com
5. Click Deploy

### Backend → Render
1. Import repo on render.com
2. Set Root Directory to backend
3. Set Runtime to Python 3
4. Set Build Command: pip install -r requirements.txt
5. Set Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
6. Add environment variables from .env
7. Click Create Web Service

---

## 🔑 Environment Variables

### Frontend (.env)
VITE_API_URL=https://your-backend-url.onrender.com

### Backend (.env)
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=your_database_url

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Health check |
| POST | /chat | AI chat response |
| POST | /eligibility | Check scheme eligibility |
| GET | /quiz | Get quiz questions |
| GET | /timeline | Get scheme timeline |
| GET | /calendar | Get important dates |
| POST | /translate | Translate content |
| GET | /videos | Get video resources |
| GET | /booth | Get booth locations |

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: git checkout -b feature/your-feature
3. Commit changes: git commit -m "Add your feature"
4. Push to branch: git push origin feature/your-feature
5. Open a Pull Request

---

## 👩‍💻 Author

Laxmi Choudhary
- GitHub: @Laxmi-Choudhary
- LinkedIn: https://www.linkedin.com/in/laxmi-choudhary-a0023531b?utm_source=share_via&utm_content=profile&utm_medium=member_android
---

## 🙏 Acknowledgements

- Google Gemini API for AI capabilities
- FastAPI for the backend framework
- Vercel for frontend hosting
- Render for backend hosting

---