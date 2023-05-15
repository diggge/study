# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
class Sorting_files_date:
    def __init__(self,source_dir,destination_dir):
        self.source_dir=source_dir
        self.destination_dir = destination_dir
    def parser(self):
        path_normalized=os.path.normpath(self.source_dir)
        for dirpath, dirnames,filenames in os.walk(path_normalized):
            for file in filenames:
                secs = os.path.getmtime(os.path.join(dirpath, file)
                file_time = time.gmtime(secs)
                final_path=

path='c:/users/user/study/lesson_009/icons'
path_normalized=os.path.normpath(path)
for dirpath, dirnames, filenames in os.walk(path_normalized):
    # print(dirpath,dirnames,filenames)
    for file in filenames:
        secs = os.path.getmtime(os.path.join(dirpath, file))
        # print(secs)
        file_time = time.gmtime(secs)
        check_dir = os.path.dirname(os.path.join(dirpath, file))
        # print(os.path.dirname(os.path.join(dirpath, file)),'Существует ли папка?',os.path.exists(check_dir))
                # final_path
        final_path=f'c:/users/user/study/lesson_009/icons_by_year/{file_time[0]}/{file_time[1]}'
        print(os.path.join(check_dir, file), os.path.join(final_path, file))
        if os.path.exists(final_path) is True:
            # print('True')
            shutil.copy2(os.path.join(check_dir, file),os.path.join(final_path, file))
        else:
            os.makedirs(final_path)
            shutil.copy2(os.path.join(check_dir, file),os.path.join(final_path, file))
            # print('False')
        # print(final_path)




