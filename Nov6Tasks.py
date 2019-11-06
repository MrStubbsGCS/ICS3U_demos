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

def task_5(li, num):
    i = 0
    while len(li)> i: #for i in range(len(li)):
        if li[i] > num:
            del li[i] #li.remove(li[i])
            i = i -1
        i = i+1
    return li

ex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(task_5(ex_list, 4))
