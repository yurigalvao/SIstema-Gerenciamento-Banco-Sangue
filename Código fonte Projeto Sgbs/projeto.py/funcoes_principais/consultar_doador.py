from uteis.arquivos import carregar_dados
from funcoes_principais.config import caminho_doadores
from funcoes_principais.interface import *




def consultar_doador():
    """
    Exibe os dados de um doador específico, incluindo o histórico de triagens.

    A função solicita o CPF do doador. Se o doador for encontrado,
    ela imprime todas as suas informações pessoais. Caso o doador
    possua um histórico de triagens, cada triagem é listada
    com seus detalhes e status.
    """
    limpar_tela()
    cabecalho('Consultar Doador'.center(45))

    # Carrega os dados dos doadores do arquivo JSON
    doadores = carregar_dados(caminho_doadores)

    # Solicita o CPF do doador para a consulta
    cpf = str(leiaint('Digite o CPF do doador que deseja consultar: '))

    # Verifica se o CPF existe no dicionário de doadores
    if cpf not in doadores:
        print('Doador não encontrado.')
        input('Pressione enter para continuar ...')
        return
    else:
        # Exibe os dados pessoais do doador
        print(f'Consulta do doador: {doadores[cpf]["nome"]}')
        print(linha())
        print(f'CPF: {cpf}')
        print(f'Idade: {doadores[cpf]["idade"]} anos.')
        print(f'Peso: {doadores[cpf]["peso"]:.1f} kg')
        print(f'Sexo: {doadores[cpf]["sexo"]}')
        print(f'Tipo Sanguíneo: {doadores[cpf]["tipo_sanguineo"]}')
        print(f'Telefone: {doadores[cpf]["telefone"]}')
        print(f'Email: {doadores[cpf]["email"]}')
        
        #Só exibe a triagem se a chave 'triagem' for identificada no cpf do doador
        if 'triagem' in doadores[cpf]:
            print(linha())
            print('Histórico de Triagens: ')
            # Itera sobre cada triagem do doador e exibe seus detalhes
            for triagem in doadores[cpf]['triagem']:
                print(linha())
                print(f"Data: {triagem['data']}")
                
                #verificando e exibindo cada uma das chaves da triagem, Garantindo que não ocorra um erro caso alguma chave não exista.
                if 'documentos' in triagem:
                    print(f"Documentos: {triagem['documentos']}")
                if 'saude' in triagem:
                    print(f"Saúde: {triagem['saude']}")
                if 'sono' in triagem:
                    print(f"Sonos: {triagem['sono']}")
                if 'alcool' in triagem:
                    print(f"Álcool: {triagem['alcool']}")
                if 'fumo' in triagem:
                    print(f"Fumo: {triagem['fumo']}")
                if 'primeira_doacao' in triagem:
                    # Converte o valor booleano para uma string amigável
                    print(f"Primeira Doação: {'Sim ' if triagem['primeira_doacao'] else 'Não '}")
                if 'doenca_impeditiva' in triagem:
                    print(f"Doença Impeditiva: {triagem['doenca_impeditiva']}") 

                if 'status' in triagem:
                    print(f'Status: {triagem['status']}')
        else:
            # Mensagem exibida caso o doador não tenha histórico de triagens
            print(f'O doador {doadores[cpf]["nome"]} não possui histórico de triagens.')


        print(linha())  
        input('Pressione Enter para continuar...')  
