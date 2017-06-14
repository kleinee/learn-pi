import sqlite3
import pandas as pd
import sys
conn = sqlite3.connect("/home/pi/data/climate.db")
c = conn.cursor()
c.execute("select count(*) from GLOBAL_LAND_TEMP_MAJOR_CITY;")
result=c.fetchone()
number_of_rows=result[0]
print(number_of_rows)
df = pd.read_sql_query("SELECT * from GLOBAL_LAND_TEMP_MAJOR_CITY", conn)
print df.head(10)
conn.close()
