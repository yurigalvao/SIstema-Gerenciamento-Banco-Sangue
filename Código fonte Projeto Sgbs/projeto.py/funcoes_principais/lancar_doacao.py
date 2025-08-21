from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.config import caminho_doadores, caminho_estoque
from funcoes_principais.interface import *
from funcoes_principais.config import ESTOQUE_MINIMO


def lancar_doacao_sangue():
    """
    Registra uma nova doação de sangue no sistema e atualiza o estoque.

    A função solicita o CPF do doador para identificar seu tipo sanguíneo.
    Em seguida, aumenta o contador de bolsas de sangue do tipo correspondente
    no arquivo de estoque. Após a atualização, exibe uma mensagem de sucesso
    e alerta o usuário se o estoque de sangue estiver abaixo do nível mínimo.
    """
    limpar_tela()
    cabecalho('Lançar Doação de Sangue'.center(45))
    print(linha())

    # 1 - Carrega os dados dos doadores e do estoque dos arquivos JSON
    doadores = carregar_dados(caminho_doadores)
    estoque = carregar_dados(caminho_estoque)

    # 2 - Solicita o CPF do doador para identificar o tipo sanguíneo
    cpf = str(leiaint('Digite o CPF do doador: '))
    if cpf not in doadores:
        print('Doador não encontrado. Por favor, cadastre o doador primeiro.')
        input('Pressione Enter para continuar...')
        return
    
    # 3 - Pega o tipo sanguíneo do doador a partir dos dados carregados 
    tipo_doador = doadores[cpf]['tipo_sanguineo']

    # 4 - Incrementa a quantidade de bolsas de sangue no estoque 
    estoque[tipo_doador] += 1

    # 5 - Salva o dicionário de estoque atualizado de volta no arquivo JSON
    salvar_dados(caminho_estoque, estoque)

    print(f'Doação de sangue do tipo {tipo_doador} lançada com sucesso!')

    # 6 - Verifica se o estoque do tipo doado está abaixo do mínimo e exibe um alerta 
    if estoque[tipo_doador] < ESTOQUE_MINIMO[tipo_doador]:
        print(f'ATENÇÃO: O estoque de {tipo_doador} está abaixo do mínimo recomendado ({ESTOQUE_MINIMO[tipo_doador]} unidades).')   

    print(linha())
    input('Pressione Enter para continuar...')  