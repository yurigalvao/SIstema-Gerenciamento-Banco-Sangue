from uteis.arquivos import carregar_dados
from funcoes_principais.config import caminho_doadores
from funcoes_principais.interface import *




def consultar_doador():
    limpar_tela()
    cabecalho('Consultar Doador'.center(45))
    doadores = carregar_dados(caminho_doadores)
    cpf = str(leiaint('Digite o CPF do doador que deseja consultar: '))
    if cpf not in doadores:
        print('Doador não encontrado.')
        input('Pressione enter para continuar ...')
        return
    else:
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
            for triagem in doadores[cpf]['triagem']:
                print(linha())
                print(f"Data: {triagem['data']}")
                
                #verificando e exibindo cada uma das chaves da triagem
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
                    print(f"Primeira Doação: {'Sim ' if triagem['primeira_doacao'] else 'Não '}")
                if 'doenca_impeditiva' in triagem:
                    print(f"Doença Impeditiva: {triagem['doenca_impeditiva']}") 

                if 'status' in triagem:
                    print(f'Status: {triagem['status']}')
        else:
            print(f'O doador {doadores[cpf]["nome"]} não possui histórico de triagens.')


        print(linha())  
        input('Pressione Enter para continuar...')  
