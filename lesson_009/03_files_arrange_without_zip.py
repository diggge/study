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
        self.file_time={}
    def parser(self):
        self.path_normalized=os.path.normpath(self.source_dir)
        for dirpath, dirnames, filenames in os.walk(self.path_normalized):
            for self.file in filenames:
                true_path_file=os.path.join(dirpath, self.file)
                secs = os.path.getmtime(true_path_file)
                self.check_dir = os.path.dirname(os.path.join(dirpath, self.file))
                self.file_time = time.gmtime(secs)
                self.final_path=f'{self.destination_dir}/{self.file_time[0]}/{self.file_time[1]}/{self.file_time[2]}'
                print(os.path.join(self.check_dir,self.file), os.path.join(self.final_path),self.file)
                if os.path.exists(self.final_path) is True:
                    shutil.copy2(os.path.join(self.check_dir, self.file), os.path.join(self.final_path, self.file))
                else:
                    os.makedirs(self.final_path)
                    shutil.copy2(os.path.join(self.check_dir, self.file),os.path.join(self.final_path, self.file))
sorting_files_date=Sorting_files_date(source_dir='C:/Users/user/study/lesson_009/icons',destination_dir='C:/Users/user/study/lesson_009/icons_by_year')
sorting_files_date.parser()






