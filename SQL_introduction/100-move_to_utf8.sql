-- Change the character set and collation for the database 'hbtn_0c_0' to utf8mb4 and utf8mb4_unicode_ci respectively
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the character set and collation of all columns in 'first_table' within the 'hbtn_0c_0' database to utf8mb4,
-- and utf8mb4_unicode_ci respectively
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
