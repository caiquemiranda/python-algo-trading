# inportação bibliotecas necessarias
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

# baixando dados pelo yfinance
ativo_df = yf.download('PETR4.SA', start='2020-02-02', end=datetime.datetime.today())

# dataframe com indices dos dados baixados
data_signal = pd.DataFrame(index = ativo_df.index)

# preços baixados 
data_signal['price'] = ativo_df['Adj Close']

# retornos diarios
data_signal['diff_diaria'] = data_signal['price'].diff()

# estrategia
data_signal['signal'] = 0.0
data_signal['signal'] = np.where(data_signal['diff_diaria'] > 0, 1.0, 0.0)

# não repetir orden 
data_signal['position'] = data_signal['signal'].diff

# parametros do backtest
capital_inicial = 1_000.00

# posições dataframe
positions = pd.DataFrame(index= data_signal.index).fillna(0.0)

# postifolio dataframe
portifolio = pd.DataFrame(index= data_signal.index).fillna(0.0)

# adc ativo a dataframe de posições
positions['PETR4'] = data_signal['signal']

# aplicando estrategia
portifolio['positions'] = (positions.multiply(data_signal['price'], axis = 0 )).cumsum()
portifolio['cash'] = capital_inicial - (positions.diff().multiply(data_signal['price'], axis = 0))
portifolio['total'] = portifolio['positions'] + portifolio['cash']

# resultado estratégia
print(portifolio[-1:])