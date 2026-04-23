print("====================================")
idade = int(input("Qual a sua idade? " ))
carteira = input("Você possui carteira de estudante? (s/n) ")
if idade >= 12 and carteira == "s":
    print("Entrada permitida com meia-entrada!")
elif idade >=12 and carteira == 'n':
    print("Entrada permitida somente com ingresso inteiro!")
else:
    idade <12
    print("Entrada proibida!")
print("===================================1")