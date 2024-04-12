-- Create the database 'hbtn_0d_2' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' with password 'user_0d_2_pwd' if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on all tables in 'hbtn_0d_2' to the user 'user_0d_2'
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Refresh the server's privileges, applying all changes made above
FLUSH PRIVILEGES;
