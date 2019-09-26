学习笔记: 《Python编程快速上手--让繁琐工作自动化》， 英文名《Automate the boring stuff with Python》

使用编程软件: Anaconda, PyCharm/Sublime Text

# 第一部分 Python编程基础

## 第01章 Python基础
- 变量名只能包含字母、数字和下划线, 且不能以数字开头；本书的变量名采用驼峰形式，没有用下划线。类似lookLikeThis
- 注释采用 # 符号
- print() 函数, input()函数, len()函数, str(), int()和float()函数

## 第02章 控制流

- 数据类型: 整数，浮点数，字符串，布尔/Boolean
- 比较操作符: ==, !=, <, >, <=, >=
- 布尔操作符: and, or, not
- 控制流if语句: if, else, elif
- while语句: 只要while语句的条件为真就会继续执行
- break语句: break相当于中断当前循环，跳出语句。执行后面的内容。
- continue语句: 注意满足continue条件意味着回到while循环开头, 重新继续开始，而非直接继续往下（否则等于不存在或等于break）
- 死循环程序的处理: Ctrl-C  //PyCharm的快捷键是Command-F2
- for循环和range()函数: 注意range(i)=range(0, i, 1)包括的数共i个，从0到i-1，不包括i; 类似地, range(m, n, t)表示起止为m，终止为n-1，步长为t的整数计数， 例子range(5, -1, -1)
- **内建函数**与导入模块: 例子，import random, sys, os, math; random.randint(1, 10); import sys; sys.exit()提前结束程序

## 第03章 函数

- 函数的创建与调用: def语句
- 返回值和return语句
- None值，print()默认返回该值
- 关键字参数, print()函数自动在末尾添加了换行，即关键字参数end默认为换行，而关键字sep默认为一个空格，用来代表','，比如print('cats', 'dogs', 'mice')显示 cats dogs mice。

- 局部和全局作用域
- global语句