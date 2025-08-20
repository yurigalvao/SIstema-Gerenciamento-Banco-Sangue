import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

caminho_doadores = 'C:\\Users\\yurig\\OneDrive\\Projeto SGBC Python\\projeto.py\\dados\\doadores.json'
caminho_estoque = 'C:\\Users\\yurig\\OneDrive\\Projeto SGBC Python\\projeto.py\\dados\\estoque.json'

from funcoes_principais.interface import *
from uteis.arquivos import verifica_arquivo, salvar_dados, carregar_dados, inicializar_estoque
from funcoes_principais.triagem import triagem
from funcoes_principais.cadastrar_doador import cadastrar_doador
from funcoes_principais.consultar_doador import consultar_doador
from funcoes_principais.editar_doador import editar_doador
from funcoes_principais.excluir_doador import excluir_doador
from funcoes_principais.consultar_estoque import consultar_estoque
from funcoes_principais.lancar_doacao import lancar_doacao_sangue
from funcoes_principais.lancar_saida import lancar_saida



if __name__ == '__main__':
    verifica_arquivo(caminho_doadores, {})
    inicializar_estoque(caminho_estoque)
    doadores = carregar_dados(caminho_doadores)
    estoque = carregar_dados(caminho_estoque)


    while True:
        limpar_tela()
        exibir_menu_principal(['Cadastrar Doador', 'Triagem', 'Consultar Doador', 'Editar Doador', 'Excluir Doador', 'Lançar Doação de Sangue', 'Lançar Saída de Bolsa de Sangue', 'Consultar Estoque', 'Sair'])
        print(linha())
        opcao = leiaint('Escolha uma opção: ')

        if opcao == 1:
            cadastrar_doador()
        elif opcao == 2:
            triagem()
        elif opcao == 3:
            consultar_doador()
        elif opcao == 4:
            editar_doador()
        elif opcao == 5:
            excluir_doador()
        elif opcao == 6:
            lancar_doacao_sangue()
        elif opcao == 7:
            lancar_saida()
        elif opcao == 8:
            consultar_estoque()
        elif opcao == 9:
            cabecalho('Sair'.center(45))
            print('Saindo do sistema... Até logo!')
            break
        else:
            limpar_tela()
            cabecalho('Opção Inválida!'.center(45))
            print('Por favor, escolha uma opção válida.')
            print(linha())
            input('Pressione Enter para continuar...')




