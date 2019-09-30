#! python3
# bulletpointAdder.py -Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()   #从剪贴板粘贴内容并赋值给text
print(text)

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text) #复制给剪贴板
print(text)
