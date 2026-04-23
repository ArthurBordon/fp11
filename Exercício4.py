print("="*40)
valor = float(input("Digite o valor da compra: R$ "))
print("="*40)
client = input("Você é cliente VIP? (s/n) ")
if valor >= 100 or client == "s":
    print("Parabéns! Você ganhou FRETE GRÁTIS!")
else:
    print("Você não tem direito ao FRETE GRÁTIS!")
print("="*40)
