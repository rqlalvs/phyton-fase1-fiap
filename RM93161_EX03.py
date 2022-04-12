array_impar = [int(input('Esta nota é de um aluno par, por favor, insira a nota do aluno de número 1: '))]
array_par = [int(input('Esta nota é de um aluno impar, por favor, insira a nota do aluno de número 2: '))]

for i in range(3,51,2):
    array_impar.append(int(input("Esta nota é de um aluno par, por favor, insira a nota do aluno de número %s: " % i)))
for i in range(4,51,2):
    array_par.append(int(input("Esta nota é de um aluno impar, por favor, insira a nota do aluno de número %s: " % i)))

if (sum(array_impar)/len(array_impar)) > (sum(array_par)/len(array_par)):
    print('A média dos alunos impares é maior')
else:
    print('A média dos alunos pares é maior.')

