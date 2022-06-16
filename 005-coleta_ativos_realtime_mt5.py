# inportação bibliotecas necessarias
import MetaTrader5 as mt5
import time 

# inicialização da plataforma
mt5.initialize()

# seleção do ativo
ativo = 'EURUSD'
simbolos = mt5.symbol_select(ativo, True)

while(True):
    print(mt5.symbol_info_tick(ativo).last)
    # 2 segundos de pausa
    time.sleep(2)

# encerrando a plataforma
mt5.shutdown()