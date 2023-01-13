import pandas as pd
import streamlit as st
from database import view_all_paintings, view_painting_ids, delete_painting


def delete():
    result = view_all_paintings()
    df = pd.DataFrame(result, columns=['Painting_ID', 'Title', 'Description', 'Year', 'Type','Cost','Artist ID','Sold in exhibition ID','Customer ID'])
    with st.expander("Current data"):
        st.dataframe(df)

    p_list = [i[0] for i in view_painting_ids()]
    selected_p = st.selectbox("Painting to Delete", p_list)
    st.warning("Do you want to remove painting #{}".format(selected_p))
    if st.button("Delete"):
        delete_painting(selected_p)
        st.success("Artist has been removed successfully")
    new_result = view_all_paintings()
    df2 = pd.DataFrame(new_result, columns=['Painting_ID', 'Title', 'Description', 'Year', 'Type','Cost','Artist ID','Sold in exhibition ID','Customer ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)