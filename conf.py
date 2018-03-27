#coding=utf-8

class huobi_config(object):
    WSS = 'wss://api.huobipro.com/ws'
    KLINE = 'market.{symbol}.kline.{period}'
    MARKET_DEPTH = 'market.{symbol}.depth.{step}'
    TRADE_DETAIL = 'market.{symbol}.trade.detail'
    MARKET_DETAIL = 'market.{symbol}.detail'


class hadax_config(object):
    WSS = 'wss://api.hadax.com/ws'
    KLINE = 'market.{symbol}.kline.{period}'
    MARKET_DEPTH = 'market.{symbol}.depth.{step}'
    TRADE_DETAIL = 'market.{symbol}.trade.detail'
    MARKET_DETAIL = 'market.{symbol}.detail'
    
