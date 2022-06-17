#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:39:52 2022

@author: poom
"""

import os
import json
import pandas as pd    

def getInstagramUrlFromMediaId(media_id):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    shortened_id = ''
    while media_id > 0:
        remainder = media_id % 64
        # dual conversion sign gets the right ID for new posts
        media_id = (media_id - remainder) // 64;
        # remainder should be casted as an integer to avoid a type error. 
        shortened_id = alphabet[int(remainder)] + shortened_id
    return 'https://instagram.com/p/' + shortened_id + '/'

df = pd.DataFrame(columns=['id', 'caption', 'url'])

for filename in os.listdir('/home/poom/Desktop/insta/json'):
    file = open(os.path.join("/home/poom/Desktop//insta/json", filename))
    data_json = json.load(file)
    id = data_json["id"]
    try:
        caption = data_json["edge_media_to_caption"]["edges"][0]["node"]["text"]
    except:
        print("no caption.")
        caption = "no caption"
    url = getInstagramUrlFromMediaId(int(id))
    temp = pd.DataFrame([[id, caption, url]], columns=['id', 'caption', 'url'])
    df = pd.concat([df, temp])
df.to_csv('/home/poom/Desktop/insta/full.csv', index=False)

filtered = df[df['caption'].str.contains('<KEYWORD1>|<KEYWORD2>|<KEYWORD3>|...')]
filtered.to_csv('/home/poom/Desktop/insta/filtered.csv', index=False)
filtered.url.to_csv('/home/poom/Desktop/insta/urls.txt', sep='\t', header=False, index=False)
