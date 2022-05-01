# HW7

import random
def get_number(age):
    """

    :return:
    """

    age = input()
    return
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
    elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        res = 'роки'
    elif age % 10 == 5 or age % 10 == 6 or age % 10 == 7 or age % 10 == 8 or age % 10 == 9 or age == exc or age % 10 == 0:
        res = 'років'
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
    if age < 7:
        print(f'Тобі ж {age} {year}! Де твої батьки?')
    elif age < 16:
        print(f'Тобі лише {age} {year}, а це е фільм для дорослих!')
    elif age > 65:
        print(f'Вам {age} {year}? Покажіть пенсійне посвідчення!')
    elif len(set(repdigit)) != len(repdigit):
        print(f'О вам {age} {year}! Який цікавий вік')
    else:
        print(f'Незважаючи на те, що вам {age} {year}, білетів всеодно нема!')

result = age_control(age)


