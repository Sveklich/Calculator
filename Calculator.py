import math

operator = input("Введите оператор (+, -, *, /, **, sqrt, !, sin, cos, tg): ")
if operator == "sqrt" or operator == "!" or operator == "sin" or operator == "cos" or operator == "tg":
    try:
        num1 = float(input("Введите число: "))
    except:
        print("Ошибка: Введённое значение не является числом!")
else:
    try:
        num1 = float(input("Введите первое число: "))
    except:
        print("Ошибка: Введённое значение не является числом!")
    try:
        num2 = float(input("Введите второе число: "))
    except:
        print("Ошибка: Введённое значение не является числом!")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "**":
    result = num1 ** num2
elif operator == "/":
    if num2 == 0:
        print("Ошибка: деление на ноль!")
        exit()
    else:
        result = num1 / num2
elif operator == "sqrt":
    if num1 < 0:
        print("Ошибка: Квадратного корня из отрицательного числа быть не может!")
        exit()
    else:
        result = math.sqrt(num1)
elif operator == "!":
    if num1 < 0:
        print("Ошибка: Факториал отрицательного числа быть не может!")
    else:
        result = math.factorial(num1)
elif operator == "sin":
    result = math.sin(math.radians(num1))
elif operator == "cos":
    result = math.cos(math.radians(num1))
elif operator == "tg":
    result = math.tan(math.radians(num1))
else:
    print("Ошибка: неверный оператор!")
    exit()

print("Результат:", result)