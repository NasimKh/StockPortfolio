#func.py
json_path= 'exchange_rate20201115-215236.txt'
happiness_path = 'wiki_happiness_score.csv'
currency_path = 'currency_list.csv'

def api_to_df(json_path):
    df_json=pd.read_json(json_path)
    df_json.reset_index(inplace=True)
    df=pd.json_normalize(df_json['rates'])
    df[['start_at','base','date']]=df_json[['start_at','base','index']].values
    return df


def happiness_to_df(happiness_path):
    df2= pd.read_csv(happiness_path)
    df2.rename(columns={"[].1": "country", "['Score']": "score"})
    return df2[['country','score']]

def currency_to_df(currency_path):
    df= pd.read_csv(currency_path)
    df=df['A'].reset_index()
    df.rename(columns={"level_0": "country", "level_1": "score",'A':'currency'},inplace = True)
    return df

