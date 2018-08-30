# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:42:42 2018

@author: sukandulapati
"""

import os
import pandas as pd

foldernames = os.listdir("D:/TGS/etl3/")
dict = {}
for f in foldernames:
    dict[f] = os.listdir("D:/TGS/etl3/" + f)


data1 = [[sentiment, file_name]
        for sentiment, files in dict.items()
        for file_name in files
        ]

df1 = pd.DataFrame(data1, columns=['sentiment', 'file_name'])

df1['file_id'], df1['rating'] = df1['file_name'].str.split('_', 1).str
df1['file_part'], _ = df1['file_name'].str.split('.', 1).str
df1.head()
df1.tail()


neg_df = df1.loc[df1['sentiment'] == 'neg']

pos_df = df1.loc[df1['sentiment'] == 'pos']


def get_dict(files, path):
    my_dict = {}
    for file in files:
        with open(path+file, encoding="utf8") as f:
            items = [i.strip() for i in f.read().split(",")]
        my_dict[file.replace(".txt", "")] = items
        return my_dict
 

#df for positive sentimenet 
files = os.listdir("D:/TGS/etl3/pos/")
path = "D:/TGS/etl3/pos/"

my_dict = get_dict(files,path)

pos_df['value']= pos_df['file_part'].map(my_dict)

pos_df.head()

#df for nagative sentimenet 
files = os.listdir("D:/TGS/etl3/neg/")
path = "D:/TGS/etl3/neg/"
my_dict = get_dict(files, path)

neg_df['value']= neg_df['file_part'].map(my_dict)

neg_df.head()

