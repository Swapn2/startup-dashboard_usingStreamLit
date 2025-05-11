import streamlit as st
import pandas as pd

st.title("Welcome to our custom app")
st.header("i am learning Streamlit")
st.subheader("i am loving it!")
st.write('Hello swapn this side')

st.markdown("""
### my favorite foods are:
- pizza
- burger
- fries
""")

st.code("""
def foo():
    return "foo**2"
    
x = foo(2)
""")

st.latex('x^2+y^2 = z^2')

df = pd.DataFrame({
    'name':['swapn','swapn','swapn'],
    'marks':[100,90,80],
    'package':[22,41,34]
})
st.dataframe(df)
st.metric('Revenue','Rs 20 lakhs','3%')

st.json({'name':'swapn','age':22})

st.image('stuff.png')

st.sidebar.title('sidebar')
col1, col2 = st.columns(2)
with col1:
    st.button('button1')
    st.image('stuff.png')
with col2:
    st.button('button2')
    st.image('stuff.png')

st.error('error')
st.success('success')
st.warning('warning')
st.info('info')