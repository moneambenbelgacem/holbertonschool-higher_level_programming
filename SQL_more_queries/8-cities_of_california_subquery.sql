-- code to that creates the MySQL table
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE name ='california') ORDER BY id ASC;