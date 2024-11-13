DROP TABLE IF EXISTS tiny;
CREATE TABLE tiny (token TEXT UNIQUE PRIMARY KEY, url TEXT UNIQUE);

INSERT INTO tiny VALUES ('kara', 'http://southeastwind.net/karaoke');
INSERT INTO tiny VALUES ('notebooks', 'http://45.33.63.153:8888/tree');
