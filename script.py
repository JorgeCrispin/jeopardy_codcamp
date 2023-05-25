import pandas as pd
import numpy as np
import re

pd.set_option('display.max_colwidth', -1)
df = pd.read_csv('jeopardy.csv')
#print(df.head())

#print(df.columns)
df.rename(columns={" Air Date": "Air Date",' Round':'Round',' Category':'Category',' Value':'Value',' Question':'Question',' Answer':'Answer'},inplace=True)
#print(df.columns)
#print(df.Value)
#print(len(df))
#print(len(df.Value))
no_none = []
for i in df.Value:
  new = i.replace('None','200')
  no_none.append(new)

no_coma = []
for i in no_none:
  new = i.replace(',', '')
  no_coma.append(new)

no_dollar = []
for i in no_coma:
  new = i.replace('$','')
  no_dollar.append(new)

 
df.Floats = no_dollar
#df.Value = df.Value.fillna(0)
df.Floats = pd.to_numeric(df.Floats,errors = 'coerce')
#print(df.Value)
def filter(data,column_name,string):
  return data[data[column_name].str.contains(string)]

print(filter(df,'Question',"King"))
df['Floats'] = df.Floats
print(df.Value,df.Floats)
df['Floats'] = df['Floats'].fillna(200.00)
print("Average prize: ",round(df.Floats.mean(),2))
def count_unique_ans_2questions(data):
  return df['Answer'].value_counts()
print(count_unique_ans_2questions(filter))

