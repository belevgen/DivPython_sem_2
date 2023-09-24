# Задание 2
# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей.
# Для проверки своего кода используйте модуль fractions.

fraction1 = input("Введите первую дробь в формате a/b: ")  # Ввод двух дробей от пользователя
fraction2 = input("Введите вторую дробь в формате a/b: ")

def gcd(a, b):                                    # Функция для вычисления наибольшего общего делителя (НОД)
    while b:
        a, b = b, a % b
    return a

def add_fractions(frac1, frac2):                    # Функция для сложения двух дробей
    num1, den1 = map(int, frac1.split('/'))
    num2, den2 = map(int, frac2.split('/'))

    common_denominator = den1 * den2 // gcd(den1, den2)  # Находим общий знаменатель для сложения

    sum_numer = num1 * (common_denominator // den1) + num2 * (common_denominator // den2) # Вычисляем числитель для суммы

    common_divisor = gcd(sum_numer, common_denominator)  # Сокращаем дробь
    sum_numer //= common_divisor
    common_denominator //= common_divisor

    return f"{sum_numer}/{common_denominator}"

def multiply_fractions(frac1, frac2):                       # Функция для умножения двух дробей
    num1, den1 = map(int, frac1.split('/'))
    num2, den2 = map(int, frac2.split('/'))

    product_numer = num1 * num2                              # Умножаем числители и знаменатели
    product_denominator = den1 * den2

    common_divisor = gcd(product_numer, product_denominator)  # Сокращаем дробь
    product_numer //= common_divisor
    product_denominator //= common_divisor

    return f"{product_numer}/{product_denominator}"

sum_result = add_fractions(fraction1, fraction2)               # Вычисляем и выводим сумму и произведение дробей
product_result = multiply_fractions(fraction1, fraction2)

print(f"Сумма: {sum_result}")
print(f"Произведение: {product_result}")
