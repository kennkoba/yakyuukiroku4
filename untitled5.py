# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:47:17 2021

@author: takumi
"""

import streamlit as st
import plotly.express as px

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

erea_list =data['球団'].unique()
selected_erea=st.sidebar.selectbox('表示する球団を選択:',erea_list)

df=data[data['球団']== selected_erea]
selected_erea = st.multiselect('グラフに表示する球団を選択', erea_list, default='巨人')
df=data[(data['球団'].isin(selected_erea))]
st.write(px.bar(df,x='選手名',y='打率',title='打率'))
st.write(px.bar(df,x='選手名',y='本塁打',title='本塁打'))
st.write(px.bar(df,x='選手名',y='打点',title='打点'))
st.write('Sportsnavi プロ野球個人成績参照')
