from funcoes_principais.config import caminho_doadores
from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.interface import *
from datetime import date


CONDICOES_IMPEDITIVAS = (
    ('HIV', 'AIDS'),
    ('HEPATITE', 'Hepatite B, C, ou qualquer tipo de icterícia após os 10 anos de idade.'),
    ('DOENÇA DE CHAGAS', 'Doença de Chagas'),
    ('MALÁRIA', 'Doença transmitida por mosquitos, mesmo que a pessoa não tenha mais os sintomas.'),
    ('SÍFILIS', 'Sífilis'),
    ('HANSENÍASE', 'Hanseníase'),
    ('TUBERCULOSE', 'Tuberculose'),
    ('CÂNCER', 'Qualquer tipo de câncer, incluindo Leucemia e Linfoma.'),
    ('DIABETES', 'Diabetes, especialmente se a pessoa usar insulina.'),
    ('DOENÇAS AUTOIMUNES', 'Como Lúpus, Artrite Reumatoide, Psoríase grave.'),
)

def triagem():
    """
    Funcao responsavel pela triagem de doadores.
    
    A funcao verifica a elegibilidade do doador com base em uma serie de criterios,
    incluindo:
    - Verificacao de saude geral.
    - Condicoes de idade e documentacao.
    - Habitos recentes (sono, alcool, fumo).
    - Doencas impeditivas.
    
    A triagem e interrompida no primeiro criterio que nao for atendido.
    O historico de triagens anteriores do doador e registrado.
    """
    limpar_tela()
    cabecalho('Triagem'.center(45))
    print(linha())
    #1 - Carrega os dados dos doadores  
    doadores = carregar_dados(caminho_doadores)

    #2 - solicita o cpf e verifica se o doador ja esta cadastrado   
    cpf = str(leiaint('Digite o CPF do doador para triagem: '))

    #3 - verifica se o doador esta cadastrado   
    if cpf not in doadores:
        print(f'Doador com CPF {cpf} não encontrado!.')
        return
    else:
        print(f'Doador encontrado: {doadores[cpf]["nome"]}')
        print('Iniciando a triagem...')
        print(linha())
        #4 - inicia a triagem, preparando a estrutura pra salvar o historico
        #Se a chave triagem nao existir , ou nao for uma lista, cria uma lista vazia
        if 'triagem' not in doadores[cpf]:
            doadores[cpf]['triagem'] = []

        #Cria um novo dicionario para a sessao de triagem atual
        data_de_hoje = date.today().strftime('%d/%m/%Y')
        nova_triagem = {'data': data_de_hoje}

        documento = leiaint('Está com todos os documentos necessários? (1 - Sim/2 - Não): ')
        if documento != 1:
            nova_triagem['documentos'] = 'Doador nao trouxe os documentos necessários'
            nova_triagem['status'] = 'Reprovado'    
            print('O doador nao trouxe a doxumentação necessária! Favor tente novamente em outro dia!.')
            doadores[cpf]['triagem'].append(nova_triagem)
            salvar_dados(caminho_doadores, doadores)
            return
        else:
            nova_triagem['documentos'] = 'Doador com toda a documentacao necessaria'
            print('Requisito atendido com sucesso!')
            
        saude_boa = leiaint('Você está se sentindo bem hoje? (1 - Sim/2 - Não): ')
        if saude_boa == 1:
            nova_triagem['saude'] = 'Boa'
            print('Requisito de saúde atendido com sucesso!')
        else:
            nova_triagem['saude'] = 'Ruim'
            nova_triagem['status'] = 'Reprovado'
            print('Triagem encerrada por questão de saúde. Favor tente novamente em outro dia!.')
            doadores[cpf]['triagem'].append(nova_triagem)
            salvar_dados(caminho_doadores, doadores)
            return
        
        horas_dormidas = leiaint('Dormiu pelo menos 6h nas últimas 24h? (1- Sim/2 - Não): ')
        if horas_dormidas != 1:
            nova_triagem['sono'] = 'Insuficiente'
            nova_triagem['status'] = 'Reprovado'
            print('O doador não atende ao requisito sono! Favor tente novamente em outro dia!.')
            doadores[cpf]['triagem'].append(nova_triagem)
            salvar_dados(caminho_doadores, doadores)
            return
        else:
            nova_triagem['sono'] = 'Suficiente'
            print('Requisito atendido com sucesso!')

        ingeriu_alcool = leiaint('Ingeriu bebidas alcoólicas nas últimas 12h? (1 - Sim/2 - Não): ')
        if ingeriu_alcool == 1:
            nova_triagem['alcool'] = 'Sim'
            nova_triagem['status'] = 'Reprovado'
            print('O doador não atende ao requisito álcool! Favor tente novamente em outro dia!.')
            doadores[cpf]['triagem'].append(nova_triagem)
            salvar_dados(caminho_doadores, doadores)
            return
        else:
            nova_triagem['alcool'] = 'Não'
            print('Requisito atendido com sucesso!')

        fumo = leiaint('Fumou nas últimas 2h? (1 - Sim/2 - Não): ')
        if fumo == 1:
            nova_triagem['fumo'] = 'Sim'
            nova_triagem['status'] = 'Reprovado'
            print('O doador não atende ao requisito fumo! Favor tente novamente em outro dia!.')
            doadores[cpf]['triagem'].append(nova_triagem)
            salvar_dados(caminho_doadores, doadores)
            return
        else:
            nova_triagem['fumo'] = 'Não'
            print('Requisito atendido com sucesso!')

        # Verificacao de primeira doacao (com a correcao)
        primeira_doacao = leiaint('É a sua primeira doação? (1 - Sim/2 - Não): ')
        nova_triagem['primeira_doacao'] = (primeira_doacao == 1) 

        if primeira_doacao == 1:
            if doadores[cpf]['idade'] > 60:
                nova_triagem['status'] = 'Reprovado'
                print('O doador não pode realizar a primeira doação com mais de 60 anos!')
                doadores[cpf]['triagem'].append(nova_triagem)
                salvar_dados(caminho_doadores, doadores)
                return
            else:
                print('Idade válida para primeira doação!')
        else:
            print('Doador experiente. Prosseguindo ...')

        print(linha())
        print('A seguir, uma lista de condições que podem impedir a doação: ')
        for condicao, descricao in CONDICOES_IMPEDITIVAS:
            print(f' - {condicao.capitalize()}: {descricao}')
        print(linha())

        doenca_impeditiva = leiaint('Você possui alguma dessas condições? (1 - Sim/2 - Não): ')
        if doenca_impeditiva == 1:
            nova_triagem['doenca_impeditiva'] = 'Sim'
            nova_triagem['status'] = 'Reprovado'
            print('O doador possui uma doença/condição impeditiva para doação!')
            doadores[cpf]['triagem'].append(nova_triagem)
            salvar_dados(caminho_doadores, doadores)
            return
        else:
            nova_triagem['doenca_impeditiva'] = 'Não'
            print('Nenhuma doença impeditiva declarada!')

        
        print(linha())
        print('Parabéns! Você atende a todos os requisitos da Triagem!')
        nova_triagem['status'] = 'Aprovado'
        doadores[cpf]['triagem'].append(nova_triagem)
        salvar_dados(caminho_doadores, doadores)
        print(f'O status de doação de {doadores[cpf]["nome"]} foi atualizado para "Aprovado".')
        input('Pressione Enter para continuar...')
