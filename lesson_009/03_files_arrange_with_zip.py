# -*- coding: utf-8 -*-
import datetime
import os, time, shutil,zipfile, datetime

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
    def __init__(self,file_name,destination_dir):
        self.destination_dir = destination_dir
        self.file_name = file_name
    def unzip(self):
        with zipfile.ZipFile(self.file_name,'r') as self.zf:
            for member in self.zf.infolist():
                date = datetime.datetime(*member.date_time)
                filename= os.path.basename(member.filename)
                self.final_path = f"{self.destination_dir}/{date.strftime('%Y')}/{date.strftime('%m')}"
                if not filename:
                    continue
                if os.path.exists(self.final_path) is True:
                    source = self.zf.open(member)
                    target = open(os.path.join(self.final_path, filename), 'wb')
                    with source, target:
                        shutil.copyfileobj(source,target)
                else:
                    os.makedirs(self.final_path)
                    source = self.zf.open(member)
                    target = open(os.path.join(self.final_path, filename), 'wb')
                    with source, target:
                        shutil.copyfileobj(source,target)

sorting_files_date = Sorting_files_date(file_name='icons.zip',destination_dir='C:/Users/user/study/lesson_009/icons_by_year')
sorting_files_date.unzip()

