#Створіть файл lib.py, помістіть в нього допоміжні функції вашої програми "Касир". Імпортуйте їх для основної функції
# в основний файл. Запустіть "Касир" з основного файл
from lib import check_age

user_age = int(input("Введіть ваш вік: "))
result = check_age(user_age)
print(result)
#Помістіть в lib.py декоратор для вимірювання часу. Імпортуйте декоратор в основний файл, задекоруйте основну функцію "Касир".
from lib import timer
@timer
def check_age(age):
    if age < 7:
        return f"Тобі ж {age} рік! Де твої батьки?"
    elif age < 16:
        return f"Тобі лише {age} роки, а це е фільм для дорослих!"
    elif age > 65:
        return f"Вам {age} років? Покажіть пенсійне посвідчення!"
    elif "7" in str(age):
        return f"Вам {age} років, вам пощастить!"
    else:
        return f"Незважаючи на те, що вам {age} років, білетів всеодно нема!"

user_age = int(input("Введіть ваш вік: "))
result = check_age(user_age)
print(result)