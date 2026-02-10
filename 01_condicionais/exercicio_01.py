num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))

operacao = (input('Insira o tipo de operação que deseja realizar\n a = Multiplicação\n b = Divisão\n '
                  'c = Soma\n d = Subtração\n'))

if operacao == 'a':
    resultado = num_1 * num_2
elif operacao == 'b':
    resultado = num_1 / num_2
elif operacao == 'c':
    resultado = num_1 + num_2
elif operacao == 'd':
    resultado = num_1 - num_2
else:
    resultado = None
    print("Operação inválida.")

if resultado is not None:
    if resultado % 2 == 0:
        tipo_paridade = "par"
    else:
        tipo_paridade = "ímpar"

    if resultado >= 0:
        tipo_sinal = "positivo"
    else:
        tipo_sinal = "negativo"

if resultado is not None:
    if resultado.is_integer():
        tipo_num = "inteiro"
    else:
        tipo_num = "decimal"
print(f'Resultado da Operação = {resultado}\nO número {resultado} é {tipo_paridade} e {tipo_sinal} sendo {tipo_num}')