import streamlit as st
from database import add_painting


def create():

    p_id = st.text_input("PAINTING ID")
    p_title = st.text_input("TITLE")
    p_desc = st.text_input("DESCRIPTION")
    p_year = st.text_input("YEAR")
    p_type = st.text_input("TYPE")
    p_cost = st.text_input("COST")
    artist_id = st.text_input("ARTIST ID")
    if st.button("Add"):
        try:
            add_painting(p_id, p_title, p_desc, p_year, p_type, p_cost, artist_id)
            st.success("Successfully added painting: {}".format(p_title))
        except:
            st.error("Painting ID {} already exists".format(p_id))