# pinyin-annotation

I think I started off by pulling the pinyin.sqlite3 file and then renaming it to db.sqlite3. That's how the tables were preserved.
A direct migration in Postgres will be more complicated.


9/13/2019 A lot of headache (which also allowed me to defend other parts of the code better, though, so kind of a win) because `markdown` needs to be v.3 or above. Idk why this one in particular triggered it.

AttributeError at /api/
'OrderedDict' object has no attribute 'register'

nikola and apache airflow are now incompatible. Whatever, install dependencies separately. I think the param is `-e` 


QA: 
{
    "input_string": [
        "Ensure this field has no more than 200 characters."
    ]
}

美国新闻 ; abc;



Frontend Thoughts:
Need a loading spinner especially if it's just booting up.


local psql:

Success. You can now start the database server using:

    /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start


Migration to prod: Must use `heroku run python manage.py migrate -a pinyin-annotation`, not ps:exec into dyno...

`\copy pinyin_pinyincodes FROM '/home/jerod/Desktop/pinyin-annotation/data.csv' delimiter ',' csv;`
