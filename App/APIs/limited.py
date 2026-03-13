# from fastapi import APIRouter, Request, HTTPException
# from App.rate_limiters.store import get_bucket

# router = APIRouter()

# @router.get("/limited")
# async def limited(request: Request):
#     ip = request.client.host

#     bucket = get_bucket(ip)

#     if not bucket.allow_request():
#         raise HTTPException(
#             status_code=429,
#             detail="Too many requests"
#         )

#     return {"message": "Limited endpoint accessed"}

from fastapi import APIRouter

router = APIRouter()

@router.get("/limited")
async def limited():
    return {"message": "Limited endpoint accessed"}