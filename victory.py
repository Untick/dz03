# (МОДУЛЬ 4) Задание
# Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими
# библиотеками кроме random)
# Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока
# использовать строку
# Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
# После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
# пользователь вводит дату в формате 'dd.mm.yyyy'
# Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
# третье января 2009 года, склонением можно пренебречь
# В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

import random2

names_dict = {'Пушкин А.С.': '26.05.1799',
              'Толстой Л.Н': '28.08.1828',
              'Достоевский Ф.М.': '30.10.1821',
              'Чехов А.П.': '17.01.1860',
              'Гагарин Ю.А.': '09.03.1934',
              'Королёв С.П.': '30.12.1906',
              'Гоголь Н.В': '20.03.1809',
              'Тургенев И.С': '09.11.1818',
              'Яшин Л.И.': '22.10.1929',
              'Высоцкий В.С.': '25.01.1938'
             }
correct_answs = {'26.05.1799': 'Двадцать шестое мая 1799 года',
                 '28.08.1828': 'Двадцать восьмое августа 1828 года',
                 '30.10.1821': 'Тридцатое октября 1821 года',
                 '17.01.1860': 'Семнадцатое января 1860 года',
                 '09.03.1934': 'Девятое марта 1934 года',
                 '30.12.1906': 'Тридцатое декабря 1906 года',
                 '20.03.1809': 'Двадцатое марта 1809 года',
                 '09.11.1818': 'Девятое ноября 1818 года',
                 '22.10.1929': 'Двадцать второе октября 1929 года',
                 '25.01.1938': 'Двадцать пятое января 1938 года'
                }
print('Добро пожаловать в викторину!')
rerun = 'да'
while rerun == 'да':
    random_choice = dict(random2.sample(names_dict.items(), 5))
    score = 0
    fail = 0

    for i, j in random_choice.items():
        print('Введите день рождения в формате dd.mm.yyyy', i,': ')
        answer = str(input())
        if answer == j:
            print('Правильно!')
            score += 1
        else:
            print('Неверно, правильный ответ: ', correct_answs.get(j))
            fail += 1

    print('Спасибо за участие в викторине! Ваш счёт', score, 'очка(о, ов)!','Вы дали', fail, 'неверный(х) ответ(ов).')
    rerun = input('Начать заново? (да/нет)')