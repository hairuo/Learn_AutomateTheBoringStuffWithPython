def spam():
    print(eggs) # ERROR!  python不会在执行spam()时退回使用全局变量eggs，而局部变量eggs不存在，于是报错。
    eggs = 'spam local'

eggs = 'global'
spam()
