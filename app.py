import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('India.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("India Census Data Viz")

selected_state = st.sidebar.selectbox('Select a State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[4:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[4:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents Primary Parameter')
    st.text('Color represents Secondary Parameter')

    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=4,
                                size=primary, color=secondary, mapbox_style='carto-positron',
                                width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)

    else:

        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6,
                                size=primary, color=secondary, mapbox_style='carto-positron',
                                width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)



