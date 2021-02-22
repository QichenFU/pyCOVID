create table date (
date date,
primary key (date));

create table country (
Country_name varchar(50),
primary key (Country_name));

Create table Country_province (
Country_name varchar(50),
Province_name varchar(50),
primary key (Province_name),
foreign key (Country_name) references country);

Create table Country_confirmed_cases (
Date date,
Country_name varchar(50),
Confirmed int4,
primary key (Date,Country_name),
foreign key (country_name) references Country,
foreign key (date) references date);

Create table Province_confirmed_cases (
Date date,
Province_name varchar(50),
Confirmed int4,
primary key (Date,Province_name),
foreign key (Province_name) references Country_province,
foreign key (date) references date);