# ! python3
# 创建一个疯狂填词（Mad Libs）程序，它将读入文本文件， 并让用户在该文本
# 文件中出现 ADJECTIVE、 NOUN、 ADVERB 或 VERB 等单词的地方， 加上他们自
# 己的文本。

madlibFile = open('MadLibs.txt')
madlibContent = madlibFile.read()
madlibFile.close()
print('Here is the content of MadLibs.txt:\n')
print(madlibContent)
print('\n')
list = madlibContent.split()
print(list)
for i in range(len(list)):
   if list[i].upper() == 'ADJECTIVE':
       list[i] = input('please input an adjective:\n')
   elif list[i].upper() == 'NOUN':
       list[i] = input('please input a noun: \n')
   elif list[i].upper() == 'ADVERB':
       list[i] = input('please input a adverb:\n')
   elif list[i].upper() == 'VERB':
       list[i] = input('please input a verb:\n')

print('Here is the modified content of MadLibs.txt:\n')
madlibContent = " ".join(list)
print(madlibContent)

