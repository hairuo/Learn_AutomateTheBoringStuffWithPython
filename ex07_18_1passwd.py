# 设置长度不少于8个字符，包含大小写，至少一位数字的密码
import re
def passwdVerify(passwd):
    passwdRegex = re.compile(r'''([a-z]+[a-zA-Z0-9]*[A-Z]+[a-zA-Z0-9]*[0-9]+[a-zA-Z0-9]*)|         #a*A*1*
                                 ([A-Z]+[a-zA-Z0-9]*[a-z]+[a-zA-Z0-9]*[0-9]+[a-zA-Z0-9]*)|         #A*a*1*
                                 ([a-z]+[a-zA-Z0-9]*[0-9]+[a-zA-Z0-9]*[A-Z]+[a-zA-Z0-9]*)|         #a*1*A*
                                 ([A-Z]+[a-zA-Z0-9]*[0-9]+[a-zA-Z0-9]*[a-z]+[a-zA-Z0-9]*)|         #A*1*a*
                                 ([0-9]+[a-zA-Z0-9]*[a-z]+[a-zA-Z0-9]*[A-Z]+[a-zA-Z0-9]*)|         #1*a*A*
                                 ([0-9]+[a-zA-Z0-9]*[A-Z]+[a-zA-Z0-9]*[a-z]+[a-zA-Z0-9]*)          #1*A*a*
                             ''', re.VERBOSE)
    # passwdRegex = re.compile(r'')

    mo = passwdRegex.search(passwd)
    if mo != None and len(mo.group()) >= 8:
        print('Correct password: ' + mo.group())
    else:
        print('Wrong password!')

print('Please input your password: ')
test = input()
passwdVerify(test)