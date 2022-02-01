# import libs
from datetime import datetimete
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import yfinance as yf
from bs4 import BeautifulSoup
import seaborn as sns


#%%
url = 'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-brasil-amplo-ibra-composicao-da-carteira.htmhttps://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-brasil-amplo-ibra-composicao-da-carteira.htm'
agent = {'User-Agent':'Mozilla/5.0'}
resposta = requests.get(url, headers=agent)
