import streamlit as st
import pandas as pd

df = pd.read_csv('startup_clean.csv')
def load_investors_details(investor):
    st.title(investor)
#     load the recent investments of the investor
    last5_df = df[df['investors'].str.contains(investor)][['date','startup','vertical','city','amount']]
    st.subheader('Recent investments')
    st.dataframe(last5_df)

# st.dataframe(df)

st.sidebar.title('startup Funding Analysis')

option = st.sidebar.selectbox('select one ',['overall analysis','startup','Investor'])

if option == 'overall analysis':
    st.title('overall analysis')
elif option == 'startup':
    st.sidebar.selectbox('select startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('find startup details')
    st.title('startup analysis')
else:
    selected_investor = st.sidebar.selectbox('select investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('investor analysis')
    if btn2:
        load_investors_details(selected_investor)

    # st.title('investor analysis')
