from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.config import caminho_doadores, caminho_estoque
from funcoes_principais.interface import *
from funcoes_principais.config import ESTOQUE_MINIMO


def lancar_doacao_sangue():
    limpar_tela()
    cabecalho('Lançar Doação de Sangue'.center(45))
    print(linha())

    doadores = carregar_dados(caminho_doadores)
    estoque = carregar_dados(caminho_estoque)

    cpf = str(leiaint('Digite o CPF do doador: '))
    if cpf not in doadores:
        print('Doador não encontrado. Por favor, cadastre o doador primeiro.')
        input('Pressione Enter para continuar...')
        return
    
    tipo_doador = doadores[cpf]['tipo_sanguineo']

    estoque[tipo_doador] += 1
    salvar_dados(caminho_estoque, estoque)

    print(f'Doação de sangue do tipo {tipo_doador} lançada com sucesso!')

    if estoque[tipo_doador] < ESTOQUE_MINIMO[tipo_doador]:
        print(f'ATENÇÃO: O estoque de {tipo_doador} está abaixo do mínimo recomendado ({ESTOQUE_MINIMO[tipo_doador]} unidades).')   

    print(linha())
    input('Pressione Enter para continuar...')  