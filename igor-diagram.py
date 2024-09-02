#!/usr/bin/python

import os
import matplotlib.pyplot as plt

# это лучше назать format_size - "форматировать размер"
#  get_size_format - "получить формат размера" - неудачное название, сбивает с толку
def get_size_format(b, factor = 1024, suffix = 'B'):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return  f"{b:.2f}{unit}{suffix}"
        b /= factor
    return  f"{b:.2f}Y{suffix}"

# here get_xxx is OK
def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total


# it works OK
def plot_pie(sizes, names): # была ОЧЕПЯТКА : не pio_pie, а наоборот plot_pie, этим плоха буква лэ 
    plt.pie(sizes, labels = names, autopct = lambda  pct: f"{pct:.2f}%")
    plt.title("Размеры подкаталогов и файлов")
    plt.show()


# здесь нужно указать МАЛЕНЬКУЮ тестовую папку с мусором
# указывая ВЕСЬ домашний каталог рискуешь потерять все файлы
folder_path = '/home/prog/tmp'  # конечно, в реальном случае - этот путь должен браться из аргументов скрипта


# здесь перепутано имя для списка - directory - это имя каталога, для списка с размерами нужно другое имя
# пусть такое
all_directory_sizes = [] # можно или all или множественное число или _list на конце имени переменной 
names = [] # множественное число - это правильно
# Вообще-то, эти 2 переменные должны быть одним списком, внутри которого лежит кортеж из имени(пути) и размера
#  о МОДЕЛЯХ ДАННЫХ я рассказывал

# по-факту - здесь отчасти делается часть из get_directory_size (берётся список), поэтому их нужно соединить 
for directory in os.listdir(folder_path):
    directory = os.path.join(folder_path, directory)
    directory_size = get_directory_size(directory)

    # if directory == 0:
    if directory_size == 0: # кажется это имелось ввиду
        continue # такое прерывание в середине мне не нравится

    all_directory_sizes.append(directory_size)
    # names.append(os.path.basename(directory) + ": " + get_size_format(directory))
    names.append(directory) # кажется так должно быть

# print("Общий размер каталога:", get_size_format(sum(directory_size)))
# plot_pie(directory_size, names)

print("Общий размер каталога:", get_size_format(sum(all_directory_sizes)))
plot_pie(all_directory_sizes, names)
