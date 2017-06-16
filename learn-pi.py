import sqlite3
import pandas as pd

#version check
#print (pd.__version__)
#v = sys.version[:3]
#print(v)
#eo version check

conn = sqlite3.connect("/home/pi/data/climate.db")
c = conn.cursor()
df = pd.read_sql_query("SELECT substr(dt,1,4) as yyyy, "\
						"Country as Cntry, "\
						"avg(AverageTemperature) as AvgTemp, "\
						"avg(AverageTemperatureUncertainty) as AvgTempUnc "\
						"from GLOBAL_LAND_TEMP_COUNTRY "\
						"where dt>'2009-00-00' "\
						"group by substr(dt,1,4), Country "\
						"order by substr(dt,1,4), Country;", conn)
print (df.head(20))
df.plot.bar()
conn.close()

# calc number rows in table
#c.execute("select count(*) from GLOBAL_LAND_TEMP_MAJOR_CITY;")
#result=c.fetchone()
#number_of_rows=result[0]
#print(number_of_rows)
