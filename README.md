# Personal Finance Tracker 💰

Um rastreador de finanças pessoais desenvolvido em Python, que permite registrar receitas e despesas e visualizar um resumo financeiro filtrado por período.

## Funcionalidades

- ✅ Registro de transações (receita ou despesa) com data, valor, categoria e descrição
- ✅ Armazenamento persistente em arquivo CSV
- ✅ Consulta de transações dentro de um intervalo de datas
- ✅ Resumo automático: total de receitas, total de despesas e saldo líquido do período

## Como usar

1. Clone o repositório:
```bash
   git clone https://github.com/gusminussi/personal_finance_tracker.git
   cd personal_finance_tracker
```

2. Instale as dependências:
```bash
   pip install pandas
```

3. Execute o programa:
```bash
   python main.py
```

4. Use o menu interativo para adicionar transações ou consultar um período:
1. Add a new transaction
2. View transactions and summary within a date range
3. Exit

## Estrutura do projeto

- `main.py` — Lógica principal: classe `CSV` (leitura/escrita de dados) e menu interativo
- `data_entry.py` — Funções de entrada e validação de dados do usuário
- `finance_data.csv` — Arquivo onde as transações são armazenadas

## Tecnologias

- Python 3
- [pandas](https://pandas.pydata.org/) — manipulação e filtragem de dados
- csv (biblioteca padrão) — escrita de registros

Próxima melhoria a caminho:

- 📊 Visualização gráfica dos dados com Matplotlib
