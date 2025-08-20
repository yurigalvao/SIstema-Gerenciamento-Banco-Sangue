from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.config import caminho_doadores
from funcoes_principais.interface import *

def cadastrar_doador():
    
    """
    Funcao responsavel pelo cadastro de novos doadores.

    A funcao solicita as informacoes basicas do doador (nome, idade, peso, etc.)
    e as armazena em um dicionario, que e salvo no arquivo de dados.
    Realiza validacoes basicas de idade e peso e verifica se o doador ja existe.
    """
    limpar_tela()
    cabecalho('Cadastrar Doador'.center(45))
    #1 - carrega os dados existentes de doadores
    doadores = carregar_dados(caminho_doadores)

    #2 - solicita o cpf e verifica se o doador ja esta cadastrado
    cpf = str(leiaint('Digite o CPF do doador (sem pontos ou traços): '))
    if cpf in doadores:
        print(f'Doador com CPF {cpf} já está cadastrado!.')

        #3 - solicita se o usuario deseja ver os dados do doador
        resposta = leiaint('Deseja ver os dados do doador? (1-sim/2-não)')
        if resposta == 1:
            print(linha())
            print(f'Nome: {doadores[cpf]["nome"]}')
            print(f'Idade: {doadores[cpf]["idade"]}')
            print(f'Peso: {doadores[cpf]["peso"]:.1f} kg')
            print(f'Tipo Sanguíneo: {doadores[cpf]["tipo_sanguineo"]}')
            print(f'Telefone: {doadores[cpf]["telefone"]}')
            print(f'E-mail: {doadores[cpf]["email"]}')
            print(linha())
            input('Pressione Enter para continuar...')
            return
        else:
            print('Saindo...')
            print(linha())
            return
    else:
        #4 - Coleta os dados para um novo cadastro
        nome = input('Digite o nome completo do doador: ')
        idade = leiaint('Digite a idade do doador: ')

        #5 - valida a idade do doador 
        if idade <16 or idade > 69:
            print('Idade inválida! O doador deve ter entre 16 e 69 anos.')
            print(linha())
            return
        peso = leiafloat('Digite o peso do doador (em kg): ')

        #6 - valida o peso do doador
        if peso < 50:
            print('Peso inválido! Doadores devem pesar no mínimo 50 kg.')
            print(linha())
            return
        sexo = input('Digite o sexo do doador (M/F): ').strip().upper()
        tipo_sanguineo = input('Digite o tipo sanguíneo do doador (A+, A-, B+, B-, AB+, AB-, O+, O-): ').upper()
        telefone = input('Digite o telefone do doador (com DDD): ')
        email = input('Digite o e-mail do doador: ')

        #7- cria um dicionario com os dados do doador
        dados_doador = {
            'nome': nome,
            'idade': idade,
            'peso': peso,
            'sexo': sexo,
            'tipo_sanguineo': tipo_sanguineo,
            'telefone': telefone,
            'email': email
        }

        #8 - Adiciona o novo doador ao dicionario principal e salva no arquivo
        doadores[cpf] = dados_doador
        salvar_dados(caminho_doadores, doadores)
        print(f'Doador {nome} cadastrado com sucesso!')
        print(linha())

        #9 Aguarda e limpa a tela para o próximo menu
        input('Pressione Enter para continuar')
        


