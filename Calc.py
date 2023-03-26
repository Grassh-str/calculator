def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


num_1 = input("Введите первое число: ")

type_float_num_1 = is_number(num_1)
type_int_num_1 = str.isnumeric(num_1)

while not type_float_num_1:
    num_1 = input("Введите корректное цисло: ")
    type_float_num_1 = is_number(num_1)
    type_int_num_1 = str.isnumeric(num_1)

arif_znak = input("Введите арифметический знак (+, -, *, /): ")

if arif_znak == '+':
    arif_znak_bool = True
elif arif_znak == '-':
    arif_znak_bool = True
elif arif_znak == '*':
    arif_znak_bool = True
elif arif_znak == '/':
    arif_znak_bool = True
else:
    arif_znak_bool = False

while not arif_znak_bool:
    arif_znak = input("Введите корректный арифметический знак (+, -, *, /): ")

    if arif_znak == '+':
        arif_znak_bool = True
    elif arif_znak == '-':
        arif_znak_bool = True
    elif arif_znak == '*':
        arif_znak_bool = True
    elif arif_znak == '/':
        arif_znak_bool = True
    else:
        arif_znak_bool = False

num_2 = input("Введите второе число: ")

type_float_num_2 = is_number(num_2)
type_int_num_2 = str.isnumeric(num_2)

while not type_float_num_2:
    num_2 = input("Введите корректное цисло: ")
    type_float_num_2 = is_number(num_2)
    type_int_num_2 = str.isnumeric(num_2)

if not type_int_num_1:
    num_1 = float(num_1)
else:
    num_1 = int(num_1)

if not type_int_num_2:
    num_2 = float(num_2)
else:
    num_2 = int(num_2)

if arif_znak == '+':
    result = num_1 + num_2
elif arif_znak == '-':
    result = num_1 - num_2
elif arif_znak == '*':
    result = num_1 * num_2
elif arif_znak == '/':
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        result = 0
        print("На 0 делить нельзя")

print("Результат: " + str(result))