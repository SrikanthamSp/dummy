
import pandas as pd
import streamlit as st
from database import view_all_paintings, view_painting_ids, painting_details, edit_painting


def update():
    result = view_all_paintings()

    df = pd.DataFrame(result, columns=['Painting_ID', 'Title', 'Description', 'Year', 'Type','Cost','Artist ID','Sold in exhibition ID','Customer ID'])
    with st.expander("Current data"):
        st.dataframe(df)
    p_list = [i[0] for i in view_painting_ids()]
    selected_p = st.selectbox("Edit painting", p_list)
    selected_result = painting_details(selected_p)

    if selected_result:
        p_title = selected_result[0][1]
        p_desc = selected_result[0][2]
        p_year = selected_result[0][3]
        p_type = selected_result[0][4]
        p_cost = selected_result[0][5]
        p_artist_id = selected_result[0][6]
        p_siex_id = selected_result[0][7]
        p_c_id = selected_result[0][8]

        
        new_p_title = st.text_input("TITLE",p_title)
        new_p_desc = st.text_input("DESCRIPTION",p_desc)
        new_p_year = st.text_input("YEAR",p_year)
        new_p_type = st.text_input("TYPE",p_type)
        new_p_cost = st.text_input("COST",p_cost)
        new_artist_id = st.text_input("ARTIST ID",p_artist_id)
        new_siex_id= st.text_input("SOLD IN EXHIBITION ID",p_siex_id)
        new_c_id=st.text_input("CUSTOMER ID",p_c_id)

        if st.button("Update"):
            edit_painting(new_p_title, new_p_desc, new_p_year,new_p_type, new_p_cost, new_artist_id, new_siex_id,new_c_id,selected_p)
            st.success("Successfully updated")

    result2 = view_all_paintings()
    df2 = pd.DataFrame(result2, columns=['Painting_ID', 'Title', 'Description', 'Year', 'Type','Cost','Artist ID','Sold in exhibition ID','Customer ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)