import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'      # learn how to use 'return' considering if, elif
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# r = random.randint(1, 9)
# print ('r =', r)
# Q: Still not sure about why it has a ',' here
# A:  https://realpython.com/python-print/, here ',' work as a single space
# message = 'r = ' + str(r)
# print(message)
# fortune = getAnswer(r)
# print(fortune)

# Pycharm多行注释快捷键 Ctrl + /
print(getAnswer(random.randint(1, 9)))   # 缩写成一行等价的代码