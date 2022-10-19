# import psycopg2 as pg

# conn = pg.connect(
#     database="personal_fitness",
#     user="postgres",
#     password="4mathft",
#     host="thernizetech.hopto.org",
#     port="5432"
# )

# cur = conn.cursor()

# cur.execute("INSERT INTO raw_data.users VALUES (%s,%s,%s,%s,%s)",
#             (1, "haitiangk92@gmail.co", "Emmanuel", "Thernize", "test_password"))
# conn.commit()

# cur.execute(
#     "SELECT column_name, data_type FROM information_schema.columns where table_name = 'users'")

# print(cur.fetchall())

import requests as r

api_url = "http://thernizetech.hopto.org"

req = r.get(api_url)

res = req.text

print(res)
