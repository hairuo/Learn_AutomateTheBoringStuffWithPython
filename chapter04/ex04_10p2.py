grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# print(len(grid[0]))

dirg = [[None]*len(grid)]*len(grid[0])
# print(dirg)
n = 0

for i in range(len(grid[0])):
        result = ''
        if n < len(grid[0]) :
                m = 0
                for j in range(len(grid)):
                        if m < len(grid):
                                dirg[n][m]= grid[j][i]
                                result = result + dirg[n][m]
                                m += 1
                        else:
                                break
                print(result)
                # print(dirg[n])
                n += 1
        else:
                break
