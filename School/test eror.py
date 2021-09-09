while 1:
    try:
        x = int(input("Введите, пожалуйста, целое число: "))
        break
    except ValueError:
        print ("Вы ошиблись. Попробуйте еще раз...")