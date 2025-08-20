import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
BASE_DIR = os.path.dirname(BASE_DIR)  # Caminho do diretório pai

caminho_doadores = os.path.join(BASE_DIR, 'dados', 'doadores.json')
caminho_estoque = os.path.join(BASE_DIR, 'dados', 'estoque.json')

print(caminho_doadores)
print(caminho_estoque)

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
