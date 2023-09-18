# Вывести последнюю букву в слове
word = 'Архангельск'

#Цикл по переменной
for i in word:
    if word.index(i)==len(word)-1:
        print(f'Последняя буква в слове {word}: {i}') 



# Вывести количество букв "а" в слове
word = 'Архангельск'
cnt_a = 0

#Цикл по переменной
for i in word:
    if i=='а':
       cnt_a = cnt_a + 1
print(f'Количество букв "а" в слове {word}: {cnt_a}') 



# Вывести количество гласных букв в слове
word = 'Архангельск'
cnt_l = 0
str_cnt = 'Количество гласных букв в слове'


#Решаем через список
wrd_vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

#Цикл по переменной
for i in word:
    for iw in wrd_vowel:
        if i.lower()==iw:
           cnt_l = cnt_l + 1
print(f'{str_cnt} {word} {cnt_l}')            


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

#Используем функцию Split
cnt_wrd = len(sentence.split(' '))
print(f'Количество слов в предложении ""{sentence}"" равно: {cnt_wrd}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

#Используем функцию Split и цикл
cnt_wrd = sentence.split(' ')
for i in cnt_wrd:
    for iw in i:
        if i.index(iw) == 0:
            print(iw)
    



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sum_len = 0
cnt_l = 0

#Получаем список слов
wrd_snt = sentence.split(' ')

#Как всегда цикл
for i in wrd_snt:
    sum_len = sum_len + len(i)
    cnt_l = cnt_l + 1

print(f'Усредненная длина слова в предложении = {int(sum_len/cnt_l)}')
