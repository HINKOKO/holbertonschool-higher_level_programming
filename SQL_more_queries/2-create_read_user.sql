-- Script that creates database hbtn_0d_2 and user_0d_2
-- Gives SELECT privilege only
-- password set to user_0d_2_pwd
-- if not exists, doesn't fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
