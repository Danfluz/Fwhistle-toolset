def avaliacao(valor, nomenclatura='naodisponivel'):
    if valor < 15:
        denominacao = 'terrível'
    elif valor >= 15 and valor < 30:
        denominacao = 'ruim'
    elif valor >= 30 and valor < 40:
        denominacao = 'fraco'
    elif valor >= 40 and valor < 50:
        denominacao = 'decente'
    elif valor >= 50 and valor < 60:
        denominacao = 'bom'
    elif valor >= 60 and valor < 70:
        denominacao = 'excelente'
    elif valor >= 15 and valor < 80:
        denominacao = 'soberbo'
    elif valor >= 15 and valor < 90:
        denominacao = 'brilhante'
    elif valor >= 15 and valor < 100:
        denominacao = 'majestoso'
    elif valor >= 100 and valor < 109:
        denominacao = 'incrível'
    elif valor >= 110 and valor < 120:
        denominacao = 'inacreditável'
    elif valor >= 120:
        denominacao = 'lendário'

    print(f'')
    print(f'O valor de {nomenclatura} é: {valor} ({denominacao}).')

"""
Calculadora para FinalWhistle - Kareshi
"""

print(f'FW Pycalc versão 0.2')
print(f'Esta é uma calculadora para o jogo FinalWhistle')
print(f'site: https://www.finalwhistle.org')
print(f'Desenvolvida em Python por: Kareshi. 2021')

while True:
    valor = None

    print('')
    print('')
    optcalc = input(f'O que deseja calcular?\n(1) Chute à distância\n(2) Driblar e chutar\n(3) Bola aérea\n(4) Passe longo (posicionamento)\n(5) Academia\n(6) Adaptação\n(S) Sair\n\nEscolha a opção: ')

    if optcalc == '1':
        print('SELECIONADO: Chute à distância.')
        print('')

        fi = int(input('Digite o valor FI: '))
        lscap = int(fi * 2)
        pa = int(input('Digite o valor PA: '))

        if pa > lscap:
            valor = (lscap + fi) / 2
        else:
            valor = (fi + pa) / 2

        avaliacao(valor, nomenclatura='chute à distância')

    if optcalc == '2':
        print('SELECIONADO: driblar e chutar.')
        print('')

        fi = int(input('Digite o valor FI: '))
        pa = int(input('Digite o valor PA: '))
        dbcap = 1.5 * pa
        if fi > dbcap:
            valor = dbcap
        else:
            valor = fi

        avaliacao(valor, nomenclatura='Driblar e chutar')

    if optcalc == '3':
        print('SELECIONADO: Bola aérea')
        print('')

        posicao = input('Digite A para atacante ou D para defensor: ')
        posicao = posicao.upper()

        if posicao == 'A':
            ae = int(input('Digite o valor AE: '))
            aecap = ae + 10
            cb = int(input('Digite o valor CB: '))
            valor = ((cb * 1.2) + (ae * 1.8)) / 3
            if valor > aecap:
                valor = aecap
            else:
                valor = ((cb * 1.2) + (ae * 1.8)) / 3

            avaliacao(valor, nomenclatura='bola aérea (Recepção)')

        if posicao == 'D':
            ae = int(input('Digite o valor AE: '))
            aecap = ae + 10
            ta = int(input('Digite o valor TA: '))
            valor = ((ta * 1.2) + (ae * 1.8)) / 3
            if valor > aecap:
                valor = aecap
            else:
                valor = ((ta * 1.2) + (ae * 1.8)) / 3

            avaliacao(valor, nomenclatura='bola aérea (Desarme)')

    if optcalc == '4':
        print('SELECIONADO: Passe longo')
        print('')

        posicao = input('Digite A para atacante ou D para defensor: ')
        posicao = posicao.upper()

        if posicao == 'A':
            ae = int(input('Digite o valor AE: '))
            po = int(input('Digite o valor PO: '))
            co = int(input('Digite o valor CO: '))
            valor = ((ae / 2) + (po / 2) + co) / 2

            avaliacao(valor, nomenclatura='posicionamento para passes longos (ataque)')

        elif posicao == 'B':
            ae = int(input('Digite o valor AE: '))
            pd = int(input('Digite o valor PD: '))
            co = int(input('Digite o valor CO: '))
            valor = ((ae / 2) + (pd / 2) + co) / 2

            avaliacao(valor, nomenclatura='posicionamento para passes longos (defesa)')

    if optcalc.upper() == 'S':

        print('')
        print('Você escolheu sair.')
        print('Lembre-se que a performance dos seus jogadores é relativa à força do adversário que ele enfrenta.')
        print('')
        input('Pressione qualquer tecla para encerrar...')
        break

    # if optcalc == '5':
    #     print('SELECIONADO: Academia')
    #     print('')
    #
    #     nivel = int(input('Digite o nível atual de sua academia: '))
    #
    #     if nivel <40:
    #         qtd_draft = 1
    #     if nivel >=40 and nivel <60:
    #         qtd_draft = 2
    #     if nivel >=60:
    #         qtd_draft = 3
    #
    #     investimento = int(input('Digite o SEU investimento mensal: '))
    #     vchave = int(input('Digite o valor de investimento CHAVE: '))
    #
    #     precisao = 40 + 0.6 * nivel
    #
    # print(f'Você possui uma academia nível {nivel} e pode puxar até {qtd_draft} jogadores de uma vez.'
    #       f'\nOs jogadores sacados podem variar entre ')

    if optcalc == '6':
        print('SELECIONADO: Adaptação')
        print('')