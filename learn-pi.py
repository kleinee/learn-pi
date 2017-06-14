import sqlite3
import pandas as pd
import sys

conn = sqlite3.connect("/home/pi/data/climate.db")
c = conn.cursor()

df = pd.read_sql_query("SELECT substr(dt,1,7) as yyyymm, Country as Cntry, avg(AverageTemperature) as AvgTemp, avg(AverageTemperatureUncertainty) as AvgTempUnc from GLOBAL_LAND_TEMP_COUNTRY where dt>'2000-00-00' group by substr(dt,1,7), Country order by substr(dt,1,7), Country;", conn)
print df.head(500)
conn.close()

# calc number rows in table
#c.execute("select count(*) from GLOBAL_LAND_TEMP_MAJOR_CITY;")
#result=c.fetchone()
#number_of_rows=result[0]
#print(number_of_rows)
