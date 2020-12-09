
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS book;

CREATE TABLE author (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);
CREATE TABLE book (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  publisher  VARCHAR(255),
  author_id INT REFERENCES author(id)
);