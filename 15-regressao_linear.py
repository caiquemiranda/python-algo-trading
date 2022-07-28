# inportação bibliotecas necessarias
import matplotlib.pyplot as plt
from datetime import datetime
import MetaTrader5 as mt5
import statsmodel as sm
import seaborn as sns
import pandas as pd
import numpy as np
import talib
import pytz
import time

# configuração parametros do pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
pd.set_option('mode.chained_assignment', None)

# importando os dados
ativo = 'EURUSD'

mt5.initialize()
mt5.symbol_select(ativo)

df_ativo = mt5.copy_rates_from_pos(ativo, mt5.TIMEFRAME_D1, 0, 5_000)
df_ativo = pd.DataFrame(df_ativo)
df_ativo['time'] = pd.to_datetime(df_ativo['time'], unit='s')

#print(df_ativo)

# visualizando fechamento do ativo
# df_ativo['close'].plot()

pacote_dias = 5

df_ativo['dias_futuro'] = df_ativo['close'].shift( - pacote_dias)
df_ativo['dias_futuro_retornos'] = df_ativo['dias_futuro'].pct_change(pacote_dias)
df_ativo['dias_atuais_retorno'] = df_ativo['close'].pct_change(pacote_dias)

df_ativo.dropna()

corr = df_ativo[['dias_atuais_retorno','dias_futuro_retorno']].corr()

# features com talib
'''

# indicador OBV talib
df_ativo['obv'] = talib.OBV(df_ativo['close'], df_ativo['real_volume'])

features_names = ['dias_atuais_retorno', 'obv']

# média exponencial e rsi

for m in [7, 9, 21, 50, 200]:
    
    # média movel exponencial
    df_ativo['mme ' + str(m)] = talib.EMA(df_ativo['close'].values, timeperiod= m)

    # rsi
    df_ativo['rsi ' + str(m)] = talib.RSI(df_ativo['close'].values, timeperiod= m)


    features_names = features_names + ['mme ' + str(m), 'rsi ' + str(m)]

print(features_names)

df_ativo.dropna()

'''

features = df_ativo[features_names]
target = df_ativo['dias_futuro_retorno']

features_and_target = ['dias_futuro_retorno'] + features_name
features_and_target_df = df_ativo[features_and_target]


# corr
corr = features_and_target_df.corr()
#print(corr)

# correlação
sns.heatmap(corr, annot=True)

linear_features = sm.add_constant(features)

# tamanho treino/test
# treino
len_train = int(0.85 * features.shape[0])
features_train = linear_features[ : len_train]
target_train = target[ : len_train]

# test
features_test = linear_features[len_train : ]
target_test = target[len_train : ]

# modelo
model = sm.OLS(target_train, features_train)
model_rl = model.fit()

# resultados.pvalues
#print(model_rl.pvalues)

# previsões
prev_train = model_rl.predict(features_train)
prev_test = model_rl.predict(features_test)

#plot scatter

# encerrando conexão
mt5.shutdown()