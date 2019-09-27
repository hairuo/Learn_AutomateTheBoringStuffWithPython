def listand(anylist):
    endlist = ''
    for i in range(len(anylist)):
        if i < len(anylist) - 1:
            endlist = endlist + ' ' + anylist[i] +','
        elif i == len(anylist) - 1:
            endlist = endlist + ' and ' + anylist[i]  + '.'
            break
    print(endlist)


spam = ['apples', 'bananas', 'tofu', 'cats']
listand(spam)