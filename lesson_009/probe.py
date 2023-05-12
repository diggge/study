import os
import time

# Все файлы лежат на диске и имеют путь в файловой системе. Как работать с файлами на уровне ОС?
# Есть встроенные модули для этого: os, os.path, shutil
# Пригодятся они для написания скриптов-аналогов bash (.bat файлов в Windows)

path = 'C:/Windows/Help'
path_normalized=os.path.normpath(path)
# Пройтись по всем файлам в директории.
for dirpath, dirnames, filenames in os.walk(path_normalized):
    # print(dirpath, dirnames, filenames)
    for file in filenames:
        secs=os.path.getmtime(dirpath+'\\'+file)
        file_time = time.gmtime(secs)

        print(dirpath+'\\'+file,round(os.path.getsize(dirpath+'\\'+file)/1024,2), 'КБ', file_time)


# os.path.normpath(path)

