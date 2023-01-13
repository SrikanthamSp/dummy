
USE artgallery;

CREATE table Artist(Artist_ID int not null primary key, 
					FirstName varchar(20) not null,
					MiddleName varchar(20) not null, 
					LastName varchar(20) not null, 
                    Email varchar (50),
					Address varchar(100) not null, 
                    Pincode int(6) not null,
					Phone int not null);

CREATE table Exhibition(Ex_ID int not null primary key, 
						Ex_Name varchar(40) not null, 
						Ex_Location varchar(100) not null, 
						Start_Date date not null, 
						End_Date date not null);

CREATE table Customer(C_ID int not null primary key, 
					  C_Email varchar(40) not null unique, 
					  C_Name varchar(40) not null, 
					  Address varchar(100) not null, 
					  Phone int(10) not null);

CREATE table Painting(Painting_ID int not null primary key, 
					  Title varchar(40) not null, 
					  Description varchar(40) not null, 
					  Year year(4) not null, 
					  Type varchar(40) not null, 
					  Cost int not null);

CREATE table Display(Painting_ID int not null, 
					 Displayed_In_Ex_ID int not null, 
		             primary key (Painting_ID,Displayed_In_Ex_ID));

ALTER table Painting add column Artist_ID int not null;

ALTER table Painting add foreign key (Artist_ID) references Artist(Artist_ID) on delete cascade;


ALTER table Painting add column Sold_In_Ex_ID int;
ALTER table Painting add foreign key (Sold_In_Ex_ID) references Exhibition(Ex_ID);


ALTER table Painting add column C_ID int;

ALTER table Painting add foreign key (C_ID) references Customer(C_ID);

ALTER table Display add foreign key (Displayed_In_Ex_ID) references Exhibition(Ex_ID);
ALTER table Display add foreign key (Painting_ID) references Painting(Painting_ID);
