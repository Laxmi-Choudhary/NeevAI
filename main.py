from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from core.database import connect_to_mongo, close_mongo_connection
from core.config import settings

from routes import health, timeline, quiz, eligibility, booth, calendar, videos, chat, translate

# Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title=settings.PROJECT_NAME)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS - Restricted in production
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://neevai-frontend-294690858332.asia-south1.run.app",
    "https://neevai-2026.web.app",
    "https://neevai-2026.firebaseapp.com"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for Body Size Limit (1KB for chat)
@app.middleware("http")
async def limit_body_size(request: Request, call_next):
    if request.url.path == "/api/chat" and request.method == "POST":
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > 1024:
            raise HTTPException(status_code=413, detail="Request body too large (max 1KB)")
    return await call_next(request)

# Startup and Shutdown Events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Include Routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(timeline.router, prefix="/api", tags=["Timeline"])
app.include_router(quiz.router, prefix="/api", tags=["Quiz"])
app.include_router(eligibility.router, prefix="/api", tags=["Eligibility"])
app.include_router(booth.router, prefix="/api", tags=["Booth"])
app.include_router(calendar.router, prefix="/api", tags=["Calendar"])
app.include_router(videos.router, prefix="/api", tags=["Videos"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(translate.router, prefix="/api", tags=["Translate"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

