import pandas as pd
import streamlit as st
from database import view_all_paintings


def read():
    result = view_all_paintings()

    df = pd.DataFrame(result, columns=['Painting_ID', 'Title', 'Description', 'Year', 'Type','Cost','Artist ID','Sold in exhibition ID','Customer ID'])

    st.dataframe(df)
