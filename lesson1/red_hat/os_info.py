#-*- coding: utf-8 -*-

#Нужно собрать информацию об операционной системе и версии пайтона

#TODO запустить этот скрипт а закомитить результат его работы2

import sys
import platform

info = 'OS info is \n {} \n\n Python version is {} {}'.format (
    platform.uname(), sys.version, platform.architecture())
print(info)

with open ('os_info.txt', 'w') as ff:
    ff.write(info)
