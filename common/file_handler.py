from pathlib import Path

import yaml


def file_create(file_path, file_name):
    whole_path = file_path + file_name
    i = 0
    name = file_name.split('.')[:-1]
    suffix = '.' + file_name.split('.')[-1]
    if not Path(file_path).is_dir():
        Path(file_path).mkdir()  # 如果不存在，创建文件夹
    while Path(whole_path).is_file():  # 判断文件是否已经存在
        i += 1
        file_name = name + str(i) + suffix
        whole_path = file_path + file_name
    return whole_path


def path_create(path):
    if not Path(path).is_dir():
        Path(path).mkdir(parents=True)
    return path


def read_yaml(file):
    if not Path(file).is_file():
        raise FileNotFoundError('文件不存在')
    with open(file, 'rb') as f:
        data = list(yaml.safe_load_all(f))[0]
    return data


def filename_duplicates(file):
    file_name = file.rsplit('.', 1)[0]
    file_suffix = '.' + file.rsplit('.', 1)[1]
    i = 0
    while Path(file).is_file():
        i += 1
        file = file_name + str(i) + file_suffix
    return file
# def file_check(file_name):
#     path = file_name.split('\\')[:-1]
#     path_check(path)
#     name=file_name.split('\\')[-1]
#
#
