#Arquivo chamado arquivo.py, ele trata de toda a manipulação de arquivos do sistema
import os
import json

def verifica_arquivo(nome_arquivo, conteudo_padrao):
    """
    Verifica se um arquivo existe, se não existir, cria o arquivo com um conteúdo padrão.

    Args:
        nome_arquivo (str): O nome do arquivo a ser verificado.
        conteudo_padrao (dict): O conteúdo padrão a ser escrito no arquivo, se necessário.
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
    O modo 'w' garante que o arquivo seja reescrito com a versão mais recente dos dados.
    #Args:
    nome_arquivo (str): O caminho e o nome do arquivo onde os dados serão salvos.
        dados (dict): O dicionário com os dados a serem salvos.
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

    Args:
        nome_arquivo (str): O caminho e o nome do arquivo a ser lido.

    Returns:
    dict: O dicionário com os dados do arquivo, ou um dicionário vazio
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
