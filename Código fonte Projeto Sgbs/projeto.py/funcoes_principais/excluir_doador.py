from uteis.arquivos import salvar_dados,carregar_dados
from funcoes_principais.config import caminho_doadores
from funcoes_principais.interface import *

def excluir_doador():
    """
    Exclui um doador do sistema com base no seu CPF.

    A função solicita o CPF do doador e, após localizá-lo, pede uma
    confirmação para a exclusão. Se confirmada, o doador é removido
    do dicionário e o arquivo de dados é atualizado.
    """
    limpar_tela()
    cabecalho('Excluir Doador'.center(45))

    # 1 - Carrega os dados de todos os doadores do arquivo JSON
    doadores = carregar_dados(caminho_doadores)

    # 2 - Solicita o CPF do doador para exclusão
    cpf = str(leiaint('Digite o CPF do doador que deseja excluir: '))

    # 3 - Verifica se o CPF existe no dicionário de doadores
    if cpf not in doadores:
        print('Doador não encontrado.')
        print(linha())
        return # Encerra a função se o doador não for encontrado
    else:
        # Pega o nome do doador para usar na mensagem de confirmação
        nome_doador = doadores[cpf]["nome"]

        print(linha())
        # 4 - Solicita a confirmação do usuário antes de excluir
        confirmacao = leiaint(f'Tem certeza que deseja excluir o doador {nome_doador}? (1 - Sim/2 - Não): ')

        if confirmacao == 1:
            # 5 - Remove o doador do dicionário usando o operador 'del'
            del doadores[cpf]
            # 6 - Salva as alterações no arquivo JSON
            salvar_dados(caminho_doadores, doadores)
            print(f'Doador {nome_doador} excluído com sucesso.')
            print(linha())
        else:
            print(f'Exclusão do doador {nome_doador} cancelada.')

    print(linha())  
    input('Pressione Enter para continuar...')
