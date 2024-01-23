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

        st.title('State Stats')

        col1, col2 = st.columns(2)

        with col1:
            st.header("Literacy Rate of: " + selected_state)

            l = {'State_population': state_df['Population'].sum(), 'Male_Literate': state_df['Male_Literate'].sum(),
                 'Female_Literate': state_df['Female_Literate'].sum()}
            df_lit = pd.DataFrame(l, index=[0])

            fig1 = px.bar(df_lit, x=df_lit.index, y=df_lit.columns, barmode='group', text_auto=True)
            st.plotly_chart(fig1)


        with col2:
            st.header(" Major Religion of: " + selected_state)

            r= {'State_population': state_df['Population'].sum(), 'Hindus': state_df['Hindus'].sum(),
                'Muslims': state_df['Muslims'].sum(), 'Christians': state_df['Christians'].sum(),
                'Sikhs': state_df['Sikhs'].sum()}
            df_r = pd.DataFrame(r, index=[0])

            fig2 = px.bar(df_r, x=df_r.index, y=df_r.columns, barmode='group', text_auto=True, log_y=True)
            st.plotly_chart(fig2)

        st.title('District Wise Comparision')


        col3, col4 = st.columns(2)

        with col3:
            st.header("Bar graph for: " + primary)

            fig = px.bar(state_df, y='District', x=primary, text_auto=True,orientation='h')
            st.plotly_chart(fig,use_container_width=True)

        with col4:
            st.header('Bar graph for: ' + secondary)

            fig = px.bar(state_df, y='District', x=secondary, text_auto=True, orientation='h')
            st.plotly_chart(fig,use_container_width=True)










