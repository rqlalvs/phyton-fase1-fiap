
Seg = int(input("Segunda-feira: "))
Ter = int(input("Terça-feira: "))
Qua = int(input("Quarta-feira: "))
Qui = int(input("Quinta-feira: "))
Sex = int(input("Sexta-feira: "))

if Seg > Ter and Seg > Qua and Seg > Qui and Seg > Sex:
    print("O dia escolhido para realização das lives foi: Segunda-feira.")
elif Ter > Seg and Ter > Qua and Ter > Qui and Ter > Sex:
    print("O dia escolhido para realização das lives foi: Terça-feira.")
elif Qua > Seg and Qua > Ter and Qua > Qui and Qua > Sex:
    print("O dia escolhido para realização das lives foi: Quarta-feira.")
elif Qui > Seg and Qui > Ter and Qui > Qua and Qui > Sex:
    print("O dia escolhido para realização das lives foi: Quinta-feira.")
elif Sex > Seg and Sex > Ter and Sex > Qua and Sex > Qui:
    print("O dia escolhido para realização das lives foi: Sexta-feira")
elif Seg == Ter or Seg == Qua or Seg == Qui or Seg == Sex or Ter == Seg or Ter == Qua or Ter == Qui or Ter == Sex or Qua == Seg or Qua == Ter or Qua == Qui or Qua == Sex or Qui == Seg or Qui == Ter or Qui == Qua or Qui == Sex or Sex == Seg or Sex == Ter or Sex == Qua or Sex == Qui:
    print("O dia das lives ainda não foi escolhido devido ao empate na votação. Favor, votar novamente.")