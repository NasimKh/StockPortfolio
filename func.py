#func.py
import requests
import pandas as pd
import datetime

json_path= 'exchange_rate20201115-215236.txt'
happiness_path = 'wiki_happiness_score.csv'
currency_path = 'currency_list.csv'

def api_to_df(json_path):
    df_json=pd.read_json(json_path)
    df_json.reset_index(inplace=True)
    df=pd.json_normalize(df_json['rates'])
    df[['start_at','base','date']]=df_json[['start_at','base','index']].values
    df.set_index(df.date, inplace=True)
    # filling values with forward fill
    df=df.resample('D').fillna('ffill')
    #df.drop(columns=['date'], inplace = True)
    #df = df.rename_axis('date').reset_index()
    #df = DataFrame.set_index('date')

    return df


def happiness_to_df(happiness_path):
    df= pd.read_csv(happiness_path)
    df.rename(columns={"[].1": "country", "['Score']": "score"} , inplace = True)
    return df[['country','score']]


def currency_to_df(currency_path):
    df= pd.read_csv(currency_path)
    df.dropna(inplace=True)
    df=df['A'].reset_index()
    df.rename(columns={"level_0": "country", "level_1": "score",'A':'currency'},inplace = True)
    return df

# def currency_to_df(currency_path):
#     df= pd.read_csv(currency_path)
#     df=df['A'].reset_index()
#     df.rename(columns={"level_0": "country", "level_1": "score",'A':'currency'},inplace = True)
#     return df

def country_currency_code(country_name , cur_df):
    """ Looks up the country currency code from a scraped list

        Args: counry_name :Could be a list
        returns : currency_code
    """
    country_name = [x.lower() for x  in country_name]
    currency_code = cur_df[cur_df['country'].str.lower().isin(country_name)].currency.values.tolist()
    #currency_code = cur_df[cur_df['country'].str.lower().isin(country_name)].currency.values.tolist()
    return currency_code

def currency_change_rate(df , country_currency_code , date1,date2 ):
    """Calculates the currency change between two dates
    """
    fx_rate1 = df.loc[date1][country_currency_code]
    fx_rate2 = df.loc[date2][country_currency_code]
    change_rate = fx_rate2 - fx_rate1
    return change_rate

def scrape_exchange_api(url , write_to_file):
    r = requests.get(url)
    date_scraped = datetime.datetime.now().strftime("%Y%m%d")
    save_path = write_to_file +  date_scraped + '.txt'
    open(save_path, 'wb').write(r.content)


def portfolio_change_value_per_year(portfolio , api_to_df_df ):
    '''plot the change in value of our portfolio in
    EUR throughout 2019. Showing min and max value
    '''
    change_inval=portfolio.portfolio_to_currency(api_to_df_df.USD,'EUR')
    dfchanges= pd.DataFrame(change_inval)
    plt.figure(figsize=(20,10))

#ax = fig.add_subplot(111)
    # ploting with
    dfchanges.plot()
    minval=dfchanges[dfchanges.EUR==dfchanges.EUR.min()]
    minx=minval.index[0].strftime('%Y-%m-%d')
    miny= minval.EUR.values[0]

    maxval=dfchanges[dfchanges.EUR==dfchanges.EUR.max()]
    maxx=maxval.index[0].strftime('%Y-%m-%d')
    maxy= maxval.EUR.values[0]

    text= "x={}, y={}".format(minx, miny)
    plt.annotate(text, xy=(minx, miny) )

    #ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)
    text= "x={}, y={}".format(maxx, maxy)
    plt.annotate(text, xy=(maxx, maxy) )
    #plt.annotate('max ', xy=(maxval.index[0], maxval.EUR))

    ax.set_ylim(0,20)
    plt.show()









