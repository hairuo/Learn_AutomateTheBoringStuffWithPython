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

## 第4章 列表

- 列表，列表值（列表本身作为一个值）/list value，表项（列表中的值）/iterms： [1, 2, 3],  ['cat', 'bat', 'rat', 'elephant'], ['hello', 3.14159, True, None, 42]
- 正负数下标， 切片/slice与子列表sublist: spam = ['cat', 'bat', 'rat', 'elephant'], spam[0:-1]==['cat', 'bat', 'rat']， btw, 发现切片不允许表项数据类型不同。
- len(spam) == 4, len('abc') == 3
- 列表连接使用+操作符(list concatenation)，删除列表中下标处的值用del语句： del spam[2]
- 对列表supplies的循环使用技巧, 使用语句for in in range(len(supplies)), str(i), supplies[i]
- in和not in操作符
- 多重赋值技巧： cat = ['fat', 'black', 'loud'], size, color, disposition = cat
- 增强的赋值操作： spam += 1, spam -=1, spam *=1, spam /= 1, spam %= 1
- 方法/methods只能在列表上调用:  index(), append(), insert()， remove(), sort(), sort默认按ASCII字符顺序排序字幕顺序需要设置关键字参数key为spam.sort(key=str.lower)
- 类似列表的类型（但不能修改、添加或删除）：字符串， 元组/tuple, tuple采用圆括号代替方括号
- 用list()和tuple函数来转换类型
- 变量包含对列表值的引用，而不是列表值本身；而对于字符串和整数值，变量包含了字符串或整数值
- 4.7.1 传递引用： eggs()被调用时，没有使用返回值来为spam赋新值，因为eggs(spam)只是相当于让someParameter指向spam的列表，但由于someParameter和spam同时指向列表，因此对列表的.append操作修改了列表的内容。这是列表和元组或字符串等一般变量的不同之处。
- copy模块的用法: copy.copy(), copy.deepcopy()