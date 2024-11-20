


def to_kv(k: str, v: int or float) -> tuple:
    tup = k,float(v*v)
    return tuple(tup)

print(to_kv("cool",5.0))