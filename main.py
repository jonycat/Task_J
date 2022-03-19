import timeit
code_to_test = '''
a = input("Введите число: ")
sum_matrix = 0
sum_end = 0

for i in range(len(a)):
    s = str(a)
    print(s[0])
    b = a = str(s[-1] + s[0:-1])
    b = int(b)
    sum_matrix += b
    print(a)

print("Сумма чисел:")
print(sum_matrix)

print("Сумма Цифр:")
sum_end = sum(map(int, str(sum_matrix)))
print(sum_end)
'''

elapsed_time = timeit.timeit(code_to_test, number=1)/100
print('____________________')
print(elapsed_time)