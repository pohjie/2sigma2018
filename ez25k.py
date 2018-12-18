# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Mean reversion libraries
import statsmodels.tsa.stattools as ts
from datetime import datetime

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# import module and create and environment
from kaggle.competitions import twosigmanews

# can only call make_env() once per run
env = twosigmanews.make_env()

# returns tuple of market and news training data
(market_train_df, news_train_df) = env.get_training_data()

# get a list of unique assetCodes
assetCodes = market_train_df['assetCode'].unique().tolist()

# Augmented Dickey-Fuller (ADF) Test
# Test statistic should be smaller than critical values
for assetCode in assetCodes:
    interested = market_train_df.loc[market_train_df['assetCode'] == assetCode]
    adf, p_val, usedlag, nobs, crit_val, icbest, resstore = ts.adfuller(interested['close'], 1)
    if p_val < 0.05:
        print(assetCode + " " + str(p_val))