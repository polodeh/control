# name = input("Введите имя: ")
# second_name = input("Введите фамилию: ")
# group = input("Введите номер группы: ")
# print(name + "" + second_name + "" + group + "")

# year = int(input("Введите год: "))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("Ваш год является високосным")
# else:
#     print("Ваш год не является високосным")
import math
def point_to_point(x,y):
    return math.dist(x,y)
count_point = int(input("Введите кол-во точек: "))
array = list()
min = 100000
max = -100000
t_max = list()
t_min = list()
for i in range(2):
    t_max.append(i)
    t_min.append(i)
for i in range(count_point):
    x = list(map(int, input("Введите точку " +str(i) + ": ").split()))
    array.append(x)
for i in range(len(array)):
    for j in range(len(array)):
        dist = point_to_point(array[i], array[j])
        if i == j:
            continue
        if dist > max:
            max = dist
            t_max[0] = array[i]
            t_max[1] = array[j]
        else:
            continue
        if dist < min:
            min = dist
            t_min[0] = array[i]
            t_min[1] = array[j]
        else:
            continue

print("Минимальное расстояние между точками" + str(t_min[0]) + str(t_min[1]) + " = " + str(min))
print("Максимальное расстояние между точками" + str(t_max[0]) + str(t_max[1]) + " = " + str(max))











