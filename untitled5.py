# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:47:17 2021

@author: takumi
"""

import streamlit as st

import pandas as pd

st.title('セリーグ打者記録')
DATA_URL=('pandas_sample.csv')
DATE_COLUMN='datepep'

def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase=lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',)
    return data

data_load_state=st.text('Loading data...')
data=load_data(10000)
data_load_state.text('Loading data...done!')


st.dataframe(data.style.highlight_max(axis=0),width=900,height=1000)

