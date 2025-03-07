import os
import time


directory = '.'
for root, dirs, files in os.walk(directory):
    print('Текущая директория:', os.getcwd())
    print(f'>> root = "{root}", dirs = "{dirs}"')
    for i, file in enumerate(files):
        print(f'{i + 1}:', end=' ')
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(root)
        print(
            f'Обнаружен файл: {file},'
            f' Путь: {filepath},'
            f' Размер: {filesize} байт,'
            f' Время изменения: {formatted_time},'
            f' Родительская директория: {parent_dir}')