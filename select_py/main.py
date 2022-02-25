import os
import fnmatch
#в цикле, с помощью os.listdir('.') получ. список файлов
#в текущей директории (точка ее и обозначает)
for fname in os.listdir('.'):
    #else extended *.py then print
    if fnmatch.fnmatch(fname,'*.py'):
        print(fname)


