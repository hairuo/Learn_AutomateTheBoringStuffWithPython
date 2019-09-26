def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global， 因为eggs未被赋值，所以当作全局变量

eggs = 42 # this is the global
spam()
print(eggs)