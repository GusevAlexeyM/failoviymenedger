import os
import shutil

nachdir = os.getcwd() # текущая директория

def pwd(): # текущая директория 0
    print(f'текущая директория: {os.getcwd()}' + '\n')

def mkdir(): # новая папка 1
    a = input('введите название новой папки, если хотите создать ее в текущем каталоге, либо путь к ней: ')
    if not (nachdir in a) and (a.count('\\') != 0 or a.count('/') != 0):
        print(f'ошибка: вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        try:
            os.mkdir(a)
            print(f'директория {a} создана' + '\n')
        except FileExistsError:
            print('создаваемая директория или файл уже существует' + '\n')


def rmdir(): # удаление директории 2
    a = input('введите название или путь удаляемой директории: ')
    if not (nachdir in a) and (a.count('\\') != 0 or a.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        try:
            os.rmdir(a)
            print(f'Директория {a} удалена' + '\n')
        except FileNotFoundError:
            print('Удаляемая директория или файл не найден' + '\n')


def cd(): # перемещение 3
    a = input("введите путь к директории или '..' если хотите подняться на папку выше: ")
    if a == '..' and os.getcwd() == nachdir:
        print('нельзя подняться выше рабочей директории' + '\n')
    else:
        try:
            os.chdir(a)
        except FileNotFoundError:
            print('Путь не найден' + '\n')


def cr_file(): # создание пустого файла 4
    a = input('введите название нового файла (или путь к файлу): ')
    if not (nachdir in a) and (a.count('\\') != 0 or a.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        try:
            f = open(a, 'w')
            f.close()
            print(f'файл {a} создан' + '\n')
        except FileExistsError:
            print('создаваемый файл уже есть' + '\n')


def wr_file(): # запись текста в файл 5
    a = input('введите название файла (или путь к файлу), в который нужно записать текст (если файла нет, то он будет создан): ')
    data = input('введите текст для записи (запись осуществляется с новой строки), затем нажмите ENTER: ')
    if not (nachdir in a) and (a.count('\\') != 0 or a.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        f = open(a, 'a')
        f.write(f"{data}" + '\n' + '\n')
        f.close()


def cat(): # просммотр файла 6
    a = input('введите название файла (или путь к файлу) для просмотра содержимого: ')
    if not (nachdir in a) and (a.count('\\') != 0 or a.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        try:
            f = open(a, 'r')
            for line in f:
                print(line[:-1])
            f.close()
        except FileNotFoundError:
            print('такого файла нет')


def removefile(): # удаление файла по имени 7
    a = input('введите название файла (или путь к файлу) для удаления: ')
    if not (nachdir in a) and (a.count('\\') != 0 or a.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        try:
            os.remove(a)
            print(f'файл {a} удален' + '\n')
        except FileNotFoundError:
            print('такого файла нет')


def copyfile(): # копирование файла 8
    old = input('введите название файла С РАСШИРЕНИЕМ TXT (или путь к файлу) для копирования: ')
    if not (nachdir in old) and (old.count('\\') != 0 or old.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        new = input('введите новый путь: ')
        if not (nachdir in new) and (new.count('\\') != 0 or new.count('/') != 0):
            print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
        else:
            try:
                shutil.copy(old, new)
            except FileNotFoundError:
                print('такого файла нет')
                
                
def movefile(): # перемещение файла 9
    old = input('введите название файла (или путь к файлу) для перемещения: ')
    if not (nachdir in old) and (old.count('\\') != 0 or old.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        new = input('введите новый путь: ')
        if not (nachdir in new) and (new.count('\\') != 0 or new.count('/') != 0):
            print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
        else:
            try:
                shutil.move(old, new)
            except FileNotFoundError:
                print('такого файла нет')

                
def renamefile(): # переименовывание файла 10
    old = input('введите название файла (или путь к файлу) для переименнования: ')
    if not (nachdir in old) and (old.count('\\') != 0 or old.count('/') != 0):
        print(f'вы пытаетесь выйти за рабочую директорию. Рабочая директория: {nachdir}' + '\n')
    else:
        new = input('введите новое название для переименнования (БЕЗ УКАЗАНИЯ ПУТИ К ФАЙЛУ): ')
        if (new.count('\\') != 0) or (new.count('/') != 0):
            print('вы ввели путь к новому файлу. Введите новое название' + '\n')
        else:
            try:
                os.rename(old, new)
                print(f'файл `{old}` переименован в `{new}`' + '\n')
            except FileNotFoundError:
                print('такого файла нет')


def main():
    dop = ''    
    print('\n' + f'ВАША ДОМАШНЯЯ ДИРЕКТОРИЯ: {os.getcwd()}. НЕЛЬЗЯ ВЫХОДИТЬ ВЫШЕ ДОМАШНЕЙ ДИРЕКТОРИИ.' + '\n')
    while True:
        print('----------------------------------------------------------------')        
        print('0. Вывести текущую директорию.')
        print('1. Создать папку.')
        print('2. Удалить папку.')
        print('3. Переместиться в другую папку или подняться на уровень выше.')
        print('4. Создание пустого файла.')
        print('5. Запись текста в файл.')
        print('6. Просмотр содержимого файла.')
        print('7. Удаление файла по имени.')
        print('8. Копирование файла.')
        print('9. Перемещение файла.')
        print('10. Переименование файла.')
        print('ВВЕДИТЕ 300 ДЛЯ ЗАВЕРШЕНИЯ РАБОТЫ ПРОГРАММЫ.')
        dop = input('ВЫБЕРИТЕ ДЕЙСТВИЕ: ')
        print('')

        if dop == '0':
            pwd()

        elif dop == '1':
            mkdir()

        elif dop == '2':
            rmdir()

        elif dop == '3':
            cd()

        elif dop == '4':
            cr_file()

        elif dop == '5':
            wr_file()

        elif dop == '6':
            cat()

        elif dop == '7':
            removefile()

        elif dop == '8':
            copyfile()

        elif dop == '9':
            movefile()

        elif dop == '10':
            renamefile()

        elif dop == '300':
            print('РАБОТА ЗАВЕРШЕНА')
            break

        else:
            print('вы выбрали несуществующий пункт меню, повторите ввод' + '\n')


main()
