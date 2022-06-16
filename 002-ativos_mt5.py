# inportação bibliotecas necessarias
import MetaTrader5 as mt5

# inicialização da plataforma
mt5.initialize()

# ativos 
simbolos = mt5.symbols_total()

# busca por ativos
if simbolos > 0:
    print(f'Total de ativos encontrados: {simbolos}')
else:
    print('Nenhum ativo encontrado.')

# encerrando a plataforma
mt5.shutdown()