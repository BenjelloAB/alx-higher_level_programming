-- lists all records of the table second_table of the hbtn_0c_0 db

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
