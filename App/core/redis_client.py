import redis

redis_client = redis.Redis(
    # host="localhost",
    host="redis",
    port=6379,
    db=0,
    decode_responses=True
)