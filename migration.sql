INSERT INTO pinyin_pinyincodes 
("character", pinyin1, number, pinyin2)
SELECT "character", pinyin1, number, pinyin2 from pinyin_codes
WHERE character not null;