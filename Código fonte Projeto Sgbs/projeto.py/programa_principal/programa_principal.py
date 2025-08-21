"""
Sistema de Gerenciamento de Banco de Sangue (SGBS)

Este é o módulo principal do sistema. Ele é responsável por:
1.  Configurar o ambiente de execução.
2.  Inicializar e carregar os arquivos de dados (doadores e estoque).
3.  Apresentar um menu interativo ao usuário.
4.  Chamar as funções apropriadas com base na escolha do usuário.
5.  Gerenciar o loop principal do programa até que o usuário decida sair.
"""
import sys
import os

# Adiciona o diretório-pai ao caminho de busca do Python
# Isso garente que o programa consiga encontrar os outros módulos (uteis, funcoes_principais).
# É uma solução para o erro "ModuleNotFoundError".
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Nota: As variáveis de caminho abaixo não são mais necessárias se você estiver usando o
# arquivo 'config.py'. Elas são mantidas aqui para referência, mas o ideal é usar as constantes definidas em config.py
caminho_doadores = 'C:\\Users\\yurig\\OneDrive\\Projeto SGBC Python\\projeto.py\\dados\\doadores.json'
caminho_estoque = 'C:\\Users\\yurig\\OneDrive\\Projeto SGBC Python\\projeto.py\\dados\\estoque.json'

# Importa todas as funções e módulos necessários para o menu principal.
# Cada importação traz uma parte da funcionalidade do sistema
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


# o Bloco 'if __name__ == '__main__':' garante que o código dentro dele
# só será executado quando o arquivo for rodado diretamente (como o script principal).
# Isso é uma boa prática para evitar que o código seja executado se o módulo
# for importado em outro lugar. 
if __name__ == '__main__':
    # 1 - Inicialização do sistema
    # Garante que os arquivos de dados existam antes de o programa começar.
    # Se os arquivos não existirem, eles serão criados com dados vazios.
    verifica_arquivo(caminho_doadores, {})
    inicializar_estoque(caminho_estoque)

    # Carrega os dados dos arquivos para a memória, preparando o sistema para as operações
    doadores = carregar_dados(caminho_doadores)
    estoque = carregar_dados(caminho_estoque)

    # 2 - Loop principal do programa
    # O 'while True' cria um loop infinito que só é interrompido quando 
    # o usuário escolhe a opção para sair (opção 9) e o comando 'break' é executado.
    while True:
        limpar_tela()
        exibir_menu_principal(['Cadastrar Doador', 'Triagem', 'Consultar Doador', 'Editar Doador', 'Excluir Doador', 'Lançar Doação de Sangue', 'Lançar Saída de Bolsa de Sangue', 'Consultar Estoque', 'Sair'])
        print(linha())
        opcao = leiaint('Escolha uma opção: ')

        # 3 - Lógica de seleção do menu
        # A estrutura 'if/elif/else' direciona o fluxo do programa para a função correspondente à escolha do usuário
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




