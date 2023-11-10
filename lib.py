#Створіть файл lib.py, помістіть в нього допоміжні функції вашої програми "Касир". Імпортуйте їх для основної функції
# в основний файл. Запустіть "Касир" з основного файл
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
#Помістіть в lib.py декоратор для вимірювання часу. Імпортуйте декоратор в основний файл, задекоруйте основну функцію "Касир".
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper