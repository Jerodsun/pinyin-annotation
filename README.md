# pinyin-annotation

I think I started off by pulling the pinyin.sqlite3 file and then renaming it to db.sqlite3. That's how the tables were preserved.
A direct migration in Postgres will be more complicated.


9/13/2019 A lot of headache (which also allowed me to defend other parts of the code better, though, so kind of a win) because `markdown` needs to be v.3 or above. Idk why this one in particular triggered it.

AttributeError at /api/
'OrderedDict' object has no attribute 'register'

nikola and apache airflow are now incompatible. Whatever, install dependencies separately. I think the param is `-e` 

Frontend Thoughts:
Need a loading spinner especially if it's just booting up.