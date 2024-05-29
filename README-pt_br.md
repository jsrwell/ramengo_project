# Projeto RamenGo (API)

A API do RamenGo permite que os usuários listem caldos e proteínas disponíveis, e façam um pedido de uma deliciosa refeição de ramen.

## Primeiros Passos

### Pré-requisitos

Make sure you have Python 3.7+ installed on your system.

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/jsrwell/ramengo_project
    cd ramengo_project
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv .venv        # Caso "python" não seja reconhecido, use "python3" ou "py"
    source .venv/bin/activate   # No Windows use `.venv\Scripts\activate`
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration and Secrets

O projeto utiliza variáveis de ambiente para configuração. Você pode definir essas variáveis diretamente no seu ambiente ou criar um arquivo `.env` no diretório raiz do seu projeto. Já existe um arquivo `.env-example` renomeie-o para `.env`. Para este exemplo, a chave da API está escrita diretamente no código no caso de o arquivo `.env` não existir, mas em um cenário real, você gostaria de manter essa chave em segredo.

Este projeto tem duas chaves:
- `API_KEY` - Chave que deve estar em cada requisição para esta API;
- `REDVENTURES_KEY` - Chave interna para gerar o pedido na API externa.

*Mude as chaves se necessário!*

## Avaliação

### 1. Executando a Aplicação

Para executar a aplicação FastAPI, use o seguinte comando:

```bash
uvicorn main:app --reload

# Por padrão, a aplicação será executada em http://127.0.0.1:8000
```

### 2. Testando com o FrontEnd da RedVentures

Abra em seu navegador https://tech.redventures.com.br/ e insira no formulário modal:

- `API url` -> `http://127.0.0.1:8000`
- `API Key` -> `ac5923cd4de19298ce7e2f9dfaa2014a4dd782b1`

*A chave padrão da API é ac5923cd4de19298ce7e2f9dfaa2014a4dd782b1, mas se você definir outra chave no .env, deverá usar a mesma.*

## Estrutura do Projeto

```bash
.
├── .venv           # ambiente virtual
├── .vscode         # configuração do VSCode para Python
├── .env-example    # renomeie para .env para definir seus próprios dados
├── .gitignore      # configuração do Git
│
├── config.py       # Configuração do projeto
├── mocks.py        # Dados mock para lidar com as respostas
├── schemas.py      # Modelos de esquema para respostas
└── main.py         # Módulo principal com rotas e manipuladores da API
```

#### Documentação da API

[Swagger UI](http://127.0.0.1:8000/docs) - Documentação interativa da API (com o projeto rodando localmente)