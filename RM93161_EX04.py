from tkinter import N


n = int(input("Digite os minutos atuais: "))
senha = 1

for x in range(1,n+1):
    senha *= x
print("Senha: LIBERDADE{}".format(senha))