a = int(input("Введите число: "))
sum_matrix = 0
sum_end = 0
leen = len(str(a)) - 1
d = 1
for i in range(leen):
    d *= 10


for i in range(len(str(a))):
    s = str(a)
    a = int(str(a // 10) + str(a % d))
    sum_matrix += a
    print("a =  ",a)

print("Сумма чисел:")
print(sum_matrix)

print("Сумма Цифр:")
sum_end = sum(map(int, str(sum_matrix)))
print(sum_end)