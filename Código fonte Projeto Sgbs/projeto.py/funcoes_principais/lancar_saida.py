from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.config import caminho_estoque
from funcoes_principais.interface import *

def lancar_saida():
    limpar_tela()
    cabecalho('Lançar Saída de Bolsa de Sangue'.center(45))
    print(linha())

    estoque = carregar_dados(caminho_estoque)

    tipo_sangue = str(input('Digite o tipo de sangue (A+, A-, B+, B-, AB+, AB-, O+, O-): ').strip().upper())

    if tipo_sangue not in estoque:
        print(f'Tipo sanguíneo {tipo_sangue} não encontrado no estoque.')
        print(linha())
        input('Pressione Enter para continuar...')
        return
    
    quantidade = leiaint(f'Quantas bolsas de {tipo_sangue} foram retiradas? ')

    if quantidade > estoque[tipo_sangue]:
        print(f'Quantidade solicitada ({quantidade}) é maior que a disponível no estoque ({estoque[tipo_sangue]}).')
        print(linha())
        input('Pressione Enter para continuar...')
        return
    
    estoque[tipo_sangue] -= quantidade
    salvar_dados(caminho_estoque, estoque)
    print('Lançamento de saída realizado com sucesso.')
    print(linha())

    input('Pressione Enter para continuar...')

