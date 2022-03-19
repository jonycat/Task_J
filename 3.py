a = input("Введите число: ")
sum_matrix = 0
sum_end = 0

for i in range(len(a)):
    s = str(a)
    print(s[0])
    a = str(s[-1] + s[0:-1])
    a = int(a)
    sum_matrix += a
    print(a)

print("Сумма чисел:")
print(sum_matrix)

print("Сумма Цифр:")
sum_end = sum(map(int, str(sum_matrix)))
print(sum_end)