# Task: 写一个函数，功能和strip()字符串一样。如果传入了要去除的字符串，没有其他参数，那么就去除空白字符。否则，按第二个参数去除指定字符。
# Tips: #7.12 用sub()方法替换字符串

import re
def stripLike(a, b=''):
    if b == '':
        # match string a start with space or end with space, and substitute it.
        namesRegex = re.compile(r'^\s+|\s+$')
        a = namesRegex.sub('', a)
        # print(a)
    else:
        c = '|'.join(list(b))
        # print(c)
        # namesRegex = re.compile(r'^((%s)+)|((%s)+)$'%c)  # this doesn't work because two %s and one %c
        # below web page only tells me use one %s at a time:
        # https://stackoverflow.com/questions/24637917/how-to-add-a-variable-into-my-re-compile-expression
        nameStart = re.compile(r'^((%s)+)'%c)   # Tried to delete the beginning part firstly
        a = nameStart.sub('', a)
        nameEnd = re.compile(r'((%s)+)$'%c) # Then the last part, use only one %s at a time
        a= nameEnd.sub('', a)
        # print(a)
    return a
    # seems like after define b='' in stripLike(a, b=''), we can return a
# Notice: 不能直接将a中的字符串b替换为''，因为b本身作为字符串是有字符顺序的。而a.strip(b)中的b的字符顺序是无所谓的。
# 参考了github上其他很多程序，发现不用.strip，很难实现这个字符无顺序功能。
# 后来想到可以使用上面语句中的'|'.join((list(b))功能，终于实现完全等效的strip功能

test = input('Please input a string:')
delete = input('Please input stripped par or just return:')
print(stripLike(test, delete))
