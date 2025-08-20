from uteis.arquivos import carregar_dados
from funcoes_principais.config import caminho_estoque, ESTOQUE_MINIMO
from funcoes_principais.interface import *



def consultar_estoque():
    limpar_tela()
    cabecalho('Consultar Estoque'.center(45))
    print(linha())

    estoque_atual = carregar_dados(caminho_estoque)

    for tipo_sangue, quantidade in estoque_atual.items():
        print(f'{tipo_sangue}: {quantidade} bolsas')
        if quantidade < ESTOQUE_MINIMO[tipo_sangue]:
            print(f'** Atenção: Estoque de tipo {tipo_sangue} abaixo do minimo recomendado!')
            
        print(linha())

    print('Consulta de estoque concluída.')
    print(linha())
    input('Pressione Enter para continuar...')

