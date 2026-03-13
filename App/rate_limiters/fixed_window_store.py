from App.rate_limiters.fixed_window import FixedWindowRateLimiter

rate_limiter = FixedWindowRateLimiter(
    limit=10,
    window_size=60
)