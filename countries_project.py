import numpy as np
import pandas as pd

df=pd.read_csv("Countries.csv")

# print(df)
# print(df.shape)
# print(df.info())
# print(df.describe())


#which country has the highest population
# print(df.columns)
# pop=df[df["population"]==df["population"].max()]["country"]
# print(pop)

#give me top 5 countries with highest democratic score

# p=df.sort_values(by = 'democracy_score',ascending=False,inplace = False)
# print(p["country"].head())

#how many total regions are there
# p=df['region'].value_counts().count()
# print(p)

#how many countries lie in Eastern Europe region

# p=df[df['region'] == "Eastern Europe"][ 'country'].count()
# p=df[df['region'] == "Eastern Europe"][ 'country']

# print(p)

#who is the political leader of the 2nd highest populated country

# p=df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader']
# print(p)


# how many countries are there whoes political leaders are unknown
p=df[df['political_leader'].isna()]['country'].count()

print(p)

#how many country have Republic in their full name
count = 0
def counting(txt):
    global count 
    if 'republic' in txt.lower():
        count+= 1
    return txt
df['country_long'] = df['country_long'].apply(counting)
print(count)

#which country in african region has highest population
africa_df = df[df['continent'] == 'Africa']
africa_df[africa_df['population'] == africa_df['population'].max()]['country']