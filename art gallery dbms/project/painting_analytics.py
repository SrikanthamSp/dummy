import pandas as pd
import streamlit as st

from database import view_painting_analytics


def painting_analytics():
    result = view_painting_analytics()
    df = pd.DataFrame(result, columns=['Painting ID', 'Title','Cost'])

    st.dataframe(df)

