import time


class FixedWindowRateLimiter:

    def __init__(self, limit: int, window_size: int):
        self.limit = limit
        self.window_size = window_size
        self.storage = {}

    def allow_request(self, ip: str) -> bool:

        now = int(time.time())

        if ip not in self.storage:
            self.storage[ip] = {
                "window_start": now,
                "count": 0
            }

        window = self.storage[ip]

        # verificar si la ventana expiró
        if now - window["window_start"] >= self.window_size:

            window["window_start"] = now
            window["count"] = 0

        # incrementar contador
        window["count"] += 1

        # verificar limite
        if window["count"] > self.limit:
            return False

        return True