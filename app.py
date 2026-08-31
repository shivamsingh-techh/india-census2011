import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from altair import Longitude

st.set_page_config(layout="wide")

df=pd.read_csv('india_census.csv')

list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.header('INDIA CENSUS 2011 ')
selected_states=st.sidebar.selectbox('Select State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter ')
    if selected_states=='Overall India':
        fig=px.scatter_map(df,lat='Latitude',lon='Longitude',map_style="carto-positron",size=primary,color=secondary,size_max=30,zoom=4,
    center={"lat": 22.0, "lon": 79.0},height=900,width=900,hover_name='District',hover_data=['State'])
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df=df[df['State']==selected_states]
        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude', map_style="carto-positron", size=primary, color=secondary,
                             size_max=30, zoom=5,
                             center={"lat": 22.0, "lon": 79.0}, height=900, width=900,hover_name='District',hover_data=['State'])
        st.plotly_chart(fig, use_container_width=True)