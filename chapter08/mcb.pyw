#! python3
# mcb.pyw - Save and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Load keyword to clipboard.
#        py.exe mcb.pyw list - Load all keywords to clipboard.
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
          # List keywords and load content.
    if sys.argv[1].lower () == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

# 该程序将利用一个关键字保存每段剪贴板文本。例如， 当运行 py mcb.pyw save spam，
# 剪贴板中当前的内容就用关键字 spam 保存。 通过运行 py mcb.pyw spam， 这
# 段文本稍后将重新加载到剪贴板中。如果用户忘记了都有哪些关键字， 他们可以运
# 行 py mcb.pyw list，将所有关键字的列表复制到剪贴板中。

# 注意sys.argv, pyperclip.copy(), pyperclip.paste()的使用