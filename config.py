import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "NeevAI"
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

settings = Settings()

