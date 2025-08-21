import os


# Define o diretório base do projeto.
# __file__ se refere a este arquivo (config.py).
# os.path.abspath(__file__) fornece o caminho absoluto de config.py.
# A função os.path.dirname() navega para o diretório pai.
# A segunda chamada de os.path.dirname() navega para o diretório raiz do projeto.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
BASE_DIR = os.path.dirname(BASE_DIR)  

# Define os caminhos completos para os arquivos de dados.
# os.path.join() junta o caminho base com as subpastas e o nome do arquivo,
# garantindo que o caminho seja compatível com qualquer sistema operacional (Windows, Linux, etc.).
caminho_doadores = os.path.join(BASE_DIR, 'dados', 'doadores.json')
caminho_estoque = os.path.join(BASE_DIR, 'dados', 'estoque.json')


# Estas linhas imprimem os caminhos para fins de depuração.
# É útil para verificar se o programa está localizando os arquivos corretamente.
print(caminho_doadores)
print(caminho_estoque)

# Dicionário que armazena os valores de estoque mínimo de cada tipo sanguíneo.
# Esta constante garante que o critério de estoque mínimo seja consistente
# em todo o programa.
ESTOQUE_MINIMO = {
    'A+': 20,
    'A-': 10,
    'B+': 20,
    'B-': 10,
    'O+': 25,
    'O-': 15,
    'AB+': 5,
    'AB-': 5
}
