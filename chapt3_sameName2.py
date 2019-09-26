def spam():
    global eggs  # global
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)