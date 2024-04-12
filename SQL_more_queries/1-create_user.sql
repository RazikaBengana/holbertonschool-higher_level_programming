-- Create a new user named 'user_0d_1' on 'localhost' if it doesn't already exist, with a specified password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and their tables to 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes immediately
FLUSH PRIVILEGES;
