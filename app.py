import streamlit as st
from dbase import DB
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
db=DB()
st.sidebar.title("Flights Analytics")
user_choice=st.sidebar.selectbox('show',['Select any','flights','Analytics'])
if user_choice=='flights':
    st.title('Check Flights')
    col1,col2=st.columns(2)
    city=db.fetch_name()
    with col1:
        source=st.selectbox("Source",city)
    with col2:
        destination=st.selectbox("Destination",city)
    if st.button('Show'):
        data=db.fetch_flights(source,destination) 
        st.dataframe(data)
elif user_choice=='Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)
else:
    st.title('Description')
    
    