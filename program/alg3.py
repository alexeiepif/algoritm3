import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import timeit


def find(a, b, len):
    for i in range(len):
        if b == a[i]:
            return i
    return -1


def create_graph(b, c, aur, bur):
    y_values = np.linspace(0, max(c), num=5)
    x_values = np.linspace(0, b[-1], num=11)
    plt.scatter(b, c, s=5)

    y_line = aur * x_values + bur
    plt.plot(x_values, y_line, color='red')

    plt.title("График")
    plt.xlabel("X-ось")
    plt.ylabel("Y-ось")
    plt.xticks(x_values)
    plt.yticks(y_values)

#Цикл нужен для создания двух графиков, один при среднем случае, второй при худшем
for iter in [1, 2]:
    x = []
    time = []
    x2 = []
    xtime = []
    for i in range(10, 1001, 10):
        x.append(i)
        a = [rnd.randint(1, 100) for j in range(i)]
        if iter == 1:
            b = a[rnd.randint(1, len(a))]
        else:
            b = 101
        timer = timeit.timeit(lambda: find(a, b, i), number=1)
        time.append(timer)
        index = find(a, b, i)
        if index != -1:
            print("№", i, "С числом b = ", b,
                  " совпал элемент с индексом ", index, "Время = ", timer)
        else:
            print("№", i, "С числом b = ", b,
                  " не совпал ни один элемент. Время = ", timer)

    for i, j in zip(x, time):
        x2.append(i**2)
        xtime.append(i*j)
    # Вычисление коэффицентов в системе уравнений метода наименьших квадратов
    sx = sum(x)
    stime = sum(time)
    sx2 = sum(x2)
    sxtime = sum(xtime)
    n = len(x)
    # Начало вычислений коэффицентов прямой, 
    # k - это такой коэффицент, при вычитании второго уравнения, 
    # умноженного на него, из первого уравнения, коэффицент при x исчезает, 
    # и мы находим свободный коэффицент
    k = sx2/sx
    #bur - это свободный коэффицент
    bur = (sxtime - k*stime)/(sx-k*n)
    #aur - это коэффицент при x
    aur = (stime - bur*n)/sx
    #Создание графических окон
    plt.figure(iter)
    #Создание графиков
    create_graph(x, time, aur, bur)
#Показ графиков
plt.show()
