print('Seja bem vindo a loja Bella Boutique')
nome=str(input('Qual é o seu nome?'))
valor = float(input(f'Olá {nome}, Qual o valor do produto?'))
print('''Formas de pagamentos:
      [1] à vista no dinheiro
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
pagamento = int(input('Qual a forma de pagamento? ')) 

if pagamento == 1:
    total = valor - (valor * 10 / 100)
    print(f'O produto vai custar {total:.2f} com o desconto de 10%')
elif pagamento == 2:
    total = valor - (valor * 5 / 100)
    print(f'O produto vai custar {total:.2f} com o desconto de 5%')
elif pagamento == 3:
    total = valor
    print(f'O produto vai custar {total:.2f}, dividido em 2x sem juros')
elif pagamento ==4:
    total=valor+(valor*20/100)    
    print(f'o produto vai custar {total:.2f} com 20% de juros')
else:
    print('Opção de pagamento inválida! Escolha uma opção entre 1 e 4.')
   
 