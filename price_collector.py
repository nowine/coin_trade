#coding=utf-8
from websocket import create_connection
import gzip
import time
import json
import sys

from conf import huobi_config, hadax_config

# HUOBI_WSS = 'wss://api.huobipro.com/ws'
# HADAX_WSS = 'wss://api.hadax.com/ws'

def get_ws_conn(config):
    while True: 
        try: 
            ws = create_connection(config.WSS)
            return ws
        except Exception as e:
            print(e)
            print('Connection error, please retry')
            time.sleep(5)


def gen_request(config, opt='sub', dataType='KLINE', symbol='BTCUSDT', period='1min', step='step0'):
    req = {'id': 'id10', }
    if dataType == 'KLINE':
        tradeStr = config.KLINE.format(symbol=symbol, period=period)
    elif dataType == 'MARKET_DEPTH': 
        tradeStr = config.MARKET_DEPTH.format(symbol=symbol, step=step)
    elif dataType == 'TRADE_DETAIL':
        tradeStr = config.TRADE_DETAIL.format(symbol=symbol)
    elif dataType == 'MARKET_DETAIL':
        tradeStr == config.MARKET_DETAIL.format(symbol=symbol)
    else:
        return None 

    req[opt] = tradeStr
    return json.dumps(req)

def rec_messge(ws, init_req, follow_up=print):
    ws.send(init_req)
    while(1):
        orig = ws.recv()
        result = gzip.decompress(orig).decode('utf-8')
        if result[:7] == '{"ping"':
            resp = '"{pong":' + result[8:21]
            ws.send(resp)
            ws.send(init_req)
        else:
            follow_up(result)


if __name__ == '__main__':
    if sys.argv[1] == 'HB':
        ws = get_ws_conn(huobi_config)
    if sys.argv[1] =='HX':
        ws = get_ws_conn(hadax_config)
    req = gen_request(hadax_config, symbol=sys.argv[2],  dataType=sys.argv[3])
    rec_messge(ws, req)


