# Homework 20 of chapter 07:
# 如何写一个正则表达式，匹配每3位就有一个逗号的数字？它必须匹配以下数字：

# '42'
# '1,234'
# '6,368,745'
# 但不会匹配：
#
# '12,34,567' （逗号之间只有两位数字）
# '1234' （缺少逗号）

import re
NumberRegex = re.compile(r'(^\d{1,3})$|(^\d{1,3},\s?\d{3}$)|(^(\d{1,3},\s?)?\d{3},\s?\d{3}$)')
# NumberRegex = re.compile(r'(^\d{1,3})$|(^\d{1,3},\d{3}$)')
print('Please input a number with correct format like 1,234: ')
test = str(input())
mo = NumberRegex.search(test)
if mo != None:
    print('Number find: ' + mo.group())
else:
    print('Format is wrong!')

# Q: what if the number has more commas? or how to match any correct large number.

# import re
# NumberRegex = re.compile(r'(\d{1,3})|(\d{1,3},\d{3})|((\d{1,3},)?\d{3},\d{3})')
# mo = NumberRegex.findall('63,68,745')
# print(mo)

