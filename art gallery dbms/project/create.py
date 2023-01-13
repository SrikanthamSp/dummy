import streamlit as st
from database import add_data


def create():

    artist_id = st.text_input("ARTIST_ID")
    artist_fname = st.text_input("FIRST NAME")
    artist_mname = st.text_input("MIDDLE NAME")
    artist_lname = st.text_input("LAST NAME")
    artist_email = st.text_input("EMAIL")
    artist_addr = st.text_input("ADDRESS",max_chars=100)
    artist_pin = st.text_input("PIN CODE")
    artist_phone = st.text_input("PHONE NUMBER")
    if st.button("Add"):
        try:
            add_data(artist_id, artist_fname, artist_mname, artist_lname, artist_email, artist_addr, artist_pin, artist_phone)
            st.success("Successfully added artist: {}".format(artist_fname,artist_lname))
        except:
            st.error("Artist ID {} already exists".format(artist_id))