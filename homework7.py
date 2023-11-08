#Доопрацюйте гру з занятя наступним чином:

#додайте підказки для користувача.
#якщо різниця між числами 1-2 - "Гаряче"
#якщо різниця між числами 3-5 - "Тепло"
#якщо різниця між числами 6 і більше- "Холодно"
#додайте лічильник спроб вгадати. користувач повинен вгадати число за фіксовану кількість спроб
# (визначіть кількість спроб самостійно). якщо він не вгадав за фіксовану кількість спроб - гра завершується
# з відповідним повідомленням
from random import randint

def get_user_number(prompt='Enter number', lower_limit=None, upper_limit=None):
    while True:
        try:
            res = int(input(f'{prompt} (int number): '))
        except Exception:
            print('Wrong input!')
        else:
            if lower_limit is not None:
                if res < lower_limit:
                    print(f'Number should be bigger than {lower_limit}!')
                    continue
            if upper_limit is not None:
                if res > upper_limit:
                    print(f'Number should be less than {upper_limit}!')
                    continue
            return res

def get_comp_number(lower_limit, upper_limit):
    res = randint(lower_limit, upper_limit)
    return res

def compare_numbers(comp_number, user_number):
    difference = abs(comp_number - user_number)
    if difference <= 2:
        print('Гаряче')
    elif difference <= 5:
        print('Тепло')
    else:
        print('Холодно')

def game_guess_number():
    lower_limit = 0
    upper_limit = 9
    max_attempts = 6
    attempts = 0

    comp_number = get_comp_number(lower_limit, upper_limit)

    while attempts < max_attempts:
        attempts += 1

        user_number = get_user_number(f'Guess the number [{lower_limit}-{upper_limit}]', lower_limit, upper_limit)

        if user_number == comp_number:
            print('Вітаємо! Ви вгадали номер')
            break
        else:
            print('Спробуйте ще!')

        compare_numbers(comp_number, user_number)

    if attempts == max_attempts:
        print('Нажаль ви програли ,спробуйте іншим разом')

game_guess_number()