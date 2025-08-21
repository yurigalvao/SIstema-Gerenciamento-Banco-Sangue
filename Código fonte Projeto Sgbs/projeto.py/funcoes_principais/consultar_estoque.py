from uteis.arquivos import carregar_dados
from funcoes_principais.config import caminho_estoque, ESTOQUE_MINIMO
from funcoes_principais.interface import *



def consultar_estoque():
    """
    Exibe o estoque atual de bolsas de sangue e alerta sobre níveis baixos.

    A função carrega o dicionário de estoque e itera sobre cada tipo sanguíneo,
    mostrando a quantidade atual de bolsas. Se a quantidade estiver abaixo
    do mínimo definido em `ESTOQUE_MINIMO`, um aviso é exibido.
    """
    limpar_tela()
    cabecalho('Consultar Estoque'.center(45))
    print(linha())

    # 1 - Carrega o dicionário com o estoque atual de sangue do arquivo JSON
    estoque_atual = carregar_dados(caminho_estoque)

    # 2 - Itera sobre cada tipo sanguíneo no estoque para exibir a quantidade
    for tipo_sangue, quantidade in estoque_atual.items():
        print(f'{tipo_sangue}: {quantidade} bolsas')

        # 3 - Verifica se a quantidade atual esta abaixo do estoque minimo definido
        if quantidade < ESTOQUE_MINIMO[tipo_sangue]:
            print(f'** Atenção: Estoque de tipo {tipo_sangue} abaixo do minimo recomendado!')
            
        print(linha())

    print('Consulta de estoque concluída.')
    print(linha())
    input('Pressione Enter para continuar...')

