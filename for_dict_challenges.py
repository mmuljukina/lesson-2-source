# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

dict_stud={} # для заполнения посчитанными студентами 

for il in range(len(students)):                              # внешний цикл по списку
    cnt_s = 1
    for key_ext, val_ext in students[il].items():            # анализируем словарь
        iwh = il + 1
    while iwh <= len(students)-1:                            # цикл по списку дальше для поиска дубликатов значений из словаря
        for key_in, val_in in students[iwh].items():
            if val_ext == val_in:
                cnt_s = cnt_s + 1
        iwh = iwh + 1 

    # Производим анализ есть ли, уже ключ-Имя в посчитанном словаре, если нет, то заполняем словарь
    if dict_stud.get(val_ext) == None: dict_stud[val_ext] = cnt_s

    # Выводим полученный словарь на печать
for key, val in dict_stud.items(): 
    print(key,':' , val)   



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

cnt_max = 0      # для получения максимального повторения имен 
name_s_max = ''  # для получения частого имени

for il in range(len(students)):                              # внешний цикл по списку
    cnt_s = 1
    for key_ext, val_ext in students[il].items():            # анализируем словарь
        iwh = il + 1
    while iwh <= len(students)-1:                            # цикл по списку дальше для поиска дубликатов значений из словаря
        for key_in, val_in in students[iwh].items():
            if val_ext == val_in:
                cnt_s = cnt_s + 1
        iwh = iwh + 1 

    # Анализирум максимально встречаемые имена
    if cnt_max <= cnt_s: 
        cnt_max = cnt_s
        name_s_max = val_ext

    # Выводим результат
print(name_s_max)


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

