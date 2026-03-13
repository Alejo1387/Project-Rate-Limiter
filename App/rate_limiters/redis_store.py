from App.rate_limiters.redis_rate_limiter import RedisRateLimiter

rate_limiter = RedisRateLimiter(
    limit=10,
    window=60
)