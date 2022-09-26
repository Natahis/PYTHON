# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# print(list(range(1,6))) #- [1,2,3,4,5]
# print(list(range(0,10,2))) #-[0,2,4,6,8] 

# list(range(-3,3))
# for i in range(0,10,2):
#     print(i, end=" ")
# print()


a=int(input())
print(list(range(-a,a+1)))