# mathjax
当前仓库的数学公式符号表达式均采用[mathjax](https://www.mathjax.org/#demo)进行撰写;  
使用chrome浏览器并搭配[mathjax extend](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima)插件, 可以直接看到渲染后的符号公式表达式.  
[latex语法学习资料](http://www.icl.utk.edu/~mgates3/docs/latex.pdf)    
[mathjax语法教程](https://www.mathelounge.de/509545/mathjax-latex-basic-tutorial-und-referenz-deutsch)
[在线编辑和渲染](https://www.mathjax.org/#demo)

&nbsp;  


# 乘方
> 一次方:       $ 2^1 $      
> 二次方(平方): $ 2^2 $    
> 三次方(立方): $ 2^3 $       

```python3
# 使用内置运算符号来表达
a = 2 ** 1                        # 2: 一次方           
b = 2 ** 2                        # 4: 二次方(平方)       
c = 2 ** 3                        # 8: 三次方(立方)        

# 使用内置函数来表达
d = pow(2, 1)                     # 2: 一次方             
e = pow(2, 2)                     # 4: 二次方(平方)       
f = pow(2, 3)                     # 8: 三次方(立方)       
```

&nbsp;  
# 单项式
> 定义: 一组数字或字母的积
>
> 李狗蛋买了n套书, 每套有m本, 每本5元, 总共花了多少钱?  
> 公式: $ 5mn $   

```python3
def danxiangshi(n: int, m: int) -> int:
    return 5*n*m
```


&nbsp;  
# 多项式
> 定义: 两组或以上的数字或字母的积相加、减
>>
> 李狗蛋买了3根铅笔(a元/根), 2本练习册(b元/本), 总共花了多少钱?  
> 公式: $ 3a + 2b $   

```python3
def duoxiangshi(a: int, b: int) -> int:
    return (3*a) + (2*b)
``` 

&nbsp;  
# 质因数(Factors)
质数(prime numbers): 一个只能被 `数字1` 和 `自己` 整除的数, 例如: 2, 3, 5, 7, 11, 13, ...;   
因数(composite numbers | 复合数): `非0` 且 `不是质数` 的数, 都是因数.

[判断一个数是否为质数(prime number)](src/factors.py#L4)   
[判断一个数是否为因数(composite number)](src/factors.py#L100)   
[列出一个数的所有质因数(短除法)](src/factors.py#L108)   
[列出一个数的所有质因数(质因数分解法)](src/factors.py#L177)

&nbsp;  
# 最小公倍数(Least common multiple)
倍数(multiple): `10 / 2 = 5` 中 10 能被 2 整除, 即: 10 可以被称为是 2 的倍数.   
公倍数: 两个数公有的倍数叫做公倍数, 以 `2` 和 `3` 举例, 找出他们的公倍数:
   
> 倍数列表去 
> 2 的倍数有: 4, 6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30   
> 3 的倍数有: 6, 9, 12, 15, 18, 21, 24, 27, 30
>  
> 2 和 3 公有的倍数有:  6, 12, 18, 24, 30  

最小公倍数: 两个数的公有倍数清单中, 最小的那个倍数被称为最小公倍数, 以上面例子来看最小的那个公倍数就是 `6`.   
[判断一个数是否为倍数](src/factors.py#L214)  
[列出一个数的倍数](src/factors.py#L234)  
[列出两个数的公倍数](src/factors.py#L329)  
[列出两个数的最小公倍数](src/factors.py#L208)   
[列出两个数的最小公倍数(TODO: )](src/factors.py#L288)   



&nbsp;  
# 最大公约数(Greatest Common Divisor)
约数(divisor | submultiple): `10 / 2 = 5` 中 10 能被 2 整除, 即: 2 可以被称为是 10 的约数.   
公约数: 两个数公有的约数叫做公约数, 以 `20` 和 `30` 举例, 找出他们的公约数:   

> 20 的约数有: 1, 2, 4, 5, 10, 20   
> 30 的约数有: 1, 2, 3, 5, 10, 15, 30   
>
> 20 和 30 公有的约数有: 1, 2, 5, 10

最大公约数: 两个数公有约数清单中, 最大的那个约数被称为最大公约数, 以上面例子来看最大的那个公约数就是 `10`.    
[判断一个数是否为约数](src/factors.py#L224)
       
[列出一个数的所有约数(短除法)](src/factors.py#L264)    
[列出两个数的公约数(短除法)](src/factors.py#L353)   
[列出两个数的最大公约数(短除法)](src/factors.py#L366)   

[列出一个数的所有约数(质因数分解法)](src/factors.py#L380)    
[列出两个数的公约数(质因数分解法)](src/factors.py#L389)      
[列出两个数的最大公约数(质因数分解法)](src/factors.py#L401)
   
[列出两个数的最大公约数(辗转相除法: 欧几里得算法)](src/gcd/euclid_algorithm/README.md)    




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
# 平方根(sqaure root)
平方根指的是: 一个数能被平方, 那么就要可以被逆平方, 这个逆运算的结果就叫做平方根.   
平方根的符号表示为: $ \sqrt{100} = 10 $
https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/


&nbsp;  
# 立方根(cube root)
平方根的符号表示为: $ \sqrt[3]{100} = 10 $




