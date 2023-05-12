import os

# Все файлы лежат на диске и имеют путь в файловой системе. Как работать с файлами на уровне ОС?
# Есть встроенные модули для этого: os, os.path, shutil
# Пригодятся они для написания скриптов-аналогов bash (.bat файлов в Windows)

path = 'C:/Windows/Help'
path_normalized=os.path.normpath(path)
# Пройтись по всем файлам в директории.
for dirpath, dirnames, filenames in os.walk(path_normalized):
    # print(dirpath, dirnames, filenames)
    for file in filenames:
        print(dirpath+'\\'+file,round(os.path.getsize(dirpath+'\\'+file)/1024,2),'КБ',os.path.getmtime(dirpath+'\\'+file))


# os.path.normpath(path)

