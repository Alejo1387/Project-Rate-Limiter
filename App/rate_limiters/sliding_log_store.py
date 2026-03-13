from App.rate_limiters.sliding_log import SlidingWindowLogRateLimiter

rate_limiter = SlidingWindowLogRateLimiter(
    limit=10,
    window_size=60
)