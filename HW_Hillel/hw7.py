# HW7

import random
def get_number():
    while True:
        try:
            return int(input('Введіть свій вік -> '))
        except Exception as e:
            print('Це не може бути ваш вік')

age = get_number()
def digits(age):
    """
    FUNCTION FIND NUMBERS WITH THE SAME NUMERIC
    Args:
        age (int):

    Returns: LIST WITH THE SAME NUM
    """

    return [int(c) for c in str(age)][::-1]

except_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def compair_except_with_list(age):
    """
    FUNCTION COMPAIR ARG(AGE) WITH EXCEPTION LIST
    Args:
         age: int

    Returns:GIVES BACK AGE , IF IT COINCIDED WITH NUM AT LIST
    """

    while (age not in except_list):
        age = random.randrange(0, 130)

    return age

exc = compair_except_with_list(age)

def form_of_age(age):
    """
    FUNCTION COMPAIR ARG(AGE) WITH RULES OF CINEMA
    Args:
        age: int

    Returns:GIVES BACK CORRECT FORM OF YEAR
    """

    if age % 10 == 1 and age != 11:
        res = 'рік'
    elif age % 10 == 5 or age % 10 == 6 or age % 10 == 7 or age % 10 == 8 or age % 10 == 9 or age == exc or age % 10 == 0:
        res = 'років'
    elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        res = 'роки'
    else:
        print('На жаль , я не можу вам допомгти')
    return res

repdigit = digits(age)
year = form_of_age(age)

def age_control(age):
    """
    FUNCTION DEFENITION AGE OF PERSON
    Args:
        age: int

    Returns:CORRECT ANSWER THAT DEPENDS ON THE AGE
    """
    if len(set(repdigit)) != len(repdigit):
        print(f'О вам {age} {year}! Який цікавий вік')
    if age == 0:
        print('Ти маєшь бути в іншему місці')
    elif age < 7 and age != 0:
        print(f'Тобі ж {age} {year}! Де твої батьки?')
    elif age < 16 and age != 0 and age != 11:
        print(f'Тобі лише {age} {year}, а це е фільм для дорослих!')
    elif age > 65 and age != 0 and age < 130 and age != 66 and age != 77 and age != 88 and age != 99 and age != 111:
        print(f'Вам {age} {year}? Покажіть пенсійне посвідчення!')

result = age_control(age)


