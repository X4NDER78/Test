# HW7

age = int(input('Введіть свій рік ->'))
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
         x: int

    Returns:GIVES BACK AGE , IF IT COINCIDED WITH NUM AT LIST
    """

    while (age not in except_list):
        print("Age = ", age)
        age = random.randrange(0, 1999)

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
    elif age % 10 == 5 or age % 10 == 6 or age % 10 == 7 or age % 10 == 8 or age % 10 == 9 or age == exc:
        res = 'років'

    return res

repdigit = digits(age)
year = form_of_age(age)

if len(set(repdigit)) != len(repdigit):
    print(f'О вам {age} {year}! Який цікавий вік')
else:
    print(f'Незважаючи на те, що вам {age} {year}, білетів всеодно нема!')




