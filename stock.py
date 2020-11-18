# -*- coding: utf-8 -*-

class Stock(object):

    def __init__( self, symbol:str, shares:float, price:float ,currency = 'EUR'):

        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.currency = currency
    def stock_change_other_currency(self):
        pass

    def __str__(self):
         return "{},{},{}".format(self.symbol,self.shares,self.price)

    def __add__(self,other):
        if self.symbol == other.symbol :
                return self.value + other.value

    @property
    def value( self ):
        return self.shares * self.price


class Currency_Dominated_Stock(object):

    def __init__( self, symbol:str, shares:float, price:float , currency : str ):

        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.currency =  currency

    @property
    def value( self  ):
        return self.shares * self.price

class Currency_asset(object):

    def __init__( self, asset:float ,currency :str):

        self.asset = asset
       # self.shares = shares
       # self.price = price
        self.currency = currency

    @property
    def value( self ):
        return self.asset
