from fastapi import APIRouter

router = APIRouter()

phases = [
    {"id": 1, "name": "Notification", "description": "Election Commission of India (ECI) announces the poll dates and notification is issued."},
    {"id": 2, "name": "Nomination", "description": "Candidates file their nomination papers with the Returning Officer."},
    {"id": 3, "name": "Scrutiny", "description": "Nomination papers are scrutinized to check for validity and completeness."},
    {"id": 4, "name": "Withdrawal", "description": "Candidates can withdraw their nominations before the final list is published."},
    {"id": 5, "name": "Campaign", "description": "Political parties and candidates campaign to present their vision to the voters."},
    {"id": 6, "name": "Polling", "description": "Voters cast their votes using Electronic Voting Machines (EVMs) at designated polling booths."},
    {"id": 7, "name": "Counting", "description": "Votes are counted under the supervision of the ECI."},
    {"id": 8, "name": "Results", "description": "Final results are declared and the process of forming the government begins."}
]

@router.get("/timeline")
async def get_timeline():
    return {"phases": phases}
