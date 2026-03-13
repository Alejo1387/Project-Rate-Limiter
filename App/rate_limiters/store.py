from .token_bucket import TokenBucket

buckets = {}

def get_bucket(ip: str):
    if ip not in buckets:
        buckets[ip] = TokenBucket(capacity=10, refill_rate=1)

    return buckets[ip]