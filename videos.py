from fastapi import APIRouter

router = APIRouter()

@router.get("/videos")
async def get_videos():
    # Placeholder curated videos (actual informative videos from ECI or news)
    videos = [
        {
            "id": "T0WvJrxtksg",
            "title": "How to Vote - Step by Step Guide",
            "embed_url": "https://www.youtube.com/embed/T0WvJrxtksg"
        },
        {
            "id": "W7_e2lXQZg8",
            "title": "Understanding the EVM and VVPAT",
            "embed_url": "https://www.youtube.com/embed/W7_e2lXQZg8"
        },
        {
            "id": "dQw4w9WgXcQ", # Placeholder
            "title": "Election Commission of India - Role and Responsibilities",
            "embed_url": "https://www.youtube.com/embed/dQw4w9WgXcQ"
        }
    ]
    return {"videos": videos}
