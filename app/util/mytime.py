import time

MIN_SEC = 60
HOUR_SEC = 3600
DAY_SEC = 86400


def ts_now() -> int:
    return int(time.time())


def ts_after(ts: int, hour: int) -> int:
    return ts + (HOUR_SEC * hour)
