Personal Finance Tracker

Um rastreador de finanças pessoais desenvolvido em Python, com duas interfaces — linha de comando e web — que permitem registrar receitas e despesas e visualizar um resumo financeiro filtrado por período.

Funcionalidades
Registro de transações (receita ou despesa) com data, valor, categoria e descrição
Armazenamento persistente em arquivo CSV
Consulta de transações dentro de um intervalo de datas
Resumo automático: total de receitas, total de despesas e saldo líquido do período
Visualização gráfica de receitas e despesas ao longo do tempo
Interface web interativa (Streamlit), além da interface por linha de comando
Como usar
Clone o repositório:
bash
   git clone https://github.com/gusminussi/personal_finance_tracker.git
   cd personal_finance_tracker
Instale as dependências:
bash
   pip install pandas matplotlib streamlit
Execute o programa em uma das duas interfaces:

Linha de comando:

bash
   python main.py

Use o menu interativo para adicionar transações ou consultar um período:

Add a new transaction
View transactions and summary within a date range
Exit

Interface web:

bash
   streamlit run app.py

Abre automaticamente no navegador (localhost:8501), com duas telas:

Add transaction
View transactions
Estrutura do projeto
main.py — Interface por linha de comando (menu interativo)
app.py — Interface web (Streamlit)
storage.py — Classe CSV: leitura e escrita dos dados
analytics.py — Regras de negócio: filtro por período, cálculo de totais e formatação de moeda
charts.py — Construção do gráfico de receitas e despesas
data_entry.py — Funções de entrada e validação de dados do usuário (usadas pela interface de linha de comando)
finance_data.csv — Arquivo onde as transações são armazenadas (gerado automaticamente na primeira execução, não incluído no repositório)
Tecnologias
Python 3
pandas — manipulação e filtragem de dados
csv (biblioteca padrão) — escrita de registros
Matplotlib — visualização gráfica dos dados
Streamlit — interface web interativa