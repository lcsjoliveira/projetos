print('bem vindo ao jogo de adivinhaçã')
numero_secreto = 42
rodada = 1
total_de_tentativas = 3
while rodada <= total_de_tentativas:
    print(f'Rodada {rodada} de {total_de_tentativas}')
    chute = int(input('digite seu chute'))
    if chute == numero_secreto:
        print('Parabéns, você acertou: FIM DO JOGO')
        break
    elif chute > numero_secreto:
        print(f'Você digitou o número {chute} que foi maior que o número secreto')
    elif chute < numero_secreto:
        print('Você digitou o número', {chute}, 'que foi menor que o número secreto')
    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada + 1