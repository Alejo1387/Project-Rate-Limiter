import time
from App.core.redis_client import redis_client


class RedisRateLimiter:

    def __init__(self, limit: int, window: int):
        self.limit = limit
        self.window = window

    def allow_request(self, ip: str):

        key = f"rate_limit:{ip}"

        current = redis_client.get(key)

        if current is None:
            redis_client.set(key, 1, ex=self.window)
            return True

        if int(current) >= self.limit:
            return False

        redis_client.incr(key)
        return True