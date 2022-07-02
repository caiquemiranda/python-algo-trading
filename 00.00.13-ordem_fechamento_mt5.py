# inportação bibliotecas necessarias
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import pytz
import time

# configuração parametros do pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
pd.set_option('mode.chained_assignment', None)

# parametros mercado(BOVESP)
abertura = pd.Timestamp(datetime.today().strftime('%Y-%m-%d') + '-10:00:00')
fechamento = pd.Timestamp(datetime.today().strftime('%Y-%m-%d') + '-17:30:00')

# inicialização da plataforma
mt5.initialize()

# seleção do ativo
ativo = 'EURUSD'
symbol = mt5.symbol_select(ativo, True)

# ordem de compra
def ordem_compra(ativo, quantidade=1, sl1=300, tp1=300):
    
    lot = float(quantidade)
    symbol = ativo
    price = mt5.symbol_info_tick(symbol).ask
    point = mt5.symbol_info(symbol).point
    deviation = 0

    request = {
        'action': mt5.TRADE_ACTION_DEAL,
        'symbol': symbol,
        'volume': lot,
        'type': mt5.ORDER_TYPE_BUY,
        'price': price,
        'sl': price - sl1 *point,
        'tp': price + tp1 *point,
        'deviation': deviation,
        'magic': 10132021,
        'comment': 'Ordem de Compra Enviada',
        'type_time': mt5.ORDER_TIME_GTC,
        'type_filling': mt5.ORDER_FILLING_RETURN
    }
    
    # dicionario enviado para ordem de compra
    resultado = mt5.order_send(request)
    print('ordem de Compra enviada')
    return resultado

# ordem de venda
def ordem_venda(ativo, quantidade=1, sl1=300, tp1=300):
    
    lot = float(quantidade)
    symbol = ativo
    price = mt5.symbol_info_tick(symbol).bid
    point = mt5.symbol_info(symbol).point
    deviation = 0

    # dicionario enviado na ordem de venda
    request = {
        'action': mt5.TRADE_ACTION_DEAL,
        'symbol': symbol,
        'volume': lot,
        'type': mt5.ORDER_TYPE_SELL,
        'price': price,
        'sl': price + sl1 * point,
        'tp': price - tp1 * point,
        'deviation': deviation,
        'magic': 10132021,
        'comment': 'Ordem de Venda Enviada',
        'type_time': mt5.ORDER_TIME_GTC,
        'type_filling': mt5.ORDER_FILLING_RETURN
    }
    resultado = mt5.order_send(request)
    print('ordem de Venda enviada')
    return resultado

# ordem de fechamento
def ordem_fechamento(ativo, quantidade, ticket, type_order, magic, deviation):

    if (type_order == 0):
        print('ORDEM DE VENDA - FECHAMENTO')

        request_fechamento = {
            'action': mt5.TRADE_ACTION_DEAL,
            'position': ticket, 
            'symbol': ativo,
            'volume': quantidade,
            'deviation': deviation,
            'magic': magic,
            'type': mt5.ORDER_TYPE_SELL,
            'price': mt5.symbol_info_tick(ativo).bid, 
            'type_time': mt5.ORDER_TIME_GTC,
            'type_filing': mt5.ORDER_FILLING_RETURN,
        }

        resultado = mt5.order_send(request_fechamento)
        print(resultado)

    else:

        print('ORDEM COMPRA - FECHAMENTO')

        request_fechamento = {
            'action': mt5.TRADE_ACTION_DEAL,
            'position': ticket, 
            'symbol': ativo,
            'volume': quantidade,
            'deviation': deviation,
            'magic': magic,
            'type': mt5.ORDER_TYPE_BUY,
            'price': mt5.symbol_info_tick(ativo).ask, 
            'type_time': mt5.ORDER_TIME_GTC,
            'type_filing': mt5.ORDER_FILLING_RETURN,
        }

        resultado = mt5.order_send(request_fechamento)
        print(resultado)

# condição bot
while True:
    # verificação se está em horario de operação bolsa aberta(BOVESPA)
    hora = datetime.now()
    horario_mercado = hora >= abertura and hora <= fechamento

    # ordens e posiçoes 
    ordens_abertas = mt5.orders_total()
    posicoes_abertas = mt5.positions_total()    
    print(f'Ordens abertas: {ordens_abertas}')
    print(f'Posições abertas: {posicoes_abertas}')

    # condições de posições e ordens
    if (ordens_abertas == 0 and posicoes_abertas == 0 ):
        ordem_compra(ativo, 1, 300, 300)
    
    else:
        time.sleep(10)
        info_positions = mt5.positions_get(symbol=ativo)

        if (len(info_positions) > 0):

            # dataframe das ordens abertas
            data_frame_positions = pd.DataFrame(list(info_positions), columns=info_positions[0]._asdict().keys())
            data_frame_positions['time'] = pd.to_datetime(data_frame_positions['time'], unit='s')

            # request enviado para fechamento
            ordem_fechamento(str(data_frame_positions['symbol'][0]),
                             float(data_frame_positions['volume'][0]),
                             int(data_frame_positions['ticket'][0]),
                             data_frame_positions['type'][0],
                             int(data_frame_positions['magic'][0]), 
                             0)

    # visualização das ordem em dataframe
    print(data_frame_positions)
    

# encerrando conexão
mt5.shutdown()