from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/booth")
async def get_booth(pincode: str):
    if not pincode.isdigit() or len(pincode) != 6:
        raise HTTPException(status_code=400, detail="Invalid pincode. Must be exactly 6 digits.")
        
    # Maps embed link
    embed_url = f"https://www.google.com/maps?q=polling+booth+near+{pincode}+India&output=embed"
    open_url = f"https://www.google.com/maps/search/polling+booth+near+{pincode}+India"
    
    return {
        "embed_url": embed_url,
        "open_url": open_url
    }
