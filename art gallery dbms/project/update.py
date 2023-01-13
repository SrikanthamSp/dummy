
import pandas as pd
import streamlit as st
from database import view_all_data, view_artist_ids, artist_details, edit_artist


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Artist_ID', 'First name', 'Middle name', 'Last name', 'Email','Address','Pincode','Phone'])
    with st.expander("Current data"):
        st.dataframe(df)
    artists_list = [i[0] for i in view_artist_ids()]
    selected_artist = st.selectbox("Edit artist", artists_list)
    selected_result = artist_details(selected_artist)

    if selected_result:
        artist_id = selected_result[0][0]
        artist_fname = selected_result[0][1]
        artist_mname = selected_result[0][2]
        artist_lname = selected_result[0][3]
        artist_email = selected_result[0][4]
        artist_addr = selected_result[0][5]
        artist_pin = selected_result[0][6]
        artist_phone = selected_result[0][7]


        new_artist_fname = st.text_input("FIRST NAME",artist_fname)
        new_artist_mname = st.text_input("MIDDLE NAME",artist_mname)
        new_artist_lname = st.text_input("LAST NAME",artist_lname)
        new_artist_email = st.text_input("EMAIL",artist_email)
        new_artist_addr = st.text_input("ADDRESS",artist_addr)
        new_artist_pin = st.text_input("PIN CODE",artist_pin)
        new_artist_phone = st.text_input("PHONE NUMBER",artist_phone)
        if st.button("Update"):
            edit_artist(new_artist_fname, new_artist_mname, new_artist_lname, new_artist_email,new_artist_addr,new_artist_pin,new_artist_phone, artist_id)
            st.success("Successfully updated")

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Artist_ID', 'First name', 'Middle name', 'Last name', 'Email','Address','Pincode','Phone'])
    with st.expander("Updated data"):
        st.dataframe(df2)
