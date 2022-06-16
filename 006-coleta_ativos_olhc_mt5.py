# inportação bibliotecas necessarias
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import time 

# propriedades de exibição dos dados pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)

# inicialização da plataforma
mt5.initialize()

# seleção do ativo
ativo = 'EURUSD'
simbolos = mt5.symbol_select(ativo, True)

# rates de 1Hora 10 barras
olhc_ativo = mt5.copy_rates_from(ativo, mt5.TIMEFRAME_H1, datetime.today(), 10)
#print(olhc_ativo)

olhc_ativo_frame = pd.DataFrame(olhc_ativo)
#print(olhc_ativo_frame)

# transformação do time
olhc_ativo_frame['time'] = pd.to_datetime(olhc_ativo_frame['time'], unit='s')
print(olhc_ativo_frame)

# encerrando a plataforma
mt5.shutdown()