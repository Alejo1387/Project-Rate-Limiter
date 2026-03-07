from fastapi import APIRouter

router = APIRouter()

@router.get("/unlimited")
async def unlimited():
    return {"message": "Unlimited! Let's Go!"}