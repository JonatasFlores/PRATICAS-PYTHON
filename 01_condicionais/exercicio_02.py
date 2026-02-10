
print("Vamos verificar se os valores inseridos podem formar um triângulo e qual tipo de triângulo é formado.")

lado_1 = float(input("Digite o primeiro valor: "))
lado_2 = float(input("Digite o segundo valor: "))
lado_3 = float(input("Digite o terceiro valor: "))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    if lado_1 == lado_2 == lado_3:
        tipo_triangulo = "Equilátero"
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    print(f"Os valores inseridos formam um triângulo {tipo_triangulo}.")
else:
    print("Os valores inseridos não podem formar um triângulo.")    