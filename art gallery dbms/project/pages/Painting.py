import streamlit as st
import pymysql

from create_p import create
from delete_p import delete
from read_p import read
from update_p import update
from painting_analytics import painting_analytics


mydb = pymysql.connect(host='127.0.0.1',user='root',passwd='')
c= mydb.cursor()


def main():
    st.title("Painting")
    p_menu = ["Add","View","Update","Remove","Painting analytics"]
    p_choice = st.sidebar.selectbox("Painting", p_menu)

    if p_choice == "Add":
        st.subheader("Enter painting details")
        create()

    elif p_choice == "View":
        st.subheader("Painting details")
        read()

    elif p_choice == "Update":
        st.subheader("Update painting details")
        update()

    elif p_choice == "Remove":
        st.subheader("Remove painting")
        delete()
    

    elif p_choice == "Painting analytics":
        st.subheader("Paintings which haven't been sold but displayed in more than one exhibition")
        painting_analytics()

    else:
        st.subheader(" ")


if __name__ == '__main__':
    main()
