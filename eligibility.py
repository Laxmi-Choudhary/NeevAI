from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class EligibilityCheck(BaseModel):
    is_citizen: bool
    age: int = Field(..., ge=1, le=120)
    has_address_proof: bool
    is_sound_mind: bool
    not_disqualified: bool


@router.post("/eligibility/check")
async def check_eligibility(data: EligibilityCheck):
    reasons = []
    eligible = True
    
    if not data.is_citizen:
        eligible = False
        reasons.append("You must be an Indian citizen to vote.")
    if data.age < 18:
        eligible = False
        reasons.append(f"You must be at least 18 years old. You are currently {data.age}.")
    if not data.has_address_proof:
        eligible = False
        reasons.append("You need a valid address proof to register in a constituency.")
    if not data.is_sound_mind:
        eligible = False
        reasons.append("You must be of sound mind as declared by a competent court.")
    if not data.not_disqualified:
        eligible = False
        reasons.append("You must not be disqualified under any law relating to corrupt practices or offences.")
        
    next_steps = []
    if eligible:
        next_steps = [
            "Visit the National Voters' Service Portal (NVSP) website.",
            "Fill Form 6 to register as a new voter.",
            "Upload your passport size photograph, age proof, and address proof.",
            "Track your application status online."
        ]
        
    return {
        "eligible": eligible,
        "reasons": reasons if not eligible else ["You meet all the basic criteria!"],
        "next_steps": next_steps
    }
