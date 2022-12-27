#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distances = dict()
moscow=sites['Moscow']
moscow_london=((sites['Moscow'][0]-sites['London'][0])**2+(sites['Moscow'][1]-sites['London'][1])**2)**0.5
moscow_paris=((sites['Moscow'][0]-sites['Paris'][0])**2+(sites['Moscow'][1]-sites['Paris'][1])**2)**0.5
london_paris=((sites['London'][0]-sites['Paris'][0])**2+(sites['London'][1]-sites['Paris'][1])**2)**0.5
distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris
distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris
distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_paris
distances['Paris']['London'] = london_paris
# distances['London']['Paris'] = london_paris
print(distances)
pprint(distances)