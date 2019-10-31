def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-' ))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': '0004', 'apples': '0012', 'cups': '0004', 'cookies': 8000}
printPicnic(picnicItems, 12, 10)
printPicnic(picnicItems, 21, 1)