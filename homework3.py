#Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
text = input("Введіть слово")
print (" Третій символ в слові ",(text),text[3])


#Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код,
# який визначить кількість слів, в цих даних.
sentence= input("Введіть текс: ")
word_count = sentence.count(" ") + 1
print("Кількість слів :", word_count)

#Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# . Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1
# . Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до за
my_list = [1,'Phyton',9,7,3,6,9.3]
print([x for x in my_list if isinstance(x, (int, float))])






