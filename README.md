# ItauChallange

## Visão Geral do Projeto
Uma aplicação web Python usando FastAPI, SQLAlchemy e Alembic para migrações de banco de dados.

---

## Pré-requisitos
- Python 3.12+
- PostgreSQL
- [pipenv](https://pipenv.pypa.io/en/latest/) ou `venv` e `pip`
- Docker & Docker Compose (opcional, para ambiente containerizado)

---

## 1. Clone o Repositório
```bash
git clone <repo-url>
cd ItauChallange
```

---

## 2. Configuração do Ambiente
### Usando venv
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 3. Configure as Variáveis de Ambiente
Crie um arquivo `.env` no diretório `app/` com o seguinte conteúdo:
```env
DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<banco>
OPENROUTER_API_KEY=<sua_chave>
```
- `OPENROUTER_API_KEY` é obrigatória para o endpoint `/v1/chat` funcionar, pois permite a conexão com a OpenRouter API.

Exemplo para desenvolvimento local:
```env
DATABASE_URL=postgresql://roots:batthing@localhost:5432/itautest
OPENROUTER_API_KEY=<sua_chave>
```

---

## 4. Configuração do Banco de Dados
- Certifique-se de que o PostgreSQL está rodando e que o banco/usuário existem.
- Conceda os privilégios necessários ao seu usuário:

```sql
GRANT CREATE, USAGE ON SCHEMA public TO <user>;
GRANT CREATE ON DATABASE <dbname> TO <user>;
```

---

## 5. Executando Migrações Alembic
```bash
# Ative seu ambiente virtual, se ainda não estiver ativo
source .venv/bin/activate

# Defina o DATABASE_URL se não for carregado automaticamente
export DATABASE_URL=postgresql://<usuario>:<senha>@localhost:<porta>/<nomedb>

# Gere a migração inicial (se ainda não existir)
alembic revision --autogenerate -m "Initial migration"

# Aplique as migrações
alembic upgrade head
```

---

## 6. Execute a Aplicação
```bash
export OPENROUTER_API_KEY=<sua_chave>
uvicorn app.main:app --reload
```

A API estará disponível em [http://localhost:8000](http://localhost:8000)

---

## 7. Usando Docker Compose (Opcional)
Se quiser rodar o app e o banco de dados com Docker Compose:
```bash
export OPENROUTER_API_KEY=<sua_chave>
docker-compose up --build
```

---

## 8. Executando Alembic no Docker Compose
Se estiver usando Docker Compose, execute as migrações dentro do container do app:
```bash
docker-compose exec app alembic upgrade head
```

---

## 9. Documentação da API
Quando a aplicação estiver rodando, acesse [http://localhost:8000/docs](http://localhost:8000/docs) para a documentação interativa da API (Swagger UI).

---

## 10. Exemplo de uso do endpoint /v1/chat com curl

```bash
curl -X POST http://localhost:8000/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "usuario123",
    "prompt": "Olá, tudo bem?"
  }'
```

A resposta será um JSON com o histórico salvo, incluindo o texto gerado pelo modelo.

---

## Solução de Problemas
- Certifique-se de que seu banco de dados está rodando e acessível.
- Verifique as strings de conexão no seu `.env` e `alembic.ini`.
- Se receber erros de permissão, confira os privilégios do seu usuário PostgreSQL.

---

## Licença
GNU v3
