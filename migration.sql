INSERT INTO pinyin_pinyincodes 
("character", pinyin1, number, pinyin2)
SELECT "character", pinyin1, number, pinyin2 from pinyin_codes
WHERE character not null;


-- sqlite3 pinyin.sqlite3 

.schema pinyin
.open db.sqlite3
ATTACH 'pinyin.sqlite3' as db2;
INSERT INTO pinyin_pinyincodes select DISTINCT * FROM db2.pinyin_codes; -- idk why it's not distinct

-- STAGE/PROD migration: 
-- sudo heroku pg:psql postgresql-tetrahedral-05425 --app pinyin-annotation -c "\copy pinyin_codes FROM '/home/jerod/Desktop/pinyin-annotation/data.csv' delimiter ',' csv;"
