from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

# from App.rate_limiters.store import get_bucket
# from App.rate_limiters.fixed_window_store import rate_limiter
# from App.rate_limiters.sliding_log_store import rate_limiter
# from App.rate_limiters.redis_store import rate_limiter

# from App.rate_limiters.lua_rate_limiter import allow_request

from App.rate_limiters.lua_rate_limiter import check_rate_limit


class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        if request.url.path == "/limited":

            ip = request.client.host

            # exercise 1: token bucket
            # bucket = get_bucket(ip)

            # if not bucket.allow_request():
            #     return JSONResponse(
            #         status_code=429,
            #         content={"detail": "Too Many Requests"}
            #     )

            # exercise 2: fixed window
            # allowed = rate_limiter.allow_request(ip)

            # if not allowed:
            #     return JSONResponse(
            #         status_code=429,
            #         content={"detail": "Too Many Requests"}
            #     )

            # exercise 3: sliding Window log
            # allowed = rate_limiter.allow_request(ip)

            # if not allowed:
            #     return JSONResponse(
            #         status_code=429,
            #         content={"detail": "Too Many Requests"}
            #     )

            # exercise 4: Redis
            # allowed = rate_limiter.allow_request(ip)

            # if not allowed:
            #     return JSONResponse(
            #         status_code=429,
            #         content={"detail": "Too Many Requests"}
            #     )

            # exercise 5: Lua script en Redis
            # allowed = allow_request(ip, limit=10, window=60)

            # if not allowed:
            #     return JSONResponse(
            #         status_code=429,
            #         content={"detail": "Too Many Requests"}
            #     )

            limit = 10
            window = 60

            allowed, remaining, reset = check_rate_limit(
                ip, limit, window
            )

            if not allowed:
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Too Many Requests"},
                    headers={
                        "X-RateLimit-Limit": str(limit),
                        "X-RateLimit-Remaining": "0",
                        "X-RateLimit-Reset": str(reset)
                    }
                )

            response = await call_next(request)

            response.headers["X-RateLimit-Limit"] = str(limit)
            response.headers["X-RateLimit-Remaining"] = str(remaining)
            response.headers["X-RateLimit-Reset"] = str(reset)

            return response
        
        return await call_next(request)