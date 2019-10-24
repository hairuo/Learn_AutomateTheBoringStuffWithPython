# 写一个函数，功能和strip()字符串一样。如果传入了要去除的字符串，没有其他参数，那么就去除空白字符。否则，按第二个参数去除指定字符。
# 提示: #7.12 用sub()方法替换字符串

import re
def stripLike(a, b):
    # if b == '':
    #     # match string a start with space or end with space, and substitute it.
    #     namesRegex = re.compile(r'^\s+|\s+$')
    #     print(namesRegex.sub('', a))
    # else:
#以上b=''情形可以忽略，写到下面去。
# 参考: https://stackoverflow.com/questions/24637917/how-to-add-a-variable-into-my-re-compile-expression
        namesRegex = re.compile(r'^\s+|%s|\s+$'%b)
        print(namesRegex.sub('', a))
# 将a中的字符串b替换为''，但是b本身作为字符串是有字符顺序的。而a.strip(b)中，b的字符顺序是无所谓的。
# 参考了很多github上其他很多程序，发现不用.strip，很难实现这个功能。待考再更新.

test = input('Please input a string:')
delete = input('Please input stripped part or just return:')
stripLike(test, delete)

