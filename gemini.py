import google.generativeai as genai
from core.config import settings
from fastapi import HTTPException

# Configure Gemini
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)
else:
    print("WARNING: GEMINI_API_KEY is not set.")

def get_chat_model():
    # Model for ECI Chatbot
    system_instruction = (
        "You are an expert on the Indian Election Process and the Representation of the People Act 1951. "
        "You must provide neutral, non-partisan, and accurate information about election procedures, voting rights, "
        "and eligibility in India. Do not answer questions unrelated to elections or civics."
    )
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction
    )

def get_translation_model():
    # Model for Translation
    return genai.GenerativeModel(model_name="gemini-1.5-flash")

async def translate_text(text: str, target_lang: str) -> str:
    lang_map = {
        "en": "English",
        "hi": "Hindi",
        "ta": "Tamil",
        "bn": "Bengali",
        "te": "Telugu"
    }
    lang_name = lang_map.get(target_lang)
    if not lang_name:
        raise HTTPException(status_code=400, detail="Unsupported language")
    
    prompt = f"Translate the following text to {lang_name}. Only output the translated text, nothing else.\n\nText: {text}"
    try:
        model = get_translation_model()
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Translation Error: {e}")
        raise HTTPException(status_code=500, detail="Translation failed")
