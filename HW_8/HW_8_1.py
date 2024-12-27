"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и
все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""

from pathlib import Path
import os, csv, json, pickle
import pprint


def save_dir(path: Path = Path.cwd()) -> None:
    if path.is_dir():
        data = dir_rec(path)
        pprint.pprint(data, indent=2)
        save_to_json(data, 'hw8_result.json')
        save_to_csv(data, 'hw8_result.csv')
        save_to_pickle(data, 'hw8_result.pkl')
    else:
        print('Это не директория!')

def dir_rec(path: Path):
    data = []
    path = Path(path)
    for file in path.iterdir():
        dir_size = 0


        if file.is_dir():
            dir_path = os.path.abspath(file)
            dir_size += get_dir_size(dir_path)
            data.append({
                'name': file.name,
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': str(path),
            })
            data += dir_rec(Path(dir_path))

        if file.is_file():
            file_path = os.path.abspath(file)
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            data.append({
                'name': file.name,
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent_directory': str(path)
            })

    return data

def get_dir_size(path):
    total_size = 0

    for path, dirs, files in os.walk(path):
        for file in files:
            f_path = os.path.join(path, file)
            total_size += os.path.getsize(f_path)

    return total_size


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def save_to_csv(data, filename):
    headers = ['name','path', 'type', 'size', 'parent_directory']
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    # save_dir(Path('C:\\Nata\\GeekBrains\\gb-git\\python_adv\\seminar7'))
    save_dir()
