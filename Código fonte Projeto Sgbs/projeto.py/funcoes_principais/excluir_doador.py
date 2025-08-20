from uteis.arquivos import salvar_dados,carregar_dados
from funcoes_principais.config import caminho_doadores
from funcoes_principais.interface import *

def excluir_doador():
    limpar_tela()
    cabecalho('Excluir Doador'.center(45))
    doadores = carregar_dados(caminho_doadores)
    cpf = str(leiaint('Digite o CPF do doador que deseja excluir: '))
    if cpf not in doadores:
        print('Doador não encontrado.')
        print(linha())
        return
    else:
        nome_doador = doadores[cpf]["nome"]

        print(linha())
        confirmacao = leiaint(f'Tem certeza que deseja excluir o doador {nome_doador}? (1 - Sim/2 - Não): ')
        if confirmacao == 1:
            del doadores[cpf]
            salvar_dados(caminho_doadores, doadores)
            print(f'Doador {nome_doador} excluído com sucesso.')
            print(linha())
        else:
            print(f'Exclusão do doador {nome_doador} cancelada.')

    print(linha())  

        