import MetaTrader5 as mt5
import time
from datetime import datetime
import pytz

if not mt5.initialize():
    print('initialize() falhou')
    mt5.shutdown()

def ordem_compra(ativo, quantidade=1, sl1=300, tp1=30):
    
    lot = float(quantidade)
    symbol = ativo
    price = mt5.symbol_info_tick(symbol).last
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
    resultado = mt5.order_send(request)
    print('ordem de Compra enviada')
    return resultado

def ordem_venda(ativo, quantidade=1, sl1=300, tp1=30):
    
    lot = float(quantidade)
    symbol = ativo
    price = mt5.symbol_info_tick(symbol).last
    point = mt5.symbol_info(symbol).point
    deviation = 0

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

