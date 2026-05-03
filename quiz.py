from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# 7 questions about the Indian Election Process
questions_db = [
    {
        "id": 1,
        "question": "What is the minimum voting age in India?",
        "options": ["16 years", "18 years", "21 years", "25 years"],
        "correct_index": 1,
        "explanation": "The 61st Amendment Act of 1988 lowered the voting age from 21 to 18 years."
    },
    {
        "id": 2,
        "question": "Who conducts the Lok Sabha elections in India?",
        "options": ["State Election Commission", "President of India", "Election Commission of India", "Supreme Court"],
        "correct_index": 2,
        "explanation": "The Election Commission of India (ECI) is an autonomous constitutional authority responsible for administering election processes in India at national, state and district level."
    },
    {
        "id": 3,
        "question": "What does EVM stand for?",
        "options": ["Electronic Voting Machine", "Electoral Voting Mechanism", "Election Verification Machine", "Electric Vote Meter"],
        "correct_index": 0,
        "explanation": "EVM stands for Electronic Voting Machine, which is used to record votes electronically."
    },
    {
        "id": 4,
        "question": "Which article of the Indian Constitution grants the power to the Election Commission?",
        "options": ["Article 370", "Article 324", "Article 356", "Article 280"],
        "correct_index": 1,
        "explanation": "Article 324 of the Constitution provides that the power of superintendence, direction, and control of elections shall be vested in the Election Commission."
    },
    {
        "id": 5,
        "question": "What is 'VVPAT'?",
        "options": ["Voter Verifiable Paper Audit Trail", "Voting Verification Process And Time", "Visual Vote Proof And Tally", "Valid Voter Public Audit Test"],
        "correct_index": 0,
        "explanation": "VVPAT stands for Voter Verifiable Paper Audit Trail, providing a paper slip to voters to verify that their vote was cast correctly."
    },
    {
        "id": 6,
        "question": "How many phases does a typical Indian general election have?",
        "options": ["Always 1 phase", "Varies, typically 7-8 phases", "Always 3 phases", "Varies, typically 2 phases"],
        "correct_index": 1,
        "explanation": "Due to the massive scale, general elections are held in multiple phases, typically 7 to 8 phases, to ensure security and smooth conduct."
    },
    {
        "id": 7,
        "question": "What does NOTA stand for?",
        "options": ["None of the Above", "No Other True Alternative", "Not Offered To Anyone", "National Option To Abstain"],
        "correct_index": 0,
        "explanation": "NOTA stands for 'None of the Above', allowing voters to officially reject all candidates."
    }
]

class SubmitAnswer(BaseModel):
    answers: List[int] # List of chosen option indices

@router.get("/quiz")
async def get_quiz():
    # Return questions without correct_index and explanation
    return {
        "questions": [
            {
                "id": q["id"],
                "question": q["question"],
                "options": q["options"]
            }
            for q in questions_db
        ]
    }

@router.post("/quiz/submit")
async def submit_quiz(data: SubmitAnswer):
    if len(data.answers) != len(questions_db):
        raise HTTPException(status_code=400, detail="Mismatch in number of answers submitted.")
    
    score = 0
    breakdown = []
    
    for idx, q in enumerate(questions_db):
        is_correct = (data.answers[idx] == q["correct_index"])
        if is_correct:
            score += 1
        breakdown.append({
            "id": q["id"],
            "is_correct": is_correct,
            "correct_answer": q["options"][q["correct_index"]],
            "explanation": q["explanation"]
        })
        
    # Badges: 0-3 Civic Learner, 4-6 Pro, 7 Champion
    if score == 7:
        badge = "Champion"
    elif score >= 4:
        badge = "Pro"
    else:
        badge = "Civic Learner"
        
    return {
        "score": score,
        "total": len(questions_db),
        "badge": badge,
        "breakdown": breakdown
    }
