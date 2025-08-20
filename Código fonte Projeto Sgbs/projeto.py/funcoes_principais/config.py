import os

caminho_doadores = os.path.join('dados', 'doadores.json')
caminho_estoque = os.path.join('dados', 'estoque.json')


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
