import pandas as pd
import streamlit as st

from database import view_all_data


def read():
    result = view_all_data()

    df = pd.DataFrame(result, columns=['Artist ID', 'First Name', 'Middle Name', 'Last Name', 'Email', 'Address','Pincode','Phone Number'])
    st.dataframe(df)
