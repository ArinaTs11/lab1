#Задание 9. Найти периметр и площадь прямоугольника
# по координатам двух противоположных вершин.

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

width = abs(x2 - x1)
height = abs(y2 - y1)

perimeter = 2 * (width + height)
area = width * height

print("Периметр прямоугольника:", perimeter)
print("Площадь прямоугольника:", area)