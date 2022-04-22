# coding : utf-8

# Комментарий

import os
import pip
import sys
import psutil
import shutil
import random


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + ' .dupl'
        shutil.copy(filename, newfile)  # копируй, от куда и куда
        if os.path.exists(newfile):
            print("Файл", newfile, "был успешно создан")
            return True
        else:
            print("Возникли проблемы с копированием")
            return False


def duble_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1

def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print("Файл", fullname,"был случано удален")

def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессов:", pip)
    print("Платформа:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Текущая директория:", os.getcwd())
    print("Текущая пользователь:", os.getlogin())


def delet_dupli(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                doubl_count += 1
                print("Файл", fullname, "был успешно удален")
    return doubl_count


def main():
    global count
    print("Great Python Program!")
    print("Привет, програмист!")
    name = input("Ваше имя:")
    print(name, "Добро пожаловать в мир Python!")

    answer = ''
    while answer != 'Q':
        answer = input("\nВыбери действие: \nY-начать работу \nN-завершить работу \nQ-неизвестный ответ \n")
        if answer == "Y":
            print("Отлично! Давай поработаем.")
            print(
                """
            Вот что я могу: 
            1- Запустить список файлов
            2- Запустить информацию о системе 
            3- Запустить список процессов
            4- Продублировать файлы в текущей директории
            5- Продублировать указанный файл
            6- Удалить дубликаты файлов
            7- Удалить случайный файл
            """
            )
            choice = input("Выбери дейтвие из списка:")
            if choice == "1":
                print(os.listdir())
            elif choice == "2":
                sys_info()
            elif choice == "3":
                print("Запуск списка процессов:", psutil.pids())
            elif choice == "4":
                print("==Дублирование файлов в текущей директории==")
                duble_files('.')
                # file_list = os.listdir()
                # i = 0
                # while i < len(file_list):
                # duplicate_file(file_list[i])
                # i += 1
            elif choice == "5":
                print("Продублирую файл")
                filename = input("Ввидите имя файла, а я его продублирую:")
                duplicate_file(filename)
            elif choice == "6":
                print("Удаление дубликотав в директории")
                dirname = input("Укажити имя директории:")
                count = delet_dupli(dirname)
                print("--Удаление файлов:", count)
            elif choice == "7":
                print("Удаление случайного файла")
                dirname = input("Укажите имя файла")
                random_delete(dirname)
            else:
                pass
        elif answer == "N":
            print("До свидания!")
        else:
            print("Неизвестный ответ")


if __name__ == "__main__":
    main()
