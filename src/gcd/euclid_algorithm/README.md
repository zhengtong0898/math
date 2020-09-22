# 欧几里得算法(也被称为: 辗转相除法)
欧几里得(Euclid's Algorithm)算法用于计算一对`非负数`的最大公约数, 它是一个递归算法, 据说出现在公元前375年, 或许是最早的递归算法实例;   
- 符号表达:   
![Euclid's Algorithm](../../../assets/images/gcd_euclid_algorithm.jpg)   
- `mathjax`语法表达:  
  ```shell script
  \begin{align}
      gcd(x, y) =
      \begin{cases}
          x                    & y = 0 \\
          gcd(y, x \ mod \  y) & y > 0
      \end{cases}
  \end{align}
  ```
- 算法解释  
  gcd(x, y) 是一个函数特征定义, 这于c/c++定义函数声明含义一致;   
  该函数要求两个参数: x(被除数) 和 y(除数).  gcd算法逻辑如下:   
  ```   
  当 y = 0 时, 返回 x ;     
  当 y > 0 时, 被除数参数由 y 担任(第一个参数), 除数参数则由 x % y 得出(第二个参数).
  ```  
- 手算(过程)   
  ```shell script
  
   gcd(20, 30)  = gcd(30, 20 % 30)
                = gcd(30, 20)
                = gcd(20, 30 % 20)
                = gcd(20, 10)
                = gcd(10, 20 % 10)
                = gcd(10, 0)
                = 10

  
   gcd(114, 42) = gcd(42, 114 % 42)
                = gcd(42, 30)
                = gcd(30, 42 % 30)
                = gcd(30, 12)
                = gcd(12, 30 % 12)
                = gcd(12, 6)
                = gcd(6, 12 % 6)
                = gcd(6, 0)
                = 6

  ```
- 代码  
  [python](./gcd.py)  
  [c++](./gcd.cpp)  
- 资料参考     
  [geeksforgeeks](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/)
