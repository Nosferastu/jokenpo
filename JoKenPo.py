import random
from time import sleep
import os

caifora = 1

cscore = 0

score = 0
print('BEM VINDO AO MEU JOGO!')

amarelo = '\033[33m'
vermelho = '\033[31m'
azul = '\033[34m'
verde = '\033[32m'
fecha = '\033[m'


while caifora == 1:
    
    lista = ['pedra','papel','tesoura']
    escolhido = random.choice(lista)
    
    print('\nPara sair, basta digitar {}[sair]{}\n'.format(verde,fecha))
    
    escolha = str(input('{}Pedra{} {}papel{} ou {}tesoura?{} '.format(vermelho,fecha,amarelo,fecha,azul,fecha)))
    
    if os.name == 'nt': #nt retorna um sistema operacional da familia windows
        os.system('cls')
    else:
        os.system('clear') # essa linha deixa essa funcionalidade multiplataforma
    
    os.system("cls")
    if escolha == 'pedra' or escolha == 'papel' or escolha == 'tesoura' or escolha == 'sair':
        if escolha == 'sair':
            break
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        sleep(1)
        print('-=' * 10)
        if (escolhido == 'pedra' and escolha == 'tesoura') or (escolhido == 'tesoura' and escolha == 'papel') or (escolhido == 'papel' and escolha == 'pedra'):
            print('{}O computador ganhou!{}'.format(vermelho,fecha))
            cscore += 1
        elif escolhido == escolha:
            print('{}EMPATOU!{}'.format(amarelo,fecha))
        else:
            score+=1
            print('{}Parabens voce ganhou{}'.format(verde,fecha))
        print(('-=' * 4) +'PLACAR' +('-=' * 3))
        print('{}VOCE:{} {}{}{}'.format(vermelho,fecha,amarelo,score,fecha))
        print('{}COMPUTADOR:{} {}{}{}'.format(azul,fecha,amarelo,cscore,fecha))
        print('-=' * 10)
        print('-=' * 10)
        print('Voce: {}\nComputador: {}'.format(escolha,escolhido))
        print('-=' * 10)
    else:
        print('{}Opção invalida, escolha novamente{}'.format(vermelho,fecha))
        continue
print('-=' * 10)   
print('A pontuação foi \n{}Voce:{} {}{}{}\n{}Computador:{} {}{}{}'.format(vermelho,fecha,amarelo,score,fecha,azul,fecha,amarelo,cscore,fecha))   
if cscore > score:
     print('E VOCE PERDEU OTARIO! AS MAQUINAS SÃO AS MELHORES')
elif score > cscore:
    print('Ganhou então...\nganhar no jokenpo ok...\nquero ver matar o exterminador do futuro...\nOTARIO!')
else:
    print('O humano deu sorte e empatou então...')
print('-=' * 10)