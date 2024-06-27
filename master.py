import streamlit as st
import pandas as pd

# To run - streamlit run master.py
st.title("Doing Streamlit")
st.header("Random header")
st.write("Hello world")

df = pd.DataFrame({
    'Name' : ['John' , 'Adam' , 'Bob' , 'Mary'],
    'Marks' : [34,89,10,90]
})

# st.write(df)
st.write(df.head(2))
st.write(df.columns)
st.write("Description of the data : ")
st.write(df.describe())

st.write("Visualization")
st.line_chart(df['Marks'])
