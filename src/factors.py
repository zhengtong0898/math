import typing


def isprime(number: int) -> bool:
    """
    判断一个数是否为质数, 时间复杂度O(logn).

    参考:
    How to Find Prime Numbers?
    https://byjus.com/maths/prime-numbers/
    """
    if number in (2, 3, 5, 7, 11): return True
    if number < 2: return False
    if number % 2 == 0: return False
    if number % 3 == 0: return False
    if number % 5 == 0: return False
    if number % 7 == 0: return False
    if number % 11 == 0: return False

    i = 6
    square_root = int(number ** 0.5)
    while i < square_root:
        if number % (i-1) == 0: return False
        if number % (i+1) == 0: return False
        i += 6
    return True


def isprime1(number: int) -> bool:
    """
    判断一个数是否为质数(对半迭代求模法), 时间复杂度O(logn)

    如何判断一个数是否能被2整除?
    通常是采用 %(求模) 来判断, 例如: 16 % 2 == 0; 表示 16可以被2整除.

    如果不能被2整除, 那怎么办?
    那就尝试用3去求模判断是否能被3整除, 以此类推往下迭代.
    """
    if number < 2: return False                                 # 小于2的都不是质数.
    if number in (2, 3): return True                            # 2, 3 是质数
    if number % 2 == 0: return False                            # 能被2整除的都不是质数.
    if number % 3 == 0: return False                            # 能被3整除的都不是质数.

    square_root = int(number ** 0.5)                            # 对数操作: 通过平方根运算, 锁定对数范围.
    for i in range(5, square_root+1):
        if (number % i) == 0: return False                      # number 能被 i 整除, 所以 number 不是质数.
    return True


def isprime2(number: int) -> bool:
    """
    判断一个数是否为质数(对半迭代求模法), 时间复杂度O(logn), 性能是 isprime, isprime2 的3倍.

    参考:
    isPrime Function for Python Language?
    https://stackoverflow.com/a/15285588/12353483
    """
    if number < 2: return False
    if number in (2, 3): return True
    if number % 2 == 0: return False
    if number % 3 == 0: return False
    if number < 9: return True

    i = 5
    square_root = int(number ** 0.5)
    while i <= square_root:
        if number % i == 0: return False                        # 6(i) + 5 一定不会被2整除
        if number % (i+2) == 0: return False                    #
        i += 6                                                  # 步长: 6

    return True


def isprime3(number: int) -> bool:
    if number < 2: return False
    if number in (2, 3): return True
    if number % 2 == 0: return False
    if number % 3 == 0: return False

    i = 5                                                       # 0,1不是质因数, 2,3是质数, 4可以被2整除, 所以从5开始.
    while (i * i) < number:                                     # 对数操作: 平方运算, 锁定对数范围
        if (number % i) == 0: return False                      # number 能被 i 整除, 所以 number 不是质数.
        i += 1

    if (i * i) == number: return False
    return True                                                 # 质数/素数: prime number.


def isprime4(number: int) -> bool:
    """
    判断一个数是否为质数(对半迭代求模法), 时间复杂度O(n)
    """
    if number < 2: return False                                # 小于2的都不是质数.

    half: int = number // 2
    for i in range(2, half + 1):                               # i 的范围是: 2 -- half
        if (number % i) == 0:
            break                                              # number 能被 i 整除, 所以 number 不是质数.
    else:
        return True                                            # 质数/素数: prime number.
    return False


def iscomposite(number: int) -> bool:
    """
    判断一个数是否为因数(composite number|复合数)
    """
    if number < 2: return False                                # 负数, 0, 1 都不是质因数.
    return isprime(number) == False


def factors(number: int) -> typing.List[int]:
    """
    列出 number 的所有质因数, 时间复杂度O(logn)

    例如:
    10 = [1, 2, 5, 10]
    16 = [1, 2, 4, 8, 16]

    算法(以10为例):
    1 x 10 = 10         # [1, 10]
    2 x  5 = 10         # [1, 10, 2, 5]
                        # [1, 2, 5, 10]         排序后

    算法(以16为例):
    1 x 16 = 16         # [1, 16]
    2 x  8 = 16         # [1, 16, 2, 8]
    4 x  4 = 16         # [1, 16, 2, 8, 4]
                        # [1, 2, 3, 8, 16]      排序后

    根据定义声明, 一个数能被另外一个数整除, 那么它一定不是质数, 所以写代码也要围绕这个概念来写.
    1. 框定一个范围: 采用 (i * i) 或者 sqaure_root 方式.
    2. 遍历该范围的每个数, 对被求数进行挨个求模.
    """
    i = 2
    if number < i: return []

    result: typing.List[int] = [1, ]                           # 头加1
    while (i * i) < number:
        if (number % i) == 0:
            result.append(i)                                   # number 能被 i 整除, 所以 i 是 number 的质因数(factors).
        else:
            i += i
    else:
        result.append(number)                                  # 尾加自己

    return result


def factors2(number: int) -> typing.List[int]:
    """
    列出 number 的所有质因数, 时间复杂度O(n)
    """
    result: typing.List[int] = [1, ]
    if number <= 0: return []
    if number == 1: return result

    half: int = number // 2
    for i in range(2, half + 1):
        if (number % i) == 0:
            result.append(i)
    else:
        result.append(number)
    return result


def factorization(number: int) -> typing.List[int]:

    """
    列出一个数的质数(分解)集合.

    例如:
    10 = 2 x 5;
    12 = 2 x 2 x 3;
    15 = 3 x 5;
    16 = 2 x 2 x 2 x 2;

    算法(以16举例):
    16 / 2 = 8;         # [2, ]            16可以被2整除, 把2纳入结果集
     8 / 2 = 4;         # [2, 2]           8可以被2整除, 把2纳入结果集
     4 / 2 = 2;         # [2, 2, 2]        4可以被2整除, 把2纳入结果集
                        # [2, 2, 2, 2]     最后剩下2是一个质数, 不能再继续被整除, 所以也把这个数字纳入结果集.
    算法(以168为例):
    168 / 2 = 84;       # [2, ]            168可以被2整除, 把2纳入结果集
     84 / 2 = 42;       # [2, 2]           84可以被2整除, 把2纳入结果集
     42 / 2 = 21;       # [2, 2, 2]        42可以被2整除, 把2纳入结果集
     21 / 3 = 7;        # [2, 2, 2, 3]     21可以被3整除, 把2纳入结果集
                        # [2, 2, 2, 3, 7]  最后剩下7是一个质数, 不能再继续被整除, 所以也把这个数字纳入结果集.

    TODO: 考虑移除下面这些说明.
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

    # 这里采取的是质因数分解法的 两数相乘 比较法,
    # 然后while内部块则负责判断两个数是否都为质数,
    # 如果都为质数那么就结束, 否则将会持续处理分叉数.
    while (i * i) <= number:
        if (number % i) == 0:
            print("number: ", number)
            number //= i
            result.append(i)
        else:
            i += 1

    if number >= 2:
        result.append(number)

    return result


def ismultiple(multiple: int, number: int) -> bool:
    """
    判断一个数是否为倍数

    :param number: 被求数
    :param multiple: 倍数
    """
    return (multiple % number) == 0


def multiples(number: int, limit: int = 10) -> typing.Iterator[int]:
    """
    列出一个数的倍数

    :param number: 被求数
    :param limit:   查找倍数的范围
    """

    # 方式一:
    # 使用这种方式写代码的好处是, 复杂场景的筛选条件可以交给外部来定夺.
    # 例如: test_common_multiple的测试场景, 要筛选某些数而不是特定范围.
    count = 1
    result = []
    while True:
        if limit and len(result) >= limit: break
        multiple = number * count                           # 两数相乘(用于匹配)被称为质因数分解法套路
        if ismultiple(multiple, number):                    # 备注: 这个函数跟factorization有什么区别?
            result.append(multiple)                         # 两者都是用质因数分解法的套路, 唯一的区别是
            yield multiple                                  # factorization是求约数, 而当前函数求得是倍数.
        count += 1

    # 方式二:
    # 使用这种写法比较简单, 运行效率也会相对更高, 但是不够灵活(指的是 limit 强行限制的范围).
    # return [number * i for i in range(2, limit+2)]


def commom_base(lhs_iter: typing.Iterator,
                rhs_iter: typing.Iterator,
                limit: int = 10) -> typing.List[int]:
    """
    采集两个迭代器的公有数据

    :param lhs_iter: 生产数a集合的迭代器
    :param rhs_iter: 生产数b集合的迭代器
    :param limit: 取交集(intersection)的limit数量的列表

    备注:
    common_base的limit: 筛选满足公有倍数的个数
      multiples的limit: 筛选满足倍数的个数
       divisors的limit: 筛选满足约数的个数
    """
    status = True
    sep = limit * 2
    result = set()
    lrs, rrs = set(), set()
    while True:

        # 按照 sep 批次获取 iter 的值
        count = 0
        while count < sep:
            try:
                lrs.add(next(lhs_iter))
            except StopIteration:
                status = False

            try:
                rrs.add(next(rhs_iter))
            except StopIteration:
                status = False

            count += 1

        [result.add(i) for i in lrs.intersection(rrs)]
        if len(result) > limit: break
        if status is False: break
    return sorted(list(result))[0:limit]

    # 方式二:
    # 这个代码有严重的性能问题, 没迭代一次循环, multiple的方式二都会从0开始迭代数值, 成几何倍数的方式在增长.
    # offset = 10
    # result = set()
    # while True:
    #     lr = set(multiples(lhs, limit=offset))
    #     rr = set(multiples(rhs, limit=offset))
    #     [result.add(i) for i in list(lr.intersection(rr))]
    #     if len(result) >= limit: break
    #     offset += offset
    # return sorted(list(result))[0:limit]


def commom_multiple(lhs: int, rhs: int, limit: int = 10) -> typing.List[int]:
    """
    列出两个数的公倍数

    :param lhs: 数a
    :param rhs: 数b
    :param limit: 查找两个数的公倍数范围
    """
    lhs_iter = multiples(lhs, limit=0)
    rhs_iter = multiples(rhs, limit=0)
    return commom_base(lhs_iter, rhs_iter, limit)


def least_common_multiple(lhs: int, rhs: int, limit: int = 10) -> int:
    """
    列出两个数的最小公倍数

    :param lhs: 数a
    :param rhs: 数b
    :param limit: 查找两个数的公倍数范围
    """
    return commom_multiple(lhs, rhs, limit)[0]


def isdivisor(number: int, divisor: int) -> bool:
    """
    判断一个数是否为约数

    :param number: 被求数
    :param divisor: 约数
    """
    return (number % divisor) == 0


def divisors(number: int) -> typing.List[int]:
    """
    列出一个数的所有约数

    :param number: 被求数
    """
    return factors(number)


def common_divisor(lhs: int, rhs: int) -> typing.List[int]:
    """
    列出两个数的公约数

    :param lhs:
    :param rhs:
    :return:
    """
    lhs_list = divisors(lhs)
    rhs_list = divisors(rhs)
    return commom_base(iter(lhs_list), iter(rhs_list))


def greatest_common_divisor(lhs: int, rhs: int) -> int:
    """
    列出两个数的最大公约数(短除法)

    :param lhs:
    :param rhs:
    :param stop:
    :return:
    """
    cd = common_divisor(lhs, rhs)
    gcd = cd[-1] if len(cd) > 0 else 1
    return gcd


def divisor_factorization(number: int) -> typing.List[int]:
    """
    列出一个数的所有约数(质因数分解法)

    :param number: 被求数
    """
    return factorization(number)


def common_divisor_factorization(lhs: int, rhs: int) -> typing.List[int]:
    """
    列出两个数的公约数(质因数分解法)
    :param lhs:
    :param rhs:
    :return:
    """
    lhs_list = divisor_factorization(lhs)
    rhs_list = divisor_factorization(rhs)
    return commom_base(iter(lhs_list), iter(rhs_list))


def greatest_common_divisor_factorization(lhs: int, rhs: int) -> int:
    """
    列出两个数的最大公约数(质因数分解法)
    :param lhs:
    :param rhs:
    :return:
    """
    cd = common_divisor_factorization(lhs, rhs)
    gcd = cd[-1] if len(cd) > 0 else 1
    return gcd


def test_isprime():
    """
    测试: 验证一个数是否为质数/素数(prime)
    """
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
    """
    测试: 验证一个数是否为因数/复合数(composite)
    """
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
    """
    测试: 验证根据一个数列出该数的所有质因数
    """
    assert factors(16) == [1, 2, 4, 8, 16]
    assert factors(20) == [1, 2, 4, 5, 10, 20]
    assert factors(45) == [1, 3, 5, 9, 15, 45]
    assert factors(75) == [1, 3, 5, 15, 25, 75]
    assert factors(73) == [1, 73]
    assert factors(77) == [1, 7, 11, 77]


def test_factorization():
    """
    测试: 验证根据一个数列出该数的质因数分解结果集
    """
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


def test_multiple():
    """
    测试: 验证 multiple数 是否为 number数 的倍数.
    """
    assert ismultiple(10, 1) == True
    assert ismultiple(10, 2) == True
    assert ismultiple(10, 3) == False
    assert ismultiple(10, 4) == False
    assert ismultiple(10, 5) == True
    assert ismultiple(10, 10) == True

    assert ismultiple(20, 1) == True
    assert ismultiple(20, 2) == True
    assert ismultiple(20, 3) == False
    assert ismultiple(20, 4) == True
    assert ismultiple(20, 5) == True
    assert ismultiple(20, 10) == True


def test_multiples():
    """
    测试: 验证根据一个数列出该数的倍数
    """
    assert list(multiples(2, limit=5)) == [2, 4, 6, 8, 10]
    assert list(multiples(3, limit=5)) == [3, 6, 9, 12, 15]
    assert list(multiples(7, limit=5)) == [7, 14, 21, 28, 35]
    assert list(multiples(10, limit=5)) == [10, 20, 30, 40, 50]


def test_common_multiple():
    """
    测试: 验证根据两个数列出这两个数的公共倍数.
    """
    assert commom_multiple(2, 3, 5) == [6, 12, 18, 24, 30]
    assert commom_multiple(2, 3, 6) == [6, 12, 18, 24, 30, 36]
    assert commom_multiple(6, 7, 5) == [42, 84, 126, 168, 210]


def test_least_common_multiple():
    """
    测试: 验证根据两个数列出这两个数的最小公倍数.
    """
    assert least_common_multiple(2, 3) == 6
    assert least_common_multiple(6, 7) == 42
    assert least_common_multiple(4, 6) == 12
    assert least_common_multiple(2, 4) == 4
    assert least_common_multiple(12, 80) == 240
    assert least_common_multiple(50, 65) == 650


def test_divisor():
    """
    测试: 验证根据一个数列出该数的约数(除数)
    """
    assert isdivisor(10, 1) == True
    assert isdivisor(10, 2) == True
    assert isdivisor(10, 3) == False
    assert isdivisor(10, 4) == False
    assert isdivisor(10, 5) == True
    assert isdivisor(10, 10) == True

    assert isdivisor(21, 1) == True
    assert isdivisor(21, 2) == False
    assert isdivisor(21, 3) == True
    assert isdivisor(21, 4) == False
    assert isdivisor(21, 5) == False
    assert isdivisor(21, 6) == False
    assert isdivisor(21, 7) == True
    assert isdivisor(21, 8) == False
    assert isdivisor(21, 9) == False
    assert isdivisor(21, 10) == False
    assert isdivisor(21, 11) == False


def test_common_divisor():
    """
    测试: 验证根据两个数列出这两个数的公共约数(除数).
    """
    assert common_divisor(15, 20) == [5]
    assert common_divisor(2, 3) == []
    assert common_divisor(2, 4) == [2]
    assert common_divisor(3, 6) == [3]
    assert common_divisor(6, 21) == [3]
    assert common_divisor(6, 6) == [2, 3, 6]


def test_greatest_common_divisor():
    """
    测试: 验证根据两个数列出这两个数的最大公约数(除数|短除法).
    """
    assert greatest_common_divisor(15, 20) == 5
    assert greatest_common_divisor(2, 3) == 1
    assert greatest_common_divisor(2, 4) == 2
    assert greatest_common_divisor(3, 6) == 3
    assert greatest_common_divisor(6, 21) == 3
    assert greatest_common_divisor(6, 6) == 6


def test_greatest_common_divisor_factorization():
    """
    测试: 验证根据两个数列出这两个数的最大公约数(除数|质因数分解法)

    声明:
    这里为什么会跟上面的test_greatest_common_divisor不一样.
    greatest_common_divisor 采用的是 factors, 结果集是质数: 1
    """
    assert greatest_common_divisor_factorization(15, 20) == 5
    assert greatest_common_divisor_factorization(2, 3) == 1
    assert greatest_common_divisor_factorization(2, 4) == 2
    assert greatest_common_divisor_factorization(3, 6) == 3
    assert greatest_common_divisor_factorization(6, 21) == 3
    assert greatest_common_divisor_factorization(6, 6) == 3


def main():
    # print([i for i in range(101) if isprime(i)])
    print(isprime(5003))
    # test_isprime()
    # test_iscomposite()
    # test_factors()
    # test_factorization()
    #
    # test_multiple()
    # test_multiples()
    # test_common_multiple()
    # test_least_common_multiple()
    #
    # test_divisor()
    # test_common_divisor()
    # test_greatest_common_divisor()
    # test_greatest_common_divisor_factorization()


if __name__ == '__main__':
    main()


# 参考:
# http://www.math.com/school/subject1/lessons/S1U3L1GL.html
# https://www.youtube.com/watch?v=fdUXGZogSxE
# https://www.mathsisfun.com/prime-factorization.html
# https://www.mathsisfun.com/prime-composite-number.html
