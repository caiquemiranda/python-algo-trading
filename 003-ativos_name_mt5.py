# inportação bibliotecas necessarias
import MetaTrader5 as mt5

# inicialização da plataforma
mt5.initialize()

# todos os ativos 
simbolos = mt5.symbols_get()

'''
#print(simbolos)
#print(len(simbolos))
count = 0
# apenas os 5 primeiros ativos
for simbolo in simbolos:
    print(f"{count}. {simbolo.name}")
    count +=1
    if count == 5:
        break
'''
# USD symbolos

usd_simbolos = mt5.symbols_get('*USD*')
print(len(usd_simbolos))
for simbolo in usd_simbolos:
    print(f"{simbolo.name}")


# encerrando a plataforma
mt5.shutdown()