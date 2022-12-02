from random import randint
D=int(input("Сортировка по возрастанию - 1\n"
        "Сортировка по убыванию - 2\n"))

N = int(input("Ввдите количство чисел\n"))
a = []
for i in range(N):
    a.append(randint(1, N))
print(a)

if D==1:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)

else:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)