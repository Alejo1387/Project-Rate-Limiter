from fastapi import APIRouter

router = APIRouter()

@router.get("/limited")
async def limited():
    return {"message": "This is a limited endpoint."}