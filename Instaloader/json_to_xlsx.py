#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:02:26 2022

@author: poom
"""

import os
import pandas as pd    

df = pd.DataFrame(columns=['caption', 'url'])

for filename in os.listdir('/home/poom/Desktop/insta/#<KEYWORD>'):
    if '.jpg' in filename:
        continue
    file = os.path.join("/home/poom/Desktop/insta/#<KEYWORD>", filename)
    with open(file) as f:
        contents = f.read()
    caption = contents.split('new_tab')[0]
    url = contents.split('new_tab')[1][:-1]
    temp = pd.DataFrame([[caption, url]], columns=['caption', 'url'])
    df = pd.concat([df, temp])
    
for filename in os.listdir('/home/poom/Desktop/insta/#<KEYWORD>'):
    if '.jpg' in filename:
        continue
    file = os.path.join("/home/poom/Desktop/insta/#<KEYWORD>", filename)
    with open(file) as f:
        contents = f.read()
    caption = contents.split('new_tab')[0]
    url = contents.split('new_tab')[1][:-1]
    temp = pd.DataFrame([[caption, url]], columns=['caption', 'url'])
    df = pd.concat([df, temp])
    
df.to_csv('/home/poom/Desktop/insta/full.csv', index=False)

filtered = df[df['caption'].str.contains('<KEYWORD1>|<KEYWORD2>|<KEYWORD3>')]
filtered.to_csv('/home/poom/Desktop/insta/filtered.csv', index=False)
filtered.url.to_csv('/home/poom/Desktop/insta/urls.txt', sep='\t', header=False, index=False)


