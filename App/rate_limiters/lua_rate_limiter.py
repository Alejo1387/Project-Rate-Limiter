from App.core.redis_client import redis_client
import time

RATE_LIMIT_SCRIPT = """
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])

local current = redis.call("GET", key)

if current and tonumber(current) >= limit then
    return {0, current}
end

current = redis.call("INCR", key)

if current == 1 then
    redis.call("EXPIRE", key, window)
end

return {1, current}
"""

rate_limiter_script = redis_client.register_script(RATE_LIMIT_SCRIPT)


def check_rate_limit(ip: str, limit: int, window: int):

    key = f"rate_limit:{ip}"

    result = rate_limiter_script(
        keys=[key],
        args=[limit, window]
    )

    allowed = result[0] == 1
    current = int(result[1])

    remaining = max(0, limit - current)

    reset = int(time.time()) + window

    return allowed, remaining, reset