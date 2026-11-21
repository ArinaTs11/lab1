# Задание 10. Найти периметр и площадь треугольника
# по координатам его вершин.

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

ab = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
bc = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
ca = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

perimeter = ab + bc + ca

area = abs(
    x1 * (y2 - y3) +
    x2 * (y3 - y1) +
    x3 * (y1 - y2)
) / 2

print("Периметр треугольника:", round(perimeter, 2))
print("Площадь треугольника:", round(area, 2))