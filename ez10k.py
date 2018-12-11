# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

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

