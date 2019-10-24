# 写一个函数，功能和strip()字符串一样。如果传入了要去除的字符串，没有其他参数，那么就去除空白字符。否则，按第二个参数去除指定字符。
# 提示: #7.12 用sub()方法替换字符串

import re
def stripLike(a, b):
    if b == '':
        # match string a start with space or end with space, and substitute it.
        namesRegex = re.compile(r'^\s+|\s+$')
        print(namesRegex.sub('', a))
    else:
        c = '|'.join(list(b))
        # print(c)
        # namesRegex = re.compile(r'^((%s)+)|((%s)+)$'%c)  #同时使用两个%s是不知道如何引入两个%c
        # re.compile表达式中变量引入格式参考(只提到一个变量的用法):
        # https://stackoverflow.com/questions/24637917/how-to-add-a-variable-into-my-re-compile-expression
        nameStart = re.compile(r'^((%s)+)'%c)   #先去头
        a = nameStart.sub('', a)
        nameEnd = re.compile(r'((%s)+)$'%c) #再去尾，这样一次引入一个变量c
        print(nameEnd.sub('', a))
# 将a中的字符串b替换为''，但是b本身作为字符串是有字符顺序的。而a.strip(b)中，b的字符顺序是无所谓的。
# 参考了github上其他很多程序，发现不用.strip，很难实现这个字符无顺序功能。
# 后来想到可以使用上面语句中的'|'.join((list(b))功能，终于实现完全等效的strip功能

test = input('Please input a string:')
delete = input('Please input stripped par or just return:')
stripLike(test, delete)

