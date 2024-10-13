# Треугольник со сторонами АВ, ВС,СА
from dis import CACHE
from distutils.bcppcompiler import BCPPCompiler

AB = int(input('Введите сторону АВ треугольника: '))
BC = int(input('Введите сторону ВС треугольника: '))
CA = int(input('Введите сторону CA треугольника: '))

if AB >= BC + CA:
    print("Такого треугольника не существует")
elif BC >= AB + CA:
    print("Такого треугольника не существует")
elif CA >= AB + BC:
    print("Такого треугольника не существует")
else:
    if AB==BC and BC==CA and CA==AB:
        print("Треугольник равносторонний")
    elif AB!=BC and BC !=CA and CA !=AB:
        print("Треугольник разносторонний")
    else:
        print("Треугольник равнобедренный")




