from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.config import caminho_estoque
from funcoes_principais.interface import *

def lancar_saida():
    """
    Registra a saída de bolsas de sangue do estoque.

    A função solicita o tipo sanguíneo e a quantidade de bolsas a serem retiradas.
    Antes de realizar a operação, ela valida se o tipo sanguíneo existe no estoque
    e se a quantidade solicitada é menor ou igual à quantidade disponível.
    Se a operação for válida, o estoque é atualizado e as alterações são salvas.
    """
    limpar_tela()
    cabecalho('Lançar Saída de Bolsa de Sangue'.center(45))
    print(linha())

    # 1 - Carrega o dicionário com o estoque atual de sangue do arquivo JSON
    estoque = carregar_dados(caminho_estoque)

    # 2 - Solicita o tipo sanguíneo para a saída de bolsas
    tipo_sangue = str(input('Digite o tipo de sangue (A+, A-, B+, B-, AB+, AB-, O+, O-): ').strip().upper())

    # 3 - Verifica se o tipo sanguíneo inserido existe no estoque
    if tipo_sangue not in estoque:
        print(f'Tipo sanguíneo {tipo_sangue} não encontrado no estoque.')
        print(linha())
        input('Pressione Enter para continuar...')
        return # Encerra a função se o tipo sanguíneo for inválido
    
    # 4 - Solicita a quantidade de bolsas a serem retiradas
    quantidade = leiaint(f'Quantas bolsas de {tipo_sangue} foram retiradas? ')

    # 5 - Valida se a quantidade solicitada é maior que a quantidade disponível
    if quantidade > estoque[tipo_sangue]:
        print(f'Quantidade solicitada ({quantidade}) é maior que a disponível no estoque ({estoque[tipo_sangue]}).')
        print(linha())
        input('Pressione Enter para continuar...')
        return # Encerra função se a quantidade for insuficiente
    
    # 6 - Decrementa a quantidade de bolsas de sangue no estoque
    estoque[tipo_sangue] -= quantidade

    # 7 - Salva o dicionário de estoque atualizado de volta no arquivo JSON
    salvar_dados(caminho_estoque, estoque)
    print('Lançamento de saída realizado com sucesso.')
    print(linha())

    input('Pressione Enter para continuar...')

