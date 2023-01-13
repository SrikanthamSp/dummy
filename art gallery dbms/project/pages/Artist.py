# Importing pakages
import streamlit as st
#import mysql.connector
import pymysql
from create import create
from delete import delete
from read import read
from update import update
from artist_analytics import artist_analytics
from artist_paintings import artist_paintings 

#mydb = mysql.connector.connect(
 #   host="localhost",
  #  user="root",
   # password=""
    # )
#c = mydb.cursor()
#c.execute("CREATE DATABASE art_gallery")

mydb = pymysql.connect(host='127.0.0.1',user='root',passwd='')
c= mydb.cursor()

def main():
    st.title("Artist")
    artist_menu = ["Add","View","Update", "Remove","Artist analytics","Artist vs Paintings"]
    artist_choice = st.sidebar.selectbox("Artist", artist_menu)

    if artist_choice == "Add":
        st.subheader("Enter Artist details")
        create()

    elif artist_choice == "View":
        st.subheader("Artist details")
        read()

    elif artist_choice == "Update":
        st.subheader("Update artist details")
        update()

    elif artist_choice == "Remove":
        st.subheader("Remove artist")
        delete()
    
    elif artist_choice == "Artist analytics":
        st.subheader("Artist revenue")
        artist_analytics()
    
    elif artist_choice == "Artist vs Paintings":
        st.subheader("Artist vs Paintings")
        artist_paintings()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
