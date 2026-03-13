from fastapi import FastAPI
from App.rate_limiters.middleware import RateLimitMiddleware

app = FastAPI()

app.add_middleware(RateLimitMiddleware)

from App.APIs.limited import router as limited_router
from App.APIs.unlimited import router as unlimited_router

app.include_router(limited_router)
app.include_router(unlimited_router)