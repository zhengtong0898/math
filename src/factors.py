import typing


def isprime(number: int) -> bool:
    """
    1. 能被2整除的数都是因数(复合数|composite number), 2除外.
    2. 剩下不能被2整除的数, 仍然有一部分因数, 例如: 21 不能被2整除, 它并不是只能 1 和 21, 它还能被3或7整除.
    3. 一个数肯定不能被大于一半的数整除, 所以: 搜寻范围是 2 ... (被验证数 // 2);
       搜索指的是: 用该范围中的每个数字对 被验证数 进行求模运算, 结果为 非0 的数就是质数.
    """

    if number < 2: return False                                                 # 小于2的都不是质数

    half: int = number // 2                                                     # 整除2
    for i in range(2, half + 1):                                                # 0 和 1 不是质因数, 所以从2开始
        if (number % i) == 0:
            break
    else:
        return True

    return False


def iscomposite(number: int) -> bool:
    """
    A natural number that is not prime.

    1. 0不是自然数: 所以0即不是质数也不是因数(复合数).
    2. 只要不是质数的都是因数(复合数)
    """
    if number == 0: return False
    return isprime(number) == False


def factors(number: int) -> typing.List[int]:
    """
    1. 一个数肯定不能被大于一半的数整除, 所以: 搜寻范围是 1 ... (被验证数 // 2);
       1是自然数并且不是质数, 那么它就是因数.
       0不是自然数, 所以范围是从1开始的.
    """
    result: typing.List[int] = []
    half: int = number // 2
    for i in range(1, half + 1):
        if number % i == 0:
            result.append(i)
    else:
        result.append(number)
    return result


def test_isprime():
    assert isprime(2) == True
    assert isprime(3) == True
    assert isprime(4) == False
    assert isprime(5) == True
    assert isprime(6) == False
    assert isprime(7) == True
    assert isprime(8) == False
    assert isprime(9) == False
    assert isprime(10) == False
    assert isprime(11) == True
    assert isprime(21) == False
    assert isprime(33) == False


def test_iscomposite():
    assert iscomposite(0) == False
    assert iscomposite(1) == True
    assert iscomposite(2) == False
    assert iscomposite(3) == False
    assert iscomposite(4) == True
    assert iscomposite(5) == False
    assert iscomposite(6) == True
    assert iscomposite(7) == False
    assert iscomposite(8) == True
    assert iscomposite(9) == True
    assert iscomposite(10) == True
    assert iscomposite(11) == False
    assert iscomposite(21) == True
    assert iscomposite(33) == True


def test_factors():
    assert factors(16) == [1, 2, 4, 8, 16]
    assert factors(20) == [1, 2, 4, 5, 10, 20]
    assert factors(45) == [1, 3, 5, 9, 15, 45]
    assert factors(75) == [1, 3, 5, 15, 25, 75]
    assert factors(73) == [1, 73]
    assert factors(77) == [1, 7, 11, 77]


def main():
    test_isprime()
    test_iscomposite()
    test_factors()


if __name__ == '__main__':
    main()
