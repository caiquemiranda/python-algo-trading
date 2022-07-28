# instalaçoes necessarias
# !pip install yfinance
# !pip install fbprophet

# importação das bibliotecas necessarias
import matplotlib.pyplot as plt
from fbprophet import Prophet
from datetime import datetime
import yfinance as yf
import pandas as pd
import numpy as np

# importando os dados MGLU3 
data = yf.download('MGLU3.SA', start='2018-01-01', end=datetime.today())

# preparando os dados 
df_ativo = pd.DataFrame()
df_ativo['y'] = data['Close']
df_ativo['ds'] = data.index

# treinando o modelo
model = Prophet(daily_seasonality=True)
model.fit(df_ativo)

# previsoes
futuro = model.make_future_dataframe(periods= 35)
previsoes = model.predict(futuro)

# visialização grafica
model.plot(previsoes)