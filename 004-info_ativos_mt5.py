# inportação bibliotecas necessarias
import MetaTrader5 as mt5

# inicialização da plataforma
mt5.initialize()

# seleção do ativo
ativo = 'EURUSD'
simbolos = mt5.symbol_select(ativo, True)

# informações do ativo
info_simbolo_dict = mt5.symbol_info(ativo)._asdict()

for p in info_simbolo_dict:
    print(f"{p} = {info_simbolo_dict[p]}")

# encerrando a plataforma
mt5.shutdown()