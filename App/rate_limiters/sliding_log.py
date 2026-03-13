import time


class SlidingWindowLogRateLimiter:

    def __init__(self, limit: int, window_size: int):
        self.limit = limit
        self.window_size = window_size
        self.storage = {}

    def allow_request(self, ip: str) -> bool:

        now = time.time()

        if ip not in self.storage:
            self.storage[ip] = []

        timestamps = self.storage[ip]

        # 1 eliminar timestamps viejos
        self.storage[ip] = [
            ts for ts in timestamps
            if ts > now - self.window_size
        ]

        timestamps = self.storage[ip]

        # 2 verificar limite
        if len(timestamps) >= self.limit:
            return False

        # 3 agregar nuevo timestamp
        timestamps.append(now)

        return True