# -*- coding: utf-8 -*-

import os
from time import gmtime

# Все файлы лежат на диске и имеют путь в файловой системе. Как работать с файлами на уровне ОС?
# Есть встроенные модули для этого: os, os.path, shutil
# Пригодятся они для написания скриптов-аналогов bash (.bat файлов в Windows)

path = 'C:/Windows/help'
path_normalized=os.path.normpath(path)
count=0
# Пройтись по всем файлам в директории.
# os.path.join(path1[, path2[, ...]])
for dirpath, dirnames, filenames in os.walk(path_normalized):
    print('*'*40)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    # print(os.path.dirname(__filenames__))
    count+=1
    for file in filenames:
        full_file_path=os.path.join(dirpath,file)
        x=os.path.getsize(full_file_path)/(1024)
        print('Размер файла =',round(x,2), 'Кбайт')
        print(full_file_path,' Время создания файла:  ',gmtime(os.path.getmtime(full_file_path)))
        # print(os.path.getsize(file))

print('Количество папок {0:5d}'.format(count))
print(__file__,os.path.dirname(__file__))