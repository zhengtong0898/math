

def gcd(x: int, y: int) -> int:
    if y <= 0: return x
    divisor: int = x % y
    return gcd(y, divisor)


def main():
    assert gcd(20, 30) == 10, "error: gcd(20, 30) == 10"
    assert gcd(112, 42) == 14, "error: gcd(112, 42) == 14"


if __name__ == '__main__':
    main()
