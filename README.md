# Desafio MBA Engenharia de Software com IA - Full Cycle
```markdown
Este projeto utiliza Python, OpenAI, embeddings, LangChain, PostgreSQL com pgVetor e Docker para criar um chat que responde perguntas sobre o conteúdo de um arquivo PDF.

## Funcionalidades

- Leitura de um arquivo PDF
- Indexação do conteúdo usando embeddings e LangChain
- Armazenamento dos dados em PostgreSQL com extensão pgVetor
- Interface de chat para perguntas e respostas sobre o PDF

## Pré-requisitos

- Python 3.8+
- Docker e Docker Compose
- Conta e chave de API da OpenAI
```
## Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/felipepossari/mba-ia-desafio-ingestao-busca.git
   cd mba-ia-desafio-ingestao-busca
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**<br>
   Renomear o arquivo `.env.example` na raiz do projeto para `.env` e adicionar sua chave da OpenAI:
     ```
     OPENAI_API_KEY=sua_openai_api_key
     ```

5. **Suba o banco de dados com Docker Compose:**
   ```bash
   docker compose up -d
   ```

6. **Ingestão do PDF:**<br>
   Execute o script de ingestão:
     ```bash
     python src/ingest.py
     ```

7. **Inicie o chat:**
   ```bash
   python src/chat.py
   ```

Agora você pode interagir com o chat e fazer perguntas sobre o conteúdo do PDF!

## Observações

- Certifique-se de que o banco de dados está rodando antes de executar os scripts.
- O projeto utiliza a extensão pgVetor no PostgreSQL para armazenar e buscar embeddings.