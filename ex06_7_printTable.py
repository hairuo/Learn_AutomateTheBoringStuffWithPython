def printTable(tableData):
    colWidths = [[None]*len(tableData)]*len(tableData[0])

    n = 0
    for i in range(len(tableData[0])):
        result = ''
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
    print(colWidths)   # Some problems here
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)