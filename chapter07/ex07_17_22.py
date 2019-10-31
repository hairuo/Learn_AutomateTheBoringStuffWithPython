# 22．如何编写一个正则表达式匹配一个句子，它的第一个词是Alice、Bob或Carol，第二个词是eats、pets或throws，第三个词是apples、cats或baseballs。该句子以句点结束。这个正则表达式应该不区分大小写。它必须匹配：
#
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# 但不匹配：
#
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'

import re
SentenceRegex = re.compile(r'(^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).$)', re.I)
# SentenceRegex = re.compile(r'(^(Alice|Bob|Carol)$)', re.I)
print('Please input a sentence with assumed vocabulary: ')
test = input()
mo = SentenceRegex.search(test)
if mo != None:
    print('Correct sentence: ' + mo.group())
else:
    print('Wrong sentence!')