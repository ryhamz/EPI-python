def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def better_parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result
