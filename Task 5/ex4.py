x = int(input("В первый день: "))
y = int(input("Цель: "))

def func():
    result = 0
    currentDistance = x

    while currentDistance < y:
        result += 1
        currentDistance *= 1.1

    return f"Дней: {result}"

print(func())