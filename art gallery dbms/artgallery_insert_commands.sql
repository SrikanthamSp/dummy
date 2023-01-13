use artgallery;
-- Loading customer values
-- syntax: INSERT INTO table_name VALUES (value1, value2, value3, ...);

/*INSERT INTO customer VALUES(211,"Jacob@gmail.com","Jacob","Bunny Street",7895643067);
INSERT INTO customer VALUES(212,"Charlie@gmail.com","Charlie","Shanti nagar",7894055672);
INSERT INTO customer VALUES(213,"Hudson@gmail.com","Hudson","Gaziabad",6757847896);
INSERT INTO customer VALUES(214,"Frankie@gmail.com","Frankie","Goregaon",6986658629);


-- syntax: INSERT INTO table_name(column 1, column2, coulmn3...) VALUES(Value1,Value2,Value3,...),(value1,value2,value3...);
INSERT INTO customer(C_ID,C_Email,C_Name,Address,Phone) VALUES (215,"Harvey@gmail.com","Harvey","Navrang",7868837586),(216,"Samuel@gmail.com","Samuel","Om Nagar",9378782096),
(217,"Michael@gmail.com","Michael","Banshankari",8485868333);


-- syntax:INSERT INTO table_name(column 1, column2, coulmn3...) VALUES(Value1,Value2,Value3,...);

INSERT INTO customer (C_ID,C_Email,C_Name,Address,Phone)VALUES(218,"Gabriel@gmail.com","Gabriel","Majestic",7038748368);
INSERT INTO customer(C_ID,C_Email,C_Name,Address,Phone) VALUES(219,"Jake@gmail.com","Jake","Yeshwantpur",8578396256);
INSERT INTO customer(C_ID,C_Email,C_Name,Address,Phone)VALUES(220,"Finn@gmail.com","Finn","Yelahanka",9856858854);


-- Loading Exhibition values
-- syntax: INSERT INTO table_name VALUES (value1, value2, value3, ...);
insert into Exhibition values(102, "Craftric","Marathalli","2022-12-28","2022-12-30");

-- syntax:INSERT INTO table_name(column 1, column2, column3...) VALUES(Value1,Value2,Value3,...),(value1,value2,value3...);
insert into exhibition(Ex_ID,Ex_Name,Ex_Location,Start_Date,End_Date) VALUES(103,'ClipArt','BTM layout',"2023-01-01","2023-01-04"),
(150,'Illuminate','HSR layout',"2022-12-30","2023-01-01"),(151,'Art Ally','Jayanagar',"2022-12-31","2023-01-02"),(140,'Features','Kormangala',"2023-01-01","2023-01-03");
*/

-- Loading painting values from a .csv file
LOAD DATA INFILE "painting.csv" INTO TABLE painting FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 LINES (Painting_ID, Title, Description, Year, Type, Cost, Artist_ID, Sold_In_Ex_ID, C_ID);
insert into painting values (8,'KRISHNA RADHA TASAR','Tasar painting',2018,'Patachitra' ,10000,6,null,null),(17,'New York Sickness','Busy life of New York',2008,'Pichwai',10000,3,null,null),
(19,'Burning Desire','Materialistic life',2020, 'Tribal Phad',200000,6,null,null),(23,'Lavender Night','Mysterious night',2013,'Patachitra' ,125000,5,null,null),(24,'How Everyday Goes','Unnoticeable things around us',2017,'Pichwai',200000,4,null,null);
-- Loading display values from a .csv file
LOAD DATA INFILE "Display.csv" INTO TABLE display FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 LINES (Painting_ID,Displayed_In_Ex_ID);

-- Loading artist values from a .csv file
-- LOAD DATA INFILE "artist.csv" INTO TABLE artist FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 LINES (Artist_ID, FirstName, MiddleName, LastName, Email, Address, Pincode , Phone);
