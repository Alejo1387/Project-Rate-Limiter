import time

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: int):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        elapsed = now - self.last_refill

        refill_tokens = int(elapsed * self.refill_rate)

        if refill_tokens > 0:
            self.tokens = min(self.capacity, self.tokens + refill_tokens)
            self.last_refill = now

        if self.tokens > 0:
            self.tokens -= 1
            return True

        return False