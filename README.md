学习笔记: 《Python编程快速上手--让繁琐工作自动化》， 英文名《Automate the boring stuff with Python》[英文原版在线免费阅读](https://automatetheboringstuff.com/)

使用编程软件: [Anaconda](https://www.anaconda.com/distribution/)+[PyCharm CE](https://www.jetbrains.com/pycharm/download/), 备选: [Sublime Text](https://www.sublimetext.com/)

# 第一部分 Python编程基础

## 第01章 Python基础
- 变量名只能包含字母、数字和下划线, 且不能以数字开头；本书的变量名采用驼峰形式，没有用下划线。类似lookLikeThis
- 注释采用 # 符号
- `print() `函数, `input()`函数, `len()`函数, `str()`, `int()`和`float()`函数

## 第02章 控制流

- 数据类型: 整数，浮点数，字符串，布尔/Boolean
- 比较操作符:``` ==, !=, <, >, <=, >=```
- 布尔操作符: ```and, or, not```
- 控制流if语句: ```if, else, elif```
- `while`语句: 只要`while`语句的条件为真就会继续执行
- `break`语句: `break`相当于中断当前循环，跳出语句。执行后面的内容。
- `continue`语句: 注意满足`continue`条件意味着回到`while`循环开头, 重新继续开始，而非直接继续往下（否则等于不存在或等于`break`）
- 死循环程序的处理: Ctrl-C  //PyCharm的快捷键是Command-F2
- `for`循环和`range()`函数: 注意`range(i)=range(0, i, 1)`包括的数共i个，从0到i-1，不包括i; 类似地, `range(m, n, t)`表示起止为m，终止为n-1，步长为t的整数计数， 例子`range(5, -1, -1)`
- **内建函数**与导入模块: 例子，```import random, sys, os, math; random.randint(1, 10)```; ```import sys; sys.exit()```提前结束程序

## 第03章 函数

- 函数的创建与调用: def语句
- 返回值和`return`语句
- None值，`print()`默认返回该值
- 关键字参数, `print()`函数自动在末尾添加了换行，即关键字参数end默认为换行，而关键字sep默认为一个空格，用来代表','，比如`print('cats', 'dogs', 'mice')`显示 cats dogs mice。

- 局部和全局作用域
- global语句

## 第04章 列表

- 列表，列表值（列表本身作为一个值）/list value，表项（列表中的值）/iterms：` [1, 2, 3]`,  `['cat', 'bat', 'rat', 'elephant']`, `['hello', 3.14159, True, None, 42]`
- 正负数下标， 切片/slice与子列表sublist: `spam = ['cat', 'bat', 'rat', 'elephant']`, `spam[0:-1]==['cat', 'bat', 'rat']`， btw, 发现切片不允许表项数据类型不同。
- `len(spam) == 4`, `len('abc') == 3`
- 列表连接使用+操作符(list concatenation)，删除列表中下标处的值用del语句： `del spam[2]`
- 对列表supplies的循环使用技巧, 使用语句`for in in range(len(supplies))`, `str(i)`, `supplies[i]`
- `in`和`not in`操作符
- 多重赋值技巧： `cat = ['fat', 'black', 'loud']`, `size, color, disposition = cat`
- 增强的赋值操作： `spam += 1`, `spam -=1`, `spam *=1`, `spam /= 1`, `spam %= 1`
- 方法/methods只能在列表上调用:  `index()`,` append()`,` insert()`， `remove()`,` sort()`, sort默认按ASCII字符顺序排序字幕顺序需要设置关键字参数key为`spam.sort(key=str.lower)`
- 类似列表的类型（但不能修改、添加或删除）：字符串， 元组/tuple, tuple采用圆括号代替方括号
- 用`list()`和`tuple`函数来转换类型
- 变量包含对列表值的引用，而不是列表值本身；而对于字符串和整数值，变量包含了字符串或整数值
- 4.7.1 传递引用： `eggs()`被调用时，没有使用返回值来为spam赋新值，因为`eggs(spam)`只是相当于让someParameter指向spam的列表，但由于someParameter和spam同时指向列表，因此对列表的`.append`操作修改了列表的内容。这是列表和元组或字符串等一般变量的不同之处。
- copy模块的用法: `copy.copy()`, `copy.deepcopy()`

## 第05章 字典和结构化数据

- 字典数据类型：键-值

- 字典(example: spam)与列表：
  
  ```python
  if color in spam.keys():
  if color in spam.values():
  if color in spam: // means spam.keys()
  list(spam.keys())
  ```
  
- keys(), values(), iterms()
  
  ```python
  for v in spam.values():
  for k in spam.keys():
  for i in spam.items():
  
  ```
  
- `get()`方法有两个参数, 第一个是要**取值**的键，第二个是如果该键不存在时，**返回**的备用值: `str(spam.get('xxx', 0))`，不使用`get()`而字典没有相应的键时，程序运行会产生错误消息。

- `setdefaut()`方法有两个参数，第一个是要检查的键，第二个是如果该键不存在时要**设置**的值: `spam.setdefault('color', 'black')`，可以确保一个键存在的快捷方式。//`get()`和`setdefault()`的区别参见[这里](https://stackoverflow.com/questions/7423428/python-dict-get-vs-setdefault)。

- 漂亮打印pprint模块：`pprint.pprint()`, `pprint.pformat()`

- 使用[**数据结构**](https://zhuanlan.zhihu.com/p/23191006)对真实世界建模: 井字棋游戏为例

- 嵌套的(nested)字典和列表
  
  - 嵌套读取的一个例子：
  
  ```python
  for k, v in guests.items():
    numBrought = numBrought + v.get(item, 0)
    
  ```

## 第06章 字符串操作

- 转义字符:  \t制表符, \n换行符, \\倒斜杠, \\\`单引号， \\"双引号

- 原始字符串，在引号之前加r 。用于正则表达式字符串很有用。

  ``` python
  >>> print(r'That is Carol\'s cat.'')
  That is Carol\'s cat.
  ```

- 三重引号, 三个单引号或三个双引号作为起止。其间所有的引号、制表符或**换行符**(不需要额外敲入`\n`)都视为字符串的一部分。

- 注释单行用#，多行用三重双引号作为起止

- 无论spam是列表，字符串还是元祖/tuple，切片读取的代码都是spam[]格式，in和not in操作符同样可用

- 字符串方法`.upper()`, `.lower()`, `.isupper()`, `.islower()`, `.isalpha()`, `.isalnum()`, `.isdecimal()`, `.isspace()`, `.istitlle()`, `.startswith()`, `endswith()`, `.join()`, `.split()`, `.rjust()`, `.ljust()`, `.center()`, `.strip()`, `.rstrip()`, `.lstrip()`,

- 用pyperclip模块拷贝粘贴字符串

  ``` python  
  >>> import pyerclip
  >>> pyerclip.copy('Hello world!')
  >>> pyerclip.paste()
  'Hello world!'
  ```

  - 安装第三方模块pyperclip的方法，Windows下使用Anaconda，可以打开anaconda prompt输入`pip install pyperclip`即可， Mac下终端输入: `conda install -c conda-forge pyperclip`, 等待响应`Collecting package metadata (repodata.json): done`等之后即可。如果输入`pip install pyperclip`则仅仅是给Mac自带的python程序安装该包，与Anaconda无关。
  - PyCharm设置解释器选项中的pyperclip安装包配置问题参见[这里](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000083390-Unable-to-Import-pyperclip)。

- 项目“口令保管箱”程序pw.py运行FAQ:

  - 可以将路径改成Anaconda的python.exe所在路径，参考附录B的做法添加到环境变量中的PATH
  - 路径名称中的目录名（或者可能包括用户名）有空格，可以将整条路径语句用双引号前后包围起来。
  - 注意pw.py代码的第一行中为`#!python3`，这里3和python之间没有空格，否则也会运行网上看到的其他人的运行问题：Can't open file... [Errno 2] No such file or directory
  - 注意pw.bat中的代码最后结尾部分有`%*` ，用于表示输入任何变量，对应这里的account
  - windows下输入pw email后，运行成功，可以ctrl+c查看效果，如果只输入pw，后面没有接email等任意账号，则会显示Usage开头的那条语句。
  
- 项目“表格打印”编写FAQ:

  - 不要用书中的生成列表方法`colWidths = [0] * len(tableData)`, 理由是因为`[[None]*n]*m` 这样的方式生成的列表, 里面的全部都这是引用, 都是同一个对象, 并不是m个对象! 因为你已经将多个引用复制到同一个对象。
  - `for a in range(len(tableData)):`这样的语句不要错写成`for a in range(tableData):`或`for a in tableData:`

# 第二部分 自动化任务

## 第07章 模式匹配与正则表达式

- 技术专家Cory Doctorow声称，甚至应该在教授编程之前，先教授正则表达式：知道正则表达式可能意味着用3步解决问题，而不是用3000步。(论vi正则表达式练习的重要性)

- `import re`导入正则表达式块之后，使用`re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')`返回一个Regex(正则表达式)对象，这里re是regular express的缩写，compile表示编制、编译的意思，所以括号内是正则表达式，引号内的\d表示一个数字字符，而引号前加r表示将该字符串标记为原始字符串（见P97, 6.1.4），而非转义字符。

- Regex对象的search()方法查找传入的字符串，返回一个Match对象，Match对象有一个group()方法返回匹配的文本。

  ``` python
  >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
  >>> mo = phoneNumRegex.search('My number is 415-555-4242')
  >>> print('Phone number found: ' + mo.group())
  ```

- 利用括号分组，管道匹配多个分组，问号实现可选匹配，星号匹配零次或多次，加号匹配一次或多次，花括号匹配特定次数。

- 花括号匹配次数{}默认为贪心匹配模式，加?改为非贪心。

- .findall()和.search()的区别，在于前者返回一个匹配字符串列表或字符串的元组的列表。

- 字符分类\w, \W, \s, \S

  ```python
  >>> xmasRegex =re.complier(r'\d+\s\w+')   
  >>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 4 birds, 3 hens, 2 doves, 1 partridge')
  ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '4 birds', '3 hens', '2 doves', '1 partridge']
  ```

  这里```\d+\s\w+```表示一个或多个数字，接一个空白字符，接一个或多个字母/数字/下划线字符.

  

  

---
## PyCharm使用笔记
### PyCharm Tutorial
#### [PyCharm Tutorial #1 - Setup & Basics:](https://www.youtube.com/watch?v=56bPIGf4us0)
- Shift + Alt + C: 查看文件修改记录

### [Getting Started with PyCharm](https://www.youtube.com/watch?v=BPC-bGdBSM8&list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP)
#### Quick Tour:

### Tips for Vim:
- 在PyCharm中启用或取消vim插件功能的快捷键: Ctrl + Alt + v
- undo: u, 3u means undo last 3 times
- redo: ctrl + r
- search: /, and press n to locate the next words
- :%s/old/new/gc: search all old and replace with new,  gc means greedily with confirm
- :$/old/new: work in the first old with new in current line
- :$/old/new/g: all in current line
- :set nu
- :set nonu
- a, o, A, O, i, I, 0, ^, $, gg, G, nG, w, nw, W, h, nh, b, B,  n+, n-, x, nx, H, L
- delete liens: dd, ndd, dW, d$, d0, d^, dG, dnG, dw, dW
- cw
- p, P
- c
- r, 5r, R
- v, V
- R
- fx: find x in the current line
- y, yy means ddP or copy current line, notice that dd means cut, not delete


