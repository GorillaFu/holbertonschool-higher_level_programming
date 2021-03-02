-- create table with id that defaults to 1 and checks if unique
CREATE TABLE IF NOT EXISTS id_not_null (
id INT default 1 UNIQUE,
name VARCHAR(256)
);
