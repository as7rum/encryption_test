import pyAesCrypt
import os
import sys
from directory import DIRECTORY

#функция шифрования файла
def decryption (file, password):
    
    #Задаем размер буффера (с его помощью зашифровывается и расшифровывается файл) 
    buffer_size = 512 * 1024

    #Вызываем метод дешифровки из pyAesCrypt
    pyAesCrypt.decryptFile(
        str(file), #файл
        str(os.path.splitext(file)[0]),
        password, #пароль
        buffer_size #собственно сам буффер
        )

    #Чтобы видеть результат выведем на экран имя расшифрованного файла
    print ('Файл: ' + str(os.path.splitext(file)[0]) + 'расшифрован')

    #Удаляем файл
    os.remove(file)

#Функция сканирования директории
def walking_by_dirs(dir, password):
    
    #перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #если мы нашли файл, то расшифровываем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print (ex)
        #Если находим директорию, то повторяем функцию в поисках файлов
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль")
walking_by_dirs(DIRECTORY, password) 

#os.remove(str(sys.argv[0]))