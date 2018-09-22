# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:34:11 2018

@author: oncall
"""

import pandas as pd
import numpy as np

airbnb = pd.read_csv('D:\GreyAtom\DataSet_AirBNB\dc_airbnb.csv')
airbnb_copy = airbnb

our_accomodates = 3

# Funcntion to find the mean price of flats which can accommodate N number of persons. 'N' is a parameter passed.
def price_predict(our_accomodates, airbnb_ds, k, feature):
    np.random.seed(6)
    airbnb_ds['distance'] = abs(airbnb_ds[feature] - our_accomodates)
    airbnb_ds['price'] = airbnb_ds['price'].str.replace(',', '')
    airbnb_ds['price'] = airbnb_ds['price'].str.replace('$', '').astype(float)
    
    airbnb_ds = airbnb_ds.loc[np.random.permutation(len(airbnb_ds))]
    airbnb_filtered = airbnb_ds[airbnb_ds['distance']==0]
    #Mean price of flats accomodating number of individuals == our_accommodates
    mean_price = airbnb_filtered['price'][:k].mean()
    airbnb_filtered['price_error'] = abs (airbnb_filtered['price'] - mean_price)
    RMSE = np.sqrt((airbnb_filtered['price_error']**2).sum()/len(airbnb_filtered))
    return RMSE
    
mean_square_error = price_predict(our_accomodates, airbnb, 5, 'bathrooms')
print (mean_square_error)
