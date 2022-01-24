import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pytz
from pylab import mpl, plt

if not mt5.initialize():
    print('initialize() falhou')
    mt5.shutdown()

ativo = 'PETR4'

mt5.copy_rates_from_pos(ativo, mt5.TIMEFRAME_M5,0 ,1)

def get_ohlc(ativo, timeframe, n=5):
    ativo = mt5.copy_rates_from_pos(ativo, timeframe, 0, n)
    ativo = pd.DataFrame(ativo)
    ativo['time'] = pd.to_datetime(ativo['time'], unit='s')
    ativo.set_index('time', inplace=True)
    return ativo

dados_ativo = get_ohlc('PETR4', mt5.TIMEFRAME_M5, 7500) #7500 periodos de M5(5 minutos)

dados_ativo.to_csv('dados-ativo.csv') # get dados em csv