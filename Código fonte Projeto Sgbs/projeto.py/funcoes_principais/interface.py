#Arquivo com o nome interface.py, ele trata de toda a interface do sistema 
import os

def leiaint(msg):
    """
    Le um numero e valida se ele é inteiro baseado na entrada do usuario

    param msg: A mensagem a ser exibida ao usuario

    return: O numero inteiro lido ou 0 em caso de erro
    """
    while True:
        try:
            n = int(input(msg)) 
        except (ValueError, TypeError):
            print('ERRO: Digite um numero inteiro')
        except (KeyboardInterrupt): 
            print('Entrada de dados interrompida pelo usuario')
            return 0 
        else: 
            return n


def leiafloat(msg):
    """
    Lê um número de ponto flutuante e valida a entrada do usuário.

    param msg: A mensagem a ser exibida ao usuário

    return: O número de ponto flutuante lido ou 0.0 em caso de erro
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um número válido')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0.0
        else:
            return n

def linha(tam = 45):
    """
    param tam: o tamanho da linha por padrão 45

    return: A linha formatada
    """
    return '-' * tam




def cabecalho(txt):
    tam = 45
    print(linha(tam)) 
    print(f'{txt:^30}')
    print(linha(tam))




def exibir_menu_principal(lista):
    cabecalho('Sistema de Gerenciamento e Controle de Sangue')
    for i, item in enumerate(lista):
        print(f'\033[0;33m{i+1}\033[m - \033[0;34m{item}\033[m')




def limpar_tela():
    """
    Limpa a tela do terminal.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

