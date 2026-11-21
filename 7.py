# Задание 7. Найти длины отрезков AC и BC и их сумму.

a = float(input("Введите координату точки A: "))
b = float(input("Введите координату точки B: "))
c = float(input("Введите координату точки C: "))

ac = abs(c - a)
bc = abs(c - b)

print("Длина AC:", ac)
print("Длина BC:", bc)
print("Сумма длин:", ac + bc)