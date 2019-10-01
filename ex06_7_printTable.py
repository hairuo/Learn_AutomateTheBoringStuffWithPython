def printTable(tableData):
    colWidths = [[None for x in range(len(tableData))] for y in range(len(tableData[0]))]
    # [[None]*n]*m 这样的方式生成的列表, 里面的全部都这是引用, 都是同一个对象, 并不是m个对象! 因为你已经将多个引用复制到同一个对象。
    # 所以书中提到的colWidths = [0] * len(tableData) 这种生成列表的方法不可采纳!!!
    print(colWidths)

    n = 0
    for i in range(len(tableData[0])):
        # result = ''
        if n < len(tableData[0]):
            m = 0
            for j in range(len(tableData)):
                if m < len(tableData):
                    colWidths[n][m] = tableData[j][i]
                    # result = result + colWidths[n][m] + ', '
                    # print(colWidths[n][m])
                    m += 1
                else:
                    break
            # print(result)
            # colWidths[n] = result
            print(colWidths[n])
            # colWidths[n]
            n += 1
        else:
            break
    print(colWidths)

    r = [0 for a in range(len(tableData))]  #generate a list [0, 0, 0]
    for x in range(len(tableData)):
        for y in range(len(tableData[x])):
            if r[x] <= len(tableData[x][y]):
                r[x] = len(tableData[x][y])
            else:
                continue

    for k in range(len(colWidths)):
        for l in range(len(r)):
            if l == 0:
                print(colWidths[k][l].rjust(r[l]), end = '')
            else:
                print(colWidths[k][l].rjust(r[l]+1), end='')
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['us', 'canada', 'china', 'japan']]

printTable(tableData)