# inportação bibliotecas necessarias
import MetaTrader5 as mt5
import pandas as pd

# inicialização da plataforma
mt5.initialize()

# informações da conta
informacoes_conta = mt5.account_info()

# trasnformação das informações em dicionario
informacoes_conta_dict = informacoes_conta._asdict()

'''
# visualização dos valores
print(informacoes_conta_dict)

for p in informacoes_conta_dict:
    print(f"{p} = {informacoes_conta_dict[p]}")
print('')
'''

# transformação em dataframe e visualização do dataframe
data_frame = pd.DataFrame(list(informacoes_conta_dict.items()), columns=['proprety', 'value'])
print("informacoes da conta data_frame")
print(data_frame)

# encerrando a plataforma
mt5.shutdown()