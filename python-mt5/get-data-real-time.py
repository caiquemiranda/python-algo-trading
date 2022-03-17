import MetaTrader5 as mt5
from time import sleep
from datetime import datetime
import pytz
import pandas as pd

if not mt5.initialize():
    print('initialize() falhou')
    mt5.shutdown()

while True:
    ativo = 'EURUSD'
    timezone = pytz.timezone("Etc/UTC")
    utc_from = datetime(2022, 3, 10, tzinfo=timezone)

    df = mt5.copy_ticks_from(ativo, datetime(2022, 3, 10),1000000000, mt5.COPY_TICKS_ALL)
    df = pd.DataFrame(df)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.drop(['flags', 'time', 'time_msc','volume', 'volume_real','last'], axis = 1, inplace=True)

    last=df[-1:]
    print(last)
    #sleep()