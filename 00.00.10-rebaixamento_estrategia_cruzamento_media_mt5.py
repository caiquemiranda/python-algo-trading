# inportação bibliotecas necessarias
from datetime import datetime
import MetaTrader5 as mt5
from pylab import mpl, plt
import pandas as pd
import numpy as np

# configuração parametros do grafico
plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'

# configuração parametros do pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
pd.set_option('mode.chained_assignment', None)

# inicialização da plataforma
mt5.initialize()

# seleção do ativo
ativo = 'EURUSD'
simbolos = mt5.symbol_select(ativo, True)

time_frame = mt5.copy_rates_from(ativo, mt5.TIMEFRAME_D1, datetime.today(), 2_500)
#print(time_frame)

# trasnformação em dataframe
data = pd.DataFrame(time_frame)
# configuração do time
data['time'] = pd.to_datetime(data['time'], unit='s')

# criação dos indicadores
# medias 43(rapida) / 252(lenta)
data['sma_rapida'] = data['close'].rolling(43).mean()
data['sma_lenta'] = data['close'].rolling(252).mean()

# limpeza dos dados Nan
data.dropna(inplace=True)

# seleção de variaveis para backtest
data = data[['close', 'time', 'sma_rapida', 'sma_lenta']]

# time para indice(transformação em serie temporal)
data = data.set_index('time')

'''
# plot do grafico com as médias
data.plot(figsize=(12, 6))
plt.show()

'''

# configurações da estrategia
# estratégia onde sma_rapida acima= 1, sma_lenta acima=-1
data['posicao'] = np.where(data['sma_rapida'] > data['sma_lenta'], 1, -1)

data['posicao'] = data['posicao'].shift(1)
data.dropna(inplace=True)

# plot do grafico com as posições
data.plot(figsize=(12,6), secondary_y='posicao')
#plt.show()

# configuração do backtest

# calculo retornos
data['retornos'] = np.log(data['close']/data['close'].shift(1))
data.dropna(inplace=True)

# calculo retornos estrategia
data['estrategia'] = data['posicao'] * data['retornos']

# retorno simples estratégia
retorno_simples = data[['retornos', 'estrategia']].sum()
print(retorno_simples)

# retorno log estratégia
retorno_log = data[['retornos', 'estrategia']].sum().apply(np.exp) - 1
print(retorno_log)

# print retornos estratégia
data[['retornos', 'estrategia']].cumsum().apply(np.exp).plot(figsize=(12,6))

# retorno acumulado
data['retorno_acumulado'] = data['estrategia'].cumsum().apply(np.exp)
data['soma_max'] = data['retorno_acumulado'].cummax()


# plot dos retornos acumulados
data[['retorno_acumulado', 'soma_max']].dropna().plot(figsize=(12,6))
plt.show()

# variavel rebaixamento
rebaixamento = (data['soma_max'] - data['retorno_acumulado']).max()
drawdown = data['soma_max'] - data['retorno_acumulado']
print(f'Rebaixamento: {rebaixamento:.2f}% ')

# tempo de rebaixamento
temp = drawdown[drawdown == 0]
periodos_rebaixamento = (temp.index[1:].to_pydatetime() - temp.index[:-1].to_pydatetime())

# periodo maximo de rebaixamento
print(periodos_rebaixamento.max())

# encerrando conexão
mt5.shutdown()