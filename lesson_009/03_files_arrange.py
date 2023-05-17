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
            for file in self.zf.infolist():
                date = datetime.datetime(*file.date_time)
                name = os.path.basename(file.filename)
                self.final_path = f"{self.destination_dir}/{date.strftime('%Y')}/{date.strftime('%m')}"
                print(f"{name}, {self.final_path}, {date.strftime('%Y.%m')}",file)
                #
                if not name:
                        continue
                if os.path.exists(self.final_path) is True:
                    source = self.zf.open(file)
                    target = open(os.path.join(self.final_path,name),'wb')
                    with source, target:
                        shutil.copyfileobj(source,target)
                else:
                    source = self.zf.open(file)
                    target = open(os.path.join(self.final_path, name), 'wb')
                    os.makedirs(self.final_path)
                    with source, target:
                        shutil.copyfileobj(source,target)


                # if os.path.exists(self.final_path) is True:
                #
                # else:
                #      os.makedirs(self.final_path)

                # print(self.final_path)
    # def check_extract(self):
    #     if os.path.exists(self.final_path) is True:
    #         self.zf.extract(self.file,self.final_path)
    #     else:
    #         os.makedirs(self.final_path)
    #         self.zf.extract(self.file, self.final_path)
sorting_files_date=Sorting_files_date(file_name='icons.zip',destination_dir='c:/users/Admin/PycharmProjects/study/lesson_009/icons_by_year')
sorting_files_date.unzip()
# sorting_files_date.check_extract()

#     def parser(self):
#         self.path_normalized=os.path.normpath(self.source_dir)
#         for dirpath, dirnames, filenames in os.walk(self.path_normalized):
#             for self.file in filenames:
#                 true_path_file=os.path.join(dirpath, self.file)
#                 secs = os.path.getmtime(true_path_file)
#                 self.check_dir = os.path.dirname(os.path.join(dirpath, self.file))
#                 file_time = time.gmtime(secs)
#                 self.final_path=f'{self.destination_dir}/{file_time[0]}/{file_time[1]}/{file_time[2]}'
#                 print(os.path.join(self.check_dir,self.file), os.path.join(self.final_path),self.file)
#     def check_copy(self):
#         if os.path.exists(self.final_path) is True:
#             shutil.copy2(os.path.join(self.check_dir, self.file), os.path.join(self.final_path, self.file))
#         else:
#             os.makedirs(self.final_path)
#             shutil.copy2(os.path.join(self.check_dir, self.file),os.path.join(self.final_path, self.file))
# sorting_files_date=Sorting_files_date(source_dir='C:/Users/Admin/PycharmProjects/study/lesson_009/icons',destination_dir='C:/Users/Admin/PycharmProjects/study/lesson_009/icons_by_year')
# sorting_files_date.parser()
# sorting_files_date.check_copy()


# path='c:/users/user/study/lesson_009/icons'
# path_normalized=os.path.normpath(path)
# for dirpath, dirnames, filenames in os.walk(path_normalized):
#     # print(dirpath,dirnames,filenames)
#     for file in filenames:
#         secs = os.path.getmtime(os.path.join(dirpath, file))
#         # print(secs)
#         file_time = time.gmtime(secs)
#         check_dir = os.path.dirname(os.path.join(dirpath, file))
#         # print(os.path.dirname(os.path.join(dirpath, file)),'Существует ли папка?',os.path.exists(check_dir))
#                 # final_path
#         final_path=f'c:/users/user/study/lesson_009/icons_by_year/{file_time[0]}/{file_time[1]}'
#         print(os.path.join(check_dir, file), os.path.join(final_path, file))
#         if os.path.exists(final_path) is True:
#             # print('True')
#             shutil.copy2(os.path.join(check_dir, file),os.path.join(final_path, file))
#         else:
#             os.makedirs(final_path)
#             shutil.copy2(os.path.join(check_dir, file),os.path.join(final_path, file))
#             # print('False')
#         # print(final_path)
#
#С помощью метода is_dir() можно проверить, является ли элемент в архиве папкой:
# from zipfile import ZipFile
#
# with ZipFile("metanit.zip", "r") as myzip:
#     for item in myzip.infolist():
#         if (item.is_dir()):
#             print(f"Папка: {item.filename}")
#         else:
#             print(f"Файл: {item.filename}")

