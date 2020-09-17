# 乘方
- 一次方  
  $ 2^1 $
- 二次方(也被称为平方)  
  $ 2^2 $
- 三次方(也被称为立方)  
  $ 2^3 $    

用python表达乘方
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

python表达单项式
```python3
# 由于公式中带有未知数, 因此只能使用函数来解决.
def ligoudanDanxiangshi(n, m):
    return 5*n*m
```


&nbsp;  
# 多项式
> 李狗蛋买了3根铅笔(a元/根), 2本练习册(b元/本), 总共花了多少钱?  
> 公式: $ 3a + 2b $   

python表达多项式
```python3
def ligoudanDuoxiangshi(a, b):
    return (3*a) + (2*b)
``` 

&nbsp;  
# 丢番图的年龄
> 公式: $ x = {1\over6}x + {1\over12}x + {1\over7}x + 5 + {1\over2}x + 4  $
>
> 解题思路: 采用最小公倍数去分母, 6,12,7,2 的最小公倍数是 84.  
>       x * 84            = 84x   
>  (1/6)x * 84 =  (84/6)x = 14x   
> (1/12)x * 84 = (84/12)x = 7x   
>  (1/7)x * 84 =  (84/7)x = 12x
>       5 * 84            = 420      
>  (1/2)x * 84 =  (84/2)x = 42x     
>       4 * 84            = 336  
>
>    84x = 14x + 7x + 12x + 420 + 42x + 336   
>    84x = 75x + 756   
> 84-75x = 756   
>     9x = 756    
>      x = 756 / 9   
>      x = 84   
 
python表达解方程
```python3
def diufantu(x):
    return x/6 + x/12 + x/7 + 5 + x/2 + 4

print(diufantu(84))   # 结果(84); 只要返回结果于传入参数一样, 那么就能得出丢番图的年龄.
```