# mathjax
当前仓库的数学公式符号表达式均采用[mathjax](https://www.mathjax.org/#demo)进行撰写;  
使用chrome浏览器并搭配[mathjax extend](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima)插件, 可以直接看到渲染后的符号公式表达式.  
[latex语法学习资料](http://www.icl.utk.edu/~mgates3/docs/latex.pdf)    
[mathjax语法教程](https://www.mathelounge.de/509545/mathjax-latex-basic-tutorial-und-referenz-deutsch)
[在线编辑和渲染](https://www.mathjax.org/#demo)

&nbsp;  


# 乘方
- 一次方  
  $ 2^1 $
- 二次方(也被称为平方)  
  $ 2^2 $
- 三次方(也被称为立方)  
  $ 2^3 $    

```python3
# 使用内置运算符号来表达
firstPowerOfTwo = 2 ** 1                        # 一次方
secondPowerOfTwo = 2 ** 2                       # 二次方(平方)
thirdPowerOfTwo = 2 ** 3                        # 三次方(立方)

print("firstPowerOfTwo:  ", firstPowerOfTwo)    # 2
print("secondPowerOfTwo: ", secondPowerOfTwo)   # 4
print("thirdPowerOfTwo:  ", thirdPowerOfTwo)    # 8


# 使用内置函数来表达
firstPowerOfTwo = pow(2, 1)                     # 一次方
secondPowerOfTwo = pow(2, 2)                    # 二次方(平方)
thirdPowerOfTwo = pow(2, 3)                     # 三次方(立方)

print("firstPowerOfTwo:  ", firstPowerOfTwo)    # 2
print("secondPowerOfTwo: ", secondPowerOfTwo)   # 4
print("thirdPowerOfTwo:  ", thirdPowerOfTwo)    # 8
```

&nbsp;  
# 单项式
> 李狗蛋买了n套书, 每套有m本, 每本5元, 总共花了多少钱?  
> 公式: $ 5mn $   
> 定义: 数字或字母的积

```python3
# 由于公式中带有未知数, 因此只能使用函数来解决.
def ligoudanDanxiangshi(n: int, m: int) -> int:
    return 5*n*m
```


&nbsp;  
# 多项式
> 李狗蛋买了3根铅笔(a元/根), 2本练习册(b元/本), 总共花了多少钱?  
> 公式: $ 3a + 2b $   
> 定义: 两组或以上的数字或字母的积相加、减

```python3
def ligoudanDuoxiangshi(a: int, b: int) -> int:
    return (3*a) + (2*b)
``` 

&nbsp;  
# 质因数(Factors)
质数(prime numbers): 一个只能被 `数字1` 和 `自己` 整除的数, 例如: 2, 3, 5, 7, 11, 13, ...;   
因数(composite numbers | 复合数): 除了能被 `数字1` 和 `自己` 之外 还能被其他数(通常指的是: 2-9)整除的数, 例如: 4, 6, 8, 9, 10, 12;       
注意事项: 0和1既不是质数也不是因数.  

[判断一个数是否为质数(prime number)](src/factors.py#L4)   
[判断一个数是否为因数(composite number)](src/factors.py#L26)   
[列出一个数的所有质因数(factors)](src/factors.py#L37)   
[质因数分解法(factorization)](src/factors.py#L61)


&nbsp;  
# 短除法
https://www.youtube.com/watch?v=hPpZ7C5rh9E



&nbsp;  
# 丢番图的年龄
公式: $ x = {1\over6}x + {1\over12}x + {1\over7}x + 5 + {1\over2}x + 4  $   
解题思路: 采用最小公倍数去分母, 6,12,7,2 的最小公倍数是 84.  
```
                                                # 去分母操作
      x * 84            = 84x                   # 等式左边 乘以 最小公倍数.
 (1/6)x * 84 =  (84/6)x = 14x                   # 等式右边 每项也都乘以 最小公倍数.
(1/12)x * 84 = (84/12)x = 7x   
 (1/7)x * 84 =  (84/7)x = 12x
      5 * 84            = 420      
 (1/2)x * 84 =  (84/2)x = 42x     
      4 * 84            = 336  

   84x = 14x + 7x + 12x + 420 + 42x + 336       # 合并同类项
   84x = 75x + 756                              # 合并同类项
84-75x = 756                                    # 合并同类项
    9x = 756                                    
9x / 9 = 756 / 9                                # 系数化一 
     x = 84   
```

&nbsp;  
# 最小公倍数


&nbsp;  
# 最大公约数(Greatest Common Divisor)



&nbsp;  
# 平方根(sqaure root)
平方根指的是: 一个数能被平方, 那么就要可以被逆平方, 这个逆运算的结果就叫做平方根.   
平方根的符号表示为: $ \sqrt{100} = 10 $
https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/


&nbsp;  
# 立方根(cube root)
平方根的符号表示为: $ \sqrt[3]{100} = 10 $




