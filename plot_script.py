#plot_script.py


json_path= 'exchange_rate20201115-215236.txt'
happiness_path = 'wiki_happiness_score.csv'
currency_path = 'currency_list.csv'

cur_df= currency_to_df(currency_path)
df = api_to_df(json_path)

fx_rates = []
for i in df.columns[:-3]:
    fx_rates.append(currency_change_rate(df , i , '2019-01-02','2019-12-31' ))


list_country = []
for item in flat_list :
    if  item.find("(") < 0 :
        list_country.append(item)

flat_list = [item for sublist in country_list for item in sublist]

df2= happiness_to_df(happiness_path)
df_scores= df2[df2.country.isin(list_country)]
dff=df_scores.merge(cur_df, on='country')
dff1 = pd.DataFrame(data=fx_rates)
dff1['code']= df.columns[:-3]
final_df=dff1.merge(dff, left_on= 'code' , right_on ='currency')
final_df.rename(columns={0: 'fx_rate'},inplace = True )



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

#df_iris=sns.load_dataset("iris")
plt.figure(figsize=(20,10))
ax = sns.lmplot('score_x', # Horizontal axis
           'fx_rate', # Vertical axis
           data=final_df[final_df['fx_rate']> -5], # Data source
           size = 15,
                fit_reg=True# Don't fix a regression line
            ) # size and dimension

# plt.title('Example Plot')
# # Set x-axis label
# plt.xlabel('Sepal Length')
# # Set y-axis label
# plt.ylabel('Sepal Width')


def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.01, point['y'], str(point['val']),fontsize=10)

label_point( final_df.score_x,final_df.fx_rate, final_df.country, plt.gca())
plt.show()
#enter image description here