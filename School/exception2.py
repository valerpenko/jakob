import os
while True:
    try:
        #path="/home/yakov/Рабочий стол/jakob-master/jakob/Schooд"
        path=input()
        for name in os.listdir(path): # вывод файлов текущего каталога построчно
            path = os.path.join(path, name)
            if name[-3:]=='.py':
                print(name)
        break
    except :
        print("введите правельное имя каталога")