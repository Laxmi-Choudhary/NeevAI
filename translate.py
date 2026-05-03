from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini import translate_text

router = APIRouter()

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/translate")
async def translate_content(req: TranslateRequest):
    translated = await translate_text(req.text, req.target_lang)
    return {"translated_text": translated}
