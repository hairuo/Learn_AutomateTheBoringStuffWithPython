def spam():
    eggs = 'spam local'
    print(eggs) # priints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) #prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

# 虽然可以在不同作用于中使用相同的变量名，但程序在执行完局部作用域后，该变量就销毁了，所以最后一句返回global