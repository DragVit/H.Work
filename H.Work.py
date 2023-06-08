# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#*Пример:*
#A = 3; B = 5 -> 243 (3⁵)   A = 2; B = 3 -> 8 
def degree_of_number(number, power):
    if number < 0:
        return 1, print("Неверное число!")
    if power == 0:
        return 1, print("Неверное число!")
    if power < 0:
        return 1, print("Неверное число!")
    if power > 0:
        return number * degree_of_number(number, power -1)

NumberToDegree = int()
power = int()

print("Введите число: ")
NumberToDegree = int(input())
print("Введите степень: ")
power = int(input())

degree_of_number = degree_of_number(NumberToDegree, power)
print(f"number {NumberToDegree}, power {power}, result: {degree_of_number}")

