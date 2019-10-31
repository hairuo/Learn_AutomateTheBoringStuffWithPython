# 如何写一个正则表达式，匹配姓Nakamoto的完整姓名？你可以假定名字总是出现在姓前面，是一个大写字母开头的单词。该正则表达式必须匹配：
#
# 'Satoshi Nakamoto'
# 'Alice Nakamoto'
# 'RoboCop Nakamoto'
# 但不匹配：
#
# 'satoshi Nakamoto'（名字没有大写首字母）
# 'Mr. Nakamoto'（前面的单词包含非字母字符）
# 'Nakamoto' （没有名字）
# 'Satoshi nakamoto'（姓没有首字母大写）

import re
NameRegex = re.compile(r'(^[A-Z][a-z]*\s[A-Z][a-z]*$)')
# NameRegex = re.compile(r'(^[A-Z][a-z]*\s[A-Z][a-z]*$)')
print('Please input a name with correct format like Michael Jordan: ')
test = input()
mo = NameRegex.search(test)
if mo != None:
    print('Name find: ' + mo.group())
else:
    print('Format is wrong!')