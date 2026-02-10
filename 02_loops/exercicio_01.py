
print("Vamos gerar a tabuada de um número inteiro de 1 a 10.")

number = int(input("Digite um número inteiro de 1 a 10: "))
if 1 <= number <= 10:
    print(f"Tabuada do {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

else:    
    print("Número inválido. Por favor, digite um número inteiro de 1 a 10.")

print("Fim do programa.")