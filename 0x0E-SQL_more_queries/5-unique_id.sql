-- create table with id that defaults to 1 and checks if unique
CREATE TABLE IF NOT EXISTS unique_id (
id INT default 1 UNIQUE,
name VARCHAR(256)
);
