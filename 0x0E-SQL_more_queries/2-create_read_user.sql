-- Create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create User
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT Privilege on database to user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
