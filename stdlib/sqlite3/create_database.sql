DROP TABLE IF EXISTS users;
CREATE TABLE users (uid INT UNIQUE PRIMARY KEY, gid INT, alias TEXT, shell TEXT);

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (gid INT UNIQUE PRIMARY KEY, name TEXT);


INSERT INTO groups VALUES (1001, "admin");
INSERT INTO groups VALUES (1002, "user");


INSERT INTO users VALUES (501, 1001, "karen", "zsh");
INSERT INTO users VALUES (502, 1002, "john", "bash");
INSERT INTO users VALUES (503, 1002, "peter", "bash");

