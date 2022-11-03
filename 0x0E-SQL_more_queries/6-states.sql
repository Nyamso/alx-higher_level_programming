--creates the database hbtn_0d_usa and the table states on your MySQL server
-- (in the database hbtn_0d_usa) on your MySQL server

CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'hbtn_0d_usa'.'states' (
       'id' INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
       'name' VARCHAR(256) NOT NULL);
