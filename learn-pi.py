import sqlite3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

conn = sqlite3.connect("/home/pi/data/climate.db")
c = conn.cursor()
df = pd.read_sql_query("SELECT "\
							"substr(dt,1,3) as decade, "\
#							"Country as Cntry, "\
							"avg(AverageTemperature) as AvgTemp, "\
							"avg(AverageTemperatureUncertainty) as AvgTempUnc "\
						"from GLOBAL_LAND_TEMP_COUNTRY "\
						"where dt>'180' and "\
							"substr(Country,1,1)='A' "\
						"group by "\
							"substr(dt,1,3) "\
#							"Country "\
						"order by "\
							"substr(dt,1,3) ", \
#							"Country" ,\
					conn)

print (df.head(20))
df.plot(x='decade', y='AvgTemp')
plt.show()
conn.close()
