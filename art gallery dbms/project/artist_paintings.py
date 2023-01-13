import pandas as pd
import streamlit as st

from database import view_artist_paintings


def artist_paintings():
    result = view_artist_paintings()
    df = pd.DataFrame(result, columns=['Artist ID', 'First Name','Last Name', 'Number of paintings made'])

    st.dataframe(df)
