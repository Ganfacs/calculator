
import math

doc = ("1.Калькулятор", "2.Дискриминант",  "3.П(Число Пи)", "4.Перевод чисел", "5.Факториал", "6.Вероятность", "7.Выход")
doc2 = ('1.Двоичную: Чиать после буквы x', '2.Шеснадцатиричную: Читать после буквы b', '3.Десятичную: Читать как обычно(только из двоичной системы)',)
f = True
class Glob:
    def discriminant(self):
        f = True
        while f == True:
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            c = float(input("Введите c: "))
            D = (b*b)-4*a*c
            print('Дискриминант равен: ', D)
            if D >= 0:
                x1 = (- b + math.sqrt(D)) / 2 * a
                x2 = (- b - math.sqrt(D))/2*a
                print('x1=', x1)
                print('x2=', x2)
            elif D < 0:
                print('Я не знал как реализовать комплексные числа в питоне, так что решай сам, а моя программа будет считать что корней нет')
            enter = str(input('Вы хотите выйти? '))
            if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                break
            elif enter == 'Нет' or enter == 'нет' or enter == 'No' or enter == 'no' or enter == 'Not' or enter == 'not':
                continue
        
    def calculator(self):
        f = True
        while f == True:
            a = ['+', '-', '/', '*']
            num1 = float(input('Введите первое число: '))
            n = input('Введите знак:')
            num2 = float(input('Введите второе число: '))
            if n == a[0]:
                c = num1 + num2
                print(c)
            elif n == a[1]:
                c = num1 - num2
                print(c)
            elif n == a[2]:
                c = num1 / num2
                print(c)
            elif n == a[3]:
                c = num1 * num2
                print(c)
            enter = input('Вы хотите выйти? ')
            if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                break
            elif enter == 'Нет' or enter == 'нет' or enter == 'No' or enter == 'no' or enter == 'Not' or enter == 'not':
                continue


    def binary_system(self):
        f = True
        try:
            while f:
                e = int(input('Введите число: '))
                g = bin(e)
                print(g)
                enter = input('Вы хотите выйти? ')
                if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                    break
                    enter = input('Вы хотите выйти на главную? ')
                    if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                        return
                elif enter == 'Нет' or enter == 'нет' or enter == 'No' or enter == 'no' or enter == 'Not' or enter == 'not':
                    continue
        except TypeError:
            print('Произошла ошибка')
        else:
            print('no')
    def hexadecimal_system(self):
        f = True
        while f:
            e = int(input('Введите число: '))
            print(hex(e))
            enter = input('Вы хотите выйти? ')
            if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                break
                enter = input('Вы хотите выйти на главную? ')
                if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                    return
            elif enter == 'Нет' or enter == 'нет' or enter == 'No' or enter == 'no' or enter == 'Not' or enter == 'not':
                continue
    def decimal_system(self):
        f = True
        while f:
            enter = input('Введите число: ')
            print(int(enter, 2))
            enter = input('Вы хотите выйти? ')
            if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                break
                enter = input('Вы хотите выйти на главную? ')
                if enter == 'Да' or enter == 'да' or enter == 'yes' or enter == 'Yes':
                    return
            elif enter == 'Нет' or enter == 'нет' or enter == 'No' or enter == 'no' or enter == 'Not' or enter == 'not':
                continue
    def probability(self):
        f = True
        while f:
            m = float(input('Введите число благоприятных событий: '))
            n = float(input('Введите число всех событий: '))
            p = m/n
            print('P = ', p)
            enter = input('Вы хотите выйти?: ')
            if enter == 'yes' or enter == 'Yes' or enter == 'Да' or enter == 'да':
                return
            elif enter == 'not' or enter == 'Not' or enter == 'Нет' or enter == 'нет':
                continue

            
c = Glob()
while f:
    enter = str(input('Введите команду: '))
    if enter == 'Калькулятор' or enter == '1':
        c.calculator()
    elif enter == 'Дискриминант' or enter == '2':
        c.discriminant()
    elif enter == 'help' or enter == 'Help' or enter == 'Помощь' or enter == 'помощь':
        for i in doc:
            print(i)
    elif enter == 'Выход' or enter == '7':
        break
    elif enter == 'П' or enter == '3':
        math.pi
        print(math.pi)
    if enter == 'Перевод чисел' or enter == '4':
   
        while f:
            vibor = str(input('В какую систему вы хотите перевести число?: '))
            if vibor == "help":
                for i in doc2:
                    print(i)
            elif vibor == 'Двоичную' or vibor == '1':
                c.binary_system()

            elif vibor == 'Шеснадцатиричную' or vibor == '2':
                c.hexadecimal_system()

            elif vibor == 'Десятичную' or vibor == '3':
                c.decimal_system()
                    
            enter = input('Вы хотите выйти на главную? ')
            if enter == 'Да' or enter == 'Yes' or enter == 'yes' or enter == 'да':
                break
            elif enter == 'Нет' or enter == 'No' or enter == 'no' or enter == 'нет':
                continue
            
    if enter == 'Факториал' or enter == '5':
        while f:
            enter = int(input('Введите число: '))
            print('Факториал равен: ', math.factorial(enter))
            enter = input('Вы хотите выйти? ')
            if enter == 'Да' or enter == 'Yes' or enter == 'yes' or enter == 'да':
                break
            elif enter == 'Нет' or enter == 'нет' or enter == 'No' or enter == 'no' or enter == 'Not' or enter == 'not':
                continue
    elif enter == 'Вероятность' or enter == '6':
        c.probability()

    
