# necessario intalação investpy

# importação da biblioteca
import investpy as inv

# coleta de 1_000 ativos
inv.get_stocks_overview(country='Brazil', as_json=False, n_results= 1_000)

# ativo especifico
ativo = 'PETR4'

# ativo da Petrobras
inv.get_stock_company_profile(ativo, country='Brazil')

# informações do demonstrativo
inv.get_stock_financial_summary(ativo, 
                                country='Brazil', 
                                summary_type='income_statement', 
                                period='quarterly')

# informações fluxo de caixa
inv.get_stocks_information(ativo, 
                           country='Brazil', 
                           as_json=False).transpose()

# indicadores
# config_ativo
petr = inv.search_quotes(text= 'petrobras', 
                         products=['stocks'], 
                         countries=['Brazil'], 
                         r_results=1)
#print(petr)
petr.retrieve_technical_indicators(interval='daily')