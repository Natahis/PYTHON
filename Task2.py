# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.         
#   *Пример:*          - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} 


# num = input('Введите положительное целое число n: ')
# result = []
# for i in range(1, int(num)+1):
#     element = [i, 3*i + 1]
#     result.append(element)
# print(dict(result))


num = input('Введите положительное целое число n: ')
result = dict()
for i in range(1, int(num)+1):
    result[i] = 3*i + 1
print(result)

