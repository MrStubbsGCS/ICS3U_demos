import random

def task_1():
    print("Hello World!")

def task_2(x):
    print(x*5)

def task_3(data):
    data = data.upper()
    return data

def task_4(num1, num2, num3):
    rand1 = random.randint(2,4)
    rand2 = random.randint(2,4)
    rand3 = random.randint(2,4)

    if num1 == rand1 and num2 == rand2 and num3 == rand3:
        return "You won!"
    else:
        return "You lost! Loser"

text = task_4(2, 3, 4)
