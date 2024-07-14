import random

from hashlib import md5
from collections import deque
import string

from app.util import mytime

CHARS = string.digits + string.ascii_letters


def n_base(num: int, n: int) -> str:
    # 10진수 num을 k진법으로 변환 (62진수까지)
    res = deque([])

    while num:
        q = num // n
        r = num % n

        res.appendleft(CHARS[r])

        num = q

    if not res:  # 0이 입력된 경우
        return "0"

    return "".join(res)


def hash_function(data: str) -> str:
    byte_str = data.encode()
    hex_key = md5(byte_str).hexdigest()

    # 16진수 key의 뒤에서 10자리 슬라이스. 앞자리가 0인 경우에는 pad로 교체
    pad = hex_key[-10] if hex_key[-10] != "0" else CHARS[((mytime.ts_now()) % 15) + 1]
    rear_10 = pad + hex_key[-9:]

    # 62진수로 변환
    base62_key = n_base(int(rear_10, 16), 62)

    return base62_key


def make_salt() -> str:
    # 길이 5짜리 랜덤 문자열(salt) 생성
    salt = ""
    random.seed()

    for i in range(5):
        salt += CHARS[random.randint(0, 62)]

    return salt
