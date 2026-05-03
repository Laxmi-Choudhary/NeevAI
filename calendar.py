from fastapi import APIRouter
import urllib.parse

router = APIRouter()

@router.get("/calendar/events")
async def get_events():
    events = [
        {
            "title": "Voter Registration Deadline",
            "date": "20240415T180000Z/20240415T190000Z",
            "details": "Last day to register as a voter or update your details."
        },
        {
            "title": "Election Day Phase 1",
            "date": "20240419T023000Z/20240419T123000Z",
            "details": "Go to your assigned polling booth and cast your vote!"
        },
        {
            "title": "Election Results Day",
            "date": "20240604T023000Z/20240604T123000Z",
            "details": "Counting of votes and declaration of results."
        }
    ]
    
    result = []
    for ev in events:
        text = urllib.parse.quote(ev["title"])
        dates = ev["date"]
        details = urllib.parse.quote(ev["details"])
        url = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={text}&dates={dates}&details={details}"
        result.append({
            "title": ev["title"],
            "google_calendar_url": url,
            "description": ev["details"]
        })
        
    return {"events": result}
