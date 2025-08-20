from uteis.arquivos import carregar_dados, salvar_dados
from funcoes_principais.config import caminho_doadores
from funcoes_principais.interface import *

def editar_doador():
    limpar_tela()
    cabecalho('Editar Doador'.center(45))
    print(linha())

    doadores = carregar_dados(caminho_doadores)
    cpf = str(leiaint('Digite o CPF do doador que deseja editar: '))

    if cpf not in doadores:
        print('Doador não encontrado.')
        print(linha())
        return
    else:
        print(f'Edição do doador: {doadores[cpf]["nome"]}')
        print(linha())

        mudou_dados = False

        while True:
            print('Selecione o campo que deseja editar: ')
            print('1 - Nome')
            print('2 - Idade')
            print('3 - Peso')
            print('4 - Sexo')
            print('5 - Tipo Sanguíneo')
            print('6 - Telefone')
            print('7 - Email')
            print('8 - Sair')   
            opcao = leiaint('Escolha uma opção: ')
            print(linha())

            if opcao == 1:
                novo_nome = input('Digite o nome atualizado do Doador: ')
                doadores[cpf]["nome"] = novo_nome
                mudou_dados = True
                print('Nome atualizado com sucesso.')
            elif opcao == 2:
                nova_idade = leiaint('Digite a nova idade do Doador: ')
                doadores[cpf]["idade"] = nova_idade
                mudou_dados = True
                print('Idade atualizada com sucesso.')  
            elif opcao == 3:
                novo_peso = leiafloat('Digite o novo peso do Doador (em kg): ')
                doadores[cpf]["peso"] = novo_peso
                mudou_dados = True
                print('Peso atualizado com sucesso.')
            elif opcao == 4:
                novo_sexo = input('Digite o novo sexo do Doador (M/F): ')
                doadores[cpf]["sexo"] = novo_sexo
                mudou_dados = True
                print('Sexo atualizado com sucesso.')
            elif opcao == 5:
                novo_tipo_sanguineo = input('Digite o novo tipo sanguíneo do Doador: ')
                doadores[cpf]["tipo_sanguineo"] = novo_tipo_sanguineo
                mudou_dados = True
                print('Tipo sanguíneo atualizado com sucesso.') 
            elif opcao == 6:
                novo_telefone = input('Digite o novo telefone do Doador: ')
                doadores[cpf]["telefone"] = novo_telefone
                mudou_dados = True
                print('Telefone atualizado com sucesso.')   
            elif opcao == 7:
                novo_email = input('Digite o novo email do Doador: ')
                doadores[cpf]["email"] = novo_email
                mudou_dados = True
                print('Email atualizado com sucesso.')  
            elif opcao == 8:
                break

            print(linha())
        
        if mudou_dados:
            salvar_dados(caminho_doadores, doadores)
            print('Dados do doador atualizados com sucesso.')
        else:
            print('Nenhuma alteração foi feita nos dados do doador.')   

        print(linha())
        input('Pressione Enter para continuar...')



