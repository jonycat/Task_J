a = input("Введите число: ")
sum_matrix = 0
sum_end = 0

for i in range(len(a)):
    s = str(a)
    b = a = str(s[-1] + s[0:-1])
    b = int(b)
    sum_matrix += b

sum_end = sum(map(int, str(sum_matrix)))
print(sum_end)