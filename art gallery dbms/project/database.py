
import pymysql

mydb = pymysql.connect(host='127.0.0.1',user='root',passwd='',database='artgallery')
c= mydb.cursor()

def add_data(artist_id, artist_fname, artist_mname, artist_lname, artist_email, artist_addr, artist_pin, artist_phone):
    c.execute('insert into artist values (%s,%s,%s,%s,%s,%s,%s,%s)',
              (artist_id, artist_fname, artist_mname, artist_lname, artist_email, artist_addr, artist_pin, artist_phone))
    mydb.commit()


def view_all_data():
    c.execute('select * from artist')
    data = c.fetchall()
    return data


def view_artist_ids():
    c.execute('select Artist_ID from artist')
    data = c.fetchall()
    return data


def artist_details(selected_artist):
    c.execute('select * from artist where Artist_ID="{}"'.format(selected_artist))
    data = c.fetchall()
    return data


def edit_artist(new_artist_fname, new_artist_mname, new_artist_lname, new_artist_email,new_artist_addr,new_artist_pin,new_artist_phone, artist_id):
    c.execute("update artist SET FirstName=%s, MiddleName=%s, LastName=%s, Email=%s, Address=%s, Pincode=%s, Phone=%s WHERE Artist_ID=%s",(new_artist_fname, new_artist_mname, new_artist_lname, new_artist_email,new_artist_addr,new_artist_pin,new_artist_phone, 
              artist_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(artist_id):
    c.execute('delete from artist where Artist_ID="{}"'.format(artist_id))
    mydb.commit()

def view_artist_analytics():
    c.execute("select A.Artist_ID, FirstName, LastName, COUNT(Painting_id) AS Number_of_paintings,SUM(Cost) AS Revenue"
              " FROM (painting AS P JOIN artist as A on P.Artist_ID = A.Artist_ID)"
              " WHERE C_ID is not null"
              " Group by A.Artist_ID" 
              " Order by Revenue desc")
    data = c.fetchall()
    return data

def view_artist_paintings():
    c.execute("select A.Artist_ID, FirstName, LastName, Count(Painting_ID)"
              " FROM (painting AS P RIGHT JOIN artist as A on P.Artist_ID = A.Artist_ID)"
              " Group by A.Artist_ID;")
    data = c.fetchall()
    return data

def view_painting_analytics():
    c.execute("SELECT Painting_ID, Title, Cost from painting"
              " where C_ID is null AND painting_id IN"
              " (SELECT Painting_ID from display"
              " Group by (Painting_ID)"
              " HAVING COUNT(Displayed_In_Ex_ID) > 1);")
    data = c.fetchall()
    return data

def add_painting(p_id, p_title, p_desc, p_year, p_type, p_cost, artist_id):
    c.execute('insert into painting values (%s,%s,%s,%s,%s,%s,%s,null,null)',
              (p_id, p_title, p_desc, p_year, p_type, p_cost, artist_id))
    mydb.commit()

def delete_painting(p_id):
    c.execute('delete from painting where Painting_ID="{}"'.format(p_id))
    mydb.commit()

def view_all_paintings():
    c.execute('select * from painting')
    data = c.fetchall()
    return data


def view_painting_ids():
    c.execute('select Painting_ID from painting')
    data = c.fetchall()
    return data


def painting_details(selected_p):
    c.execute('select * from painting where Painting_ID="{}"'.format(selected_p))
    data = c.fetchall()
    return data

def edit_painting(new_p_title, new_p_desc, new_p_year, new_p_type, new_p_cost, new_artist_id, new_siex_id,new_c_id,selected_p):
    c.execute("update painting SET Title=%s, Description=%s, Year=%s, Type=%s, Cost=%s, Artist_ID=%s, Sold_In_Ex_ID=%s, C_ID=%s WHERE Painting_ID=%s",(new_p_title, new_p_desc, new_p_year, new_p_type, new_p_cost, new_artist_id, new_siex_id,new_c_id,selected_p))
    mydb.commit()
    data = c.fetchall()
    return data

