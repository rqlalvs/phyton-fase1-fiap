#Faturamento e assinatura do cliente
fatur_anual = float(input("Informe seu faturamento anual: "))
nv_assin = input("Por favor, insira o nível de assinatura desejado: ")
#Basic - Bônus de 30% sobre o faturamento anual
if nv_assin.upper() == "BASIC":
    valor_basic = float(fatur_anual) * 0.3
    print("O valor a ser pago é: {:.2f}".format(valor_basic))
#Silver - Bônus de 20% sobre o faturamento anual
elif nv_assin.upper() == "SILVER":
    valor_silver = float(fatur_anual) * 0.2
    print("O valor a ser pago é: {:.2f}".format(valor_silver))
#Gold - Bônus de 10% sobre o faturamento anual
elif nv_assin.upper() == "GOLD":
    valor_gold = float(fatur_anual) * 0.1
    print("O valor a ser pago é: {:.2f}".format(valor_gold))
#Platinum - Bônus de 5% sobre o faturamento anual
elif nv_assin.upper() == "PLATINUM":
    valor_platinum = float(fatur_anual) * 0.05
    print("O valor a ser pago é: {:.2f}".format(valor_platinum))
else:
    valor_bônus = float(fatur_anual)
    print("Opção de assinatura invalida.")
