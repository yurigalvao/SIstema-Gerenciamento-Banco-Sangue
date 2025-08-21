#Arquivo chamado arquivo.py, ele trata de toda a manipulação de arquivos do sistema
import os
import json

def verifica_arquivo(nome_arquivo, conteudo_padrao):
    """
    Verifica a existência de um arquivo e o cria com conteúdo padrão se não existir.

    Esta função tenta abrir o arquivo em modo de leitura. Se um FileNotFoundError
    (erro comum quando o arquivo não existe) for capturado, ela cria o arquivo
    e escreve o conteúdo padrão fornecido.

    Args:
        nome_arquivo (str): O caminho e nome do arquivo a ser verificado.
        conteudo_padrao (dict): Um dicionário com o conteúdo JSON inicial.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            pass
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(conteudo_padrao, arquivo, indent=4)



def salvar_dados(nome_arquivo, dados):
    """
    Salva um dicionário Python em um arquivo JSON.

    Esta função sobrescreve o arquivo existente com os dados mais recentes.
    Ela utiliza um bloco try-except para capturar e tratar possíveis erros
    de I/O (entrada/saída de arquivo) ou outros erros inesperados.

    Args:
        nome_arquivo (str): O caminho completo e o nome do arquivo JSON onde os dados serão salvos.
        dados (dict): O dicionário Python contendo os dados a serem salvos.
    """
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
            print(f'Dados salvos em {nome_arquivo} com sucesso!.')
    except IOError as e:
        print(f'Erro ao salvar dados em {nome_arquivo}: {e}')
    except Exception as e:
        print(f'Erro inesperado ao salvar dados em {nome_arquivo}: {e}')


def carregar_dados(nome_arquivo):
    """
    Carrega dados de um arquivo JSON para um dicionário Python.

    Esta função lê o conteúdo de um arquivo JSON e o converte para um dicionário.
    Ela trata três possíveis erros:
    - FileNotFoundError: se o arquivo não existir.
    - json.JSONDecodeError: se o arquivo JSON estiver corrompido ou mal formatado.
    - Exception: para qualquer outro erro inesperado.

    Args:
        nome_arquivo (str): O caminho completo e o nome do arquivo a ser lido.

    Returns:
        dict: O dicionário com os dados do arquivo. Retorna um dicionário vazio
            se o arquivo não for encontrado ou estiver corrompido.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')
        return {}
    except json.JSONDecodeError:
        print(f'Erro ao decodificar o JSON em {nome_arquivo}.')
        return {}
    except Exception as e:
        print(f'Erro inesperado ao carregar dados de {nome_arquivo}: {e}')
        return {}
    


def inicializar_estoque(nome_arquivo):
    """
    Inicializa o arquivo de estoque com valores padrão para cada tipo sanguíneo.

    Esta função verifica se o arquivo de estoque de sangue já existe. Se não
    existir, ela cria um novo arquivo JSON com todos os tipos sanguíneos
    (A+, A-, B+, etc.) e seus respectivos estoques iniciais zerados.

    Args:
        nome_arquivo (str): O caminho completo e o nome do arquivo JSON do estoque a ser inicializado.
    """
    if not os.path.exists(nome_arquivo):
        estoque_inicial = {
            "A+": 0,
            "A-": 0,
            "B+": 0,
            "B-": 0,
            "AB+": 0,
            "AB-": 0,
            "O+": 0,
            "O-": 0
        }
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(estoque_inicial, arquivo, indent=4)
            print(f'Arquivo {nome_arquivo} criado com estoque inicial.')
