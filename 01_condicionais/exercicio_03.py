
print("Vamos calcular o valor a ser pago pelo cliente com base na quantidade de litros vendidos e o tipo de combustível.")

qtd_litros = float(input("Digite a quantidade de litros vendidos: "))

while True:
    tipo_combustivel = input("Digite o tipo de combustível (E para etanol e D para diesel): ").upper()

    if tipo_combustivel == "E":
        preco_litro = 1.70
        if qtd_litros <= 15:
            desconto = 0.02 * preco_litro * qtd_litros
        else:
            desconto = 0.04 * preco_litro * qtd_litros
        break

    elif tipo_combustivel == "D":
        preco_litro = 2.00
        if qtd_litros <= 15:
            desconto = 0.03 * preco_litro * qtd_litros
        else:
            desconto = 0.05 * preco_litro * qtd_litros
        break
    else:
        print("Tipo de combustível inválido. Por favor, insira 'E' para etanol ou 'D' para diesel.")
 

valor_total = preco_litro * qtd_litros - desconto
print(f"O valor a ser pago pelo cliente é: R$ {valor_total:.2f}")