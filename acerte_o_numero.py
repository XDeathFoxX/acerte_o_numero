"""
Programa criado atraves de um exercício que encontrei na internet para praticar
Esse programa gera um valor aleatório entre 1 e 50 sem ser mostrado para o usuário e é 
preciso dar "chutes" para tentar acertar o número aleatório,o programa retorna se
o número que você digitou está baixo,alto ou se é o número certo.
"""

from random import choice as cho

def jogar_novamente():
    escolhas='sim','nao'
    jogar_novamente=input('Deseja jogar novamente?(Sim/Não): ').lower().strip()
    jogar_novamente=jogar_novamente.replace('ã','a')
    
    if jogar_novamente=='sim':
        acerte_numero()
    
    if jogar_novamente=='nao':
        exit()
    
    if jogar_novamente not in escolhas:
        while jogar_novamente not in escolhas:
            print('Digite Sim ou Não: ')
            jogar_novamente=input('Deseja jogar novamente?(Sim/Não): ').lower().strip()
        else:
            if jogar_novamente=='sim':
                acerte_numero()
            if jogar_novamente=='nao':
                exit() 

def acerte_numero():
    chute = 0
    chances = 8
    numeros=range(1,51)
    nums_digitados = []
    num_certo=cho(numeros)
    #print(num_certo)
    
    while chute !='sair':
        chute=input('Tente acertar o número entre 1 à 50: ')
        
        try:
            int(chute)
            it_is=True
        except:
            it_is=False
        
        if chute == 'sair':
            break

        if it_is==True:
            if int(chute) < num_certo:
                if chute not in nums_digitados:
                    chances = chances - 1
                    print()
                    print(f'Chute mais alto! Você ainda tem {chances} tentativas')
                    nums_digitados.append(chute)
                else:
                    print()
                    print('Chute mais alto, número já digitado!')
                    print(f'Você ainda tem {chances} tentativas!')
                    print()

            elif int(chute) > num_certo and int(chute) <= 50:
                if chute not in nums_digitados:
                    chances = chances - 1
                    print()
                    print(f'Chute mais baixo! Você ainda tem {chances} tentativas')
                    nums_digitados.append(chute)
                else:
                    print()
                    print('Chute mais baixo, número já digitado!')
                    print(f'Você ainda tem {chances} tentativas!')
                    print()

            elif int(chute) == num_certo:
                print()
                print(f'Parabéns,você acertou, o número secreto era {num_certo}!!')
                print()
                jogar_novamente()

            elif int(chute) > 50:
                print('Digite números abaixo de 50!')

            if chances == 0:
                print()
                print(f'Ops! Você perdeu! O número secreto era {num_certo}')
                jogar_novamente()
        else:
            print('Digite somente números entre 1 e 50! ')
acerte_numero()
