# SGBS - Sistema de Gerenciamento de Banco de Sangue

## 🎯 Objetivo do Projeto
O Sistema de Gerenciamento de Banco de Sangue (SGBS) é uma aplicação em Python desenvolvida para auxiliar na administração de um banco de sangue. O sistema permite cadastrar doadores, realizar triagens, gerenciar o estoque de bolsas de sangue e fornecer consultas rápidas sobre doadores e o inventário de sangue.

## ✨ Funcionalidades
- **Cadastro de Doador:** Permite registrar novos doadores com informações como CPF, nome, idade, peso e tipo sanguíneo.
- **Triagem:** Realiza uma triagem completa baseada em critérios de saúde e hábitos para determinar a aptidão do doador.
- **Consulta de Doador:** Busca e exibe informações detalhadas de um doador, incluindo seu histórico de triagens.
- **Edição de Doador:** Atualiza os dados cadastrais de um doador existente.
- **Exclusão de Doador:** Remove permanentemente um doador do sistema.
- **Gerenciamento de Estoque:**
    - **Lançar Doação:** Adiciona uma bolsa de sangue ao estoque após uma doação.
    - **Lançar Saída:** Registra a saída de bolsas de sangue do estoque para uso.
    - **Consultar Estoque:** Exibe a quantidade atual de bolsas de cada tipo sanguíneo e alerta sobre estoques baixos.

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3.x

### Passos
1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/yurigalvao/SIstema-Gerenciamento-Banco-Sangue.git](https://github.com/yurigalvao/SIstema-Gerenciamento-Banco-Sangue.git)
    cd Sistema-Gerenciamento-Banco-Sangue
    ```

2. **Execute o arquivo principal:**
    Abra o terminal e execute o seguinte comando na pasta raiz do projeto:
    ```bash
    python Programa_principal/programa_principal.py
    ```

## 📁 Estrutura do Projeto
- `.vscode/`: Pasta de configurações do Visual Studio Code, inclui o `launch.json` para facilitar a depuração.
- `Programa_principal/`: Contém o arquivo principal que inicializa e executa o sistema.
- `funcoes_principais/`: Módulos com as lógicas de negócio do sistema (cadastro, triagem, edição, etc.).
- `uteis/`: Módulos com funções utilitárias, como manipulação de arquivos JSON.
- `dados/`: Pasta onde os dados dos doadores e do estoque são armazenados em arquivos JSON.
- `__pycache__/`: Pastas e arquivos criados automaticamente pelo Python para otimizar a execução. Podem ser ignorados.
- `.gitattributes`: Arquivo de configuração do Git.
- `.gitignore`: Lista arquivos e pastas que o Git deve ignorar (como as pastas `__pycache__`).
- `LICENSE`: Arquivo que especifica a licença de uso do seu código.
- `README.md`: Este arquivo, com informações sobre o projeto.
- `launch.json`: Arquivo de configuração de depuração para o VS Code.

---

**Autor:** Yuri Galvão
