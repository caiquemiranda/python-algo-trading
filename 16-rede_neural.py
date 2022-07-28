# inportação bibliotecas necessarias
import matplotlib.pyplot as plt
from datetime import datetime
import MetaTrader5 as mt5
import statsmodels.api as sm
import seaborn as sns
import pandas as pd
import numpy as np
import random
import talib
import pytz
import time

# rede neural
from sklearn.neural_network import MLPClassifier
import tensorflow as tf
from keras.models import sequential
from keras.layers import Dense
from keras.optimizers import Adam, RMSprop

# configuração parametros do pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
pd.set_option('mode.chained_assignment', None)

# importando e preparando os dados
ativo = 'EURUSD'

mt5.initialize()
mt5.symbol_select(ativo)

df_ativo = mt5.copy_rates_from_pos(ativo, mt5.TIMEFRAME_D1, 0, 5_000)
df_ativo = pd.DataFrame(df_ativo)
df_ativo['time'] = pd.to_datetime(df_ativo['time'], unit='s')
df_ativo = df_ativo.set_index('time')
# print(df_ativo)

# encerrando conexão
mt5.shutdown()

# retorno log
df_ativo['return'] = np.log(df_ativo['close']/df_ativo['close'].shift(1))
df_ativo.dropna(inplace=True)
# print(df_ativo)

cols = []
lags = 5

for lag in range(1, lags + 1):
    
    col = f'lag...{lag}'
    df_ativo[col] = df_ativo['return'].shift(lag)
    cols.append(col)

df_ativo.dropna(inplace=True)
#print(df_ativo)

variaveis_uteis = ['close', 'return']  + cols
df_ativo_new = df_ativo[variaveis_uteis]
df_ativo_new['direction'] = np.where(df_ativo_new['return']> 0, 1, 0)
df_ativo_new

# rede neural
optmizer = Adam(learning_rate=0.0001)

# semente para manter o mesmo valor
def set_seed(seed = 100):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

set_seed()

# modelo
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(lags, )))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optmizer=optmizer, loss='binary_crossentropy', metrics=['accuracy'])

# separação de dados 
cutoff = '2020-09-01'
training_data = df_ativo_new[df_ativo_new.index < cutoff].copy()

# normalização dos dados traning
mean = training_data.mean()
std = training_data.std()
training = (training_data - mean)/std
#print(traing)

# dados test
test_data = df_ativo_new[df_ativo_new.index >= cutoff].copy()
test = (test_data - mean) / std
#print(test)

# treino modelo
model.fit(training[cols], training_data['direction'], ephochs=50, verbose=True, validation_split=0.2, shuffle=False)
result = pd.DataFrame(model.history.history)
#print(result)

# visualização grafica
result[['accuracy', 'val_accuracy']].plot(figsize=(20,10))

# avaliação
model.evaluate(training[cols], training_data['direction'])

# predict
pred = np.where(model.predict(training[cols]) > 0.5, 1, 0)
training_data['prediction'] = np.where(pred > 0, 1, -1)

# strategy
training_data['strategy'] = (training_data['prediction'] * training_data['return'])
training_data[['return', 'strategy']].sum().apply(np.exp)

# soma retornos e visualização dados treino
training_data[['return', 'strategy']].cumsum().apply(np.exp).plot(figsize=(20, 10))

# 
model.evaluate(test_data[cols], test_data['direction'])

# pred test
pred = np.where(model.predict(test[cols]) > 0.5, 1, 0)
test_data['prediction'] = np.where(pred > 0, 1, -1)
test_data['strategy'] = (test_data['prediction'] * test_data['return'])
test_data[['return', 'strategy']].sum().apply(np.exp)

# visualização dados de test
test_data[['return', 'strategy']].cumsum().apply(np.exp).plot(figsize=(20, 10))