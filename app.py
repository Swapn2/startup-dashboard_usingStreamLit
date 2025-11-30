import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide",page_title="startup Funding Analysis",page_icon=":moneybag:")
df = pd.read_csv('startup_clean.csv')

df['date'] = pd.to_datetime(df['date'],errors = 'coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year   # st.dataframe(big_df)
def load_investors_details(investor):
    st.title(investor)
#     load the recent investments of the investor
    last5_df = df[df['investors'].str.contains(investor)][['date','startup','vertical','city','amount']]
    st.subheader('Recent investments')
    st.dataframe(last5_df)
    # biggest investments

    col1, col2 = st.columns(2)
    with col1:
        big_df = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest investments')
        fig, ax = plt.subplots()
        ax.bar(big_df.index, big_df.values)
        st.pyplot(fig)
    with col2:
        vertical = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Vertical investments')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical,labels = vertical.index,autopct = "%0.03f%%")
        st.pyplot(fig1)
    # print(df.info())

    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('YoY investments')
    st.dataframe(year_series)
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)
    st.pyplot(fig2)

 # st.dataframe(df)
def load_overall_analysis():
    # total invest amount :
    total = int(df['amount'].sum())
    # st.metric('total',str(total) + 'cr' )

    # max amount infused in the startup
    max_fund = int(df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(1).values[0])
    # st.metric('total', str(max_fund) + 'cr')
    # avg ticklet size
    avg_fund = int(df.groupby('startup')['amount'].sum().mean())

    total_funded_startups = int(df['startup'].nunique())
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total',str(total) + 'cr' )
    with col2:
        st.metric('Max_funds', str(max_fund) + 'cr')
    with col3:
        st.metric('Avg_funds', str(avg_fund) + 'cr')
        #etric('max vertical',df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(1).index[0])
    with col4:
        st.metric('Total_funded_startups', str(total_funded_startups))
        # st.metric('max city',df.groupby('city')['amount'].sum().sort_values(ascending=False).head(1).index[0])
   st.header('MoM Graph : (2015 - 2020)')
   selected_option = st.selectbox('select type', ['total', 'count'])
    
   if selected_option == 'total':
       temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
   else:
       temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    
    # Create Year-Month label
   temp_df['x_axis'] = temp_df['year'].astype(str) + '-' + temp_df['month'].astype(str)
    
   fig3, ax3 = plt.subplots()
   ax3.plot(temp_df['x_axis'], temp_df['amount'])
    
    # 🔥 FIX FOR MESSY X-AXIS
   ax3.tick_params(axis='x', labelrotation=90)     # rotate labels
   ax3.set_xlabel("Year-Month")
   ax3.set_ylabel("Amount")
    
   st.pyplot(fig3)
    # st.header('MoM Graph : (2015 - 2020')
    # selected_option = st.selectbox('select type',['total','count'])
    # if selected_option == 'total':
    #     temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    # else:
    #     temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    # temp_df['x_axis'] = temp_df['year'].astype(str) + '-' + temp_df['month'].astype(str)
    # fig3, ax3 = plt.subplots()
    # ax3.plot(temp_df['x_axis'],temp_df['amount'])
    # st.pyplot(fig3)
   


st.sidebar.title('startup Funding Analysis')

option = st.sidebar.selectbox('select one ',['overall analysis','startup','Investor'])

if option == 'overall analysis':
    load_overall_analysis()

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
