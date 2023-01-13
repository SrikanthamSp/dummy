import pandas as pd
import streamlit as st
from database import view_all_data, view_artist_ids, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Artist_ID', 'First name', 'Middle name', 'Last name', 'Email','Address','Pincode','Phone'])
    with st.expander("Current data"):
        st.dataframe(df)

    artists_list = [i[0] for i in view_artist_ids()]
    selected_artist = st.selectbox("Artist to Delete", artists_list)
    st.warning("Do you want to remove artist #{}".format(selected_artist))
    if st.button("Delete"):
        delete_data(selected_artist)
        st.success("Artist has been removed successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Artist_ID', 'First name', 'Middle name', 'Last name', 'Email','Address','Pincode','Phone'])
    with st.expander("Updated data"):
        st.dataframe(df2)