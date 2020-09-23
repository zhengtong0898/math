import typing


def isprime(number: int) -> bool:
    """
    判断一个数是否为质数

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
    判断一个数是否为因数(composite number|复合数)

    A natural number that is not prime.
    1 is not Prime and also not Composite.
    """
    if number < 2: return False
    return isprime(number) == False


def factors(number: int) -> typing.List[int]:
    """
    列出 number 的所有质因数

    TODO: 这里有说: 1 is not Prime and also not Composite.
    https://www.mathsisfun.com/prime-composite-number.html

    TODO: 数字1 如果不是质因数, 那为什么要列出来?  :  16 --> 1, 2, 4, 8, 16
    http://www.math.com/school/subject1/lessons/S1U3L1DP.html

    为什么要定义half变量?
    大于 number 一半的数字(除了 number 自己之外),
    一定不是 number 的质因数, 这样写能减少匹配范围.
    """
    result: typing.List[int] = []
    half: int = number // 2
    for i in range(1, half + 1):
        if number % i == 0:
            result.append(i)
    else:
        result.append(number)
    return result


def factorization(number: int) -> typing.List[int]:

    """
    质因数分解法

    质因数分解的本质原理是用两个数相乘得出的结果等于被求数, 例如:
    12 = 3 * 4;      这种分解通过心算(小时候背过的乘法口诀)能得出这个表达式, 但是表达式还能被进一步再分解, 因为4不是质数.
    12 = 2 * 2 * 3;  这样才是正确的质因数分解表达式， 因为右侧表达式中每个项都是质数.

    程序没有心算能力, 所以只能按照一些特定原则和范围来进行推到:
    1. 从 i = 2 开始:        是因为 0 和 1 不是质数(结果集必须是质数), i是要被放入到结果集中的数.
    2. (i * i) <= number:    两个数相乘 等于 被求数 是一个有效的分解, 如果两个数都是质数, 就不能再进一步推到, 反之.
                             两个数相乘 小于 被求数 是一个无效的分解, 但是还可以被进一步推到.
                             两个数相乘 大于 被求数 是一个无效的分解, 不可以继续推到, 跳出循环.
    3. (number % i) == 0:    能被i求模, 就意味着i是一个有效的质数.
                             这里解释一下为什么i能被求模就一定是质数, 因为整个算法是从小到大去求模,
                             所以能被2求模掉的数, 后续就不会再出现能被4求模的数了, 也不会再出现能被6求模的数了, 以此类推.

    4. result.append(i):     由于推到是从最小的有效质数2开始, 所以不需要再次确认i还不能能再被拆分.
    5. number //= i:         是为了能够继续分解剩下的数字, 例如:
                             20 = 2 * 10
                             10 = 20 // 2
                             5  =  10 // 2
                             2  = 5 // 2            -->   (2 * 2) <= 2 不成立, 退出程序.
    """

    i = 2
    result: typing.List[int] = []

    while (i * i) <= number:
        if (number % i) == 0:
            number //= i
            result.append(i)
        else:
            i += 1

    if number >= 2:
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
    assert [i for i in range(101) if isprime(i)] == [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


def test_iscomposite():
    assert iscomposite(0) == False
    assert iscomposite(1) == False
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
    assert [i for i in range(21) if iscomposite(i)] == [4,6,8,9,10,12,14,15,16,18,20]


def test_factors():
    assert factors(16) == [1, 2, 4, 8, 16]
    assert factors(20) == [1, 2, 4, 5, 10, 20]
    assert factors(45) == [1, 3, 5, 9, 15, 45]
    assert factors(75) == [1, 3, 5, 15, 25, 75]
    assert factors(73) == [1, 73]
    assert factors(77) == [1, 7, 11, 77]


def test_factorization():
    assert factorization(4) == [2,2]
    assert factorization(6) == [2,3]
    assert factorization(8) == [2,2,2]
    assert factorization(9) == [3,3]
    assert factorization(10) == [2,5]
    assert factorization(12) == [2,2,3]
    assert factorization(14) == [2,7]
    assert factorization(15) == [3,5]
    assert factorization(16) == [2,2,2,2]
    assert factorization(18) == [2,3,3]
    assert factorization(20) == [2,2,5]
    assert factorization(330) == [2,3,5,11]
    assert factorization(600851475143) == [71, 839, 1471, 6857]


def main():
    test_isprime()
    test_iscomposite()
    test_factors()
    test_factorization()


if __name__ == '__main__':
    main()


# 参考:
# http://www.math.com/school/subject1/lessons/S1U3L1GL.html
# https://www.youtube.com/watch?v=fdUXGZogSxE
# https://www.mathsisfun.com/prime-factorization.html
# https://www.mathsisfun.com/prime-composite-number.html
