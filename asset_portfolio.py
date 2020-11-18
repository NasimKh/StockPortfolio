# -*- coding: utf-8 -*-

class AssetPortfolio(object):

    def __init__( self, *args, **kwargs ):

        self.portfolio = list()

    def add( self, stock ):

        self.portfolio.append(stock)

    def add(self ,Currency_Dominated_Stock ):

        self.portfolio.append(Currency_Dominated_Stock)

    def add(self,Currency_asset):

        self.portfolio.append(Currency_asset)


    def get_stock(self):
        port_stocks = []
        for item in self.portfolio:
            port_stocks.append(item)
        return port_stocks

    @property
    def get_currency_in_portfolio(self):
        lst=[]
        for s in self.portfolio:
            lst.append(s.currency) if s.currency not in lst else lst
        return lst


    def value_all( self ):

        v = 0

        for s in self.portfolio:

            v += s.value


        return v

    @property
    def value( self ):
        'calculates the value in different currencies'
        v = 0
        dic={}
        currency_list = self.get_currency_in_portfolio

        for currency in currency_list:
            v=0
            for s in self.portfolio:

                if s.currency == currency :
                    v += s.value
                dic[currency] = v
        return dic


    def portfolio_to_currency(self , exchange_rate,to_currency):
        'calculates the value of portfolio in one Currency(to_currency) '

        dic =self.value.copy()
        v = 0

        for key, value in self.value.items():
            v = 0
            if key != to_currency:
                v = value * exchange_rate
                dic.pop(key, None)
                dic[to_currency] += v

        return dic

    @property
    def average_stock(self):
        'Creating a df from the stocks'
        df = pd.DataFrame(columns = ['symbol','shares', 'price','currency'])
        i= 0
        for s in self.portfolio:
            if type(s).__name__ == 'Stock':
                i+=1
                #df.loc[i] = ['name' + str(i)] + list(randint(10, size=2))
                df.loc[i]=[ s.symbol,s.shares, s.price,s.currency]

        grouped=df.groupby(['symbol','currency']).sum().reset_index()
        grouped['value']=grouped['shares'] * grouped['price']
        average_stock_price = grouped['value'].sum()/grouped['shares'].sum()

        return average_stock_price, grouped['shares'].sum() ,list(grouped['currency'].unique())


    @property
    def value_asset( self ):
        'calculates the value in different currencies'
        v = 0
        dic={}
        currency_list = self.get_currency_in_portfolio

        for currency in currency_list:
            #v=0
            for s in self.portfolio:
                v=0
                if s.currency == currency :
                    if type(s).__name__ == 'Currency_asset' :
                        v += s.value
                        dic['Currency_asset' ,currency] = v
                    elif type(s).__name__ == 'Currency_Dominated_Stock':
                        v += s.value
                        dic['Currency_Dominated_Stock' ,currency] = v
        return dic


    def consolidate( self ):
        print( self.average_stock , self.value_asset)




#             elif type(s).__name__ == 'Currency_asset'  :
#                 ca += s.value
#             else :
#                 cds += s.value * s.currency



       # raise Exception("NotImplementedException")


# portfolio = AssetPortfolio()
# portfolio.add( Stock('ABC',200,4) )
# portfolio.add( Stock('DDW',100,10) )
# portfolio.add( Stock('DDW',100,10) )
# portfolio.add(Currency_asset(10,'$'))
# portfolio.add(Currency_Dominated_Stock('DDW',100,10,'EUR'))
