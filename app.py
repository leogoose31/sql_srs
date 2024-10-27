import streamlit as st
import pandas as pd
import duckdb
st.write("Hello world")
data = {"a": [1, 2, 3], "b":[4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["cat", "dog","owl"])

with tab1:
    sql_query = st.text_area(label = "entrez votre input")
    result = duckdb.query(sql_query).df()
    st.write(f"{sql_query}")
    st.dataframe(result)