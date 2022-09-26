#  Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
mx = max(a,b,c,d,e)
print(mx)

# a,b,c,d,e = int(input()), int(input()), int(input()), int(input()), int(input())
# print(max(list([a,b,c,d,e])))

# number_list = list(map(int, input().split()))
# print(max(number_list) )
