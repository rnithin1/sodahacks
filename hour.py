from datetime import datetime
import pandas as pd
import numpy as np

df = pd.read_csv("dataframe_concat.csv")
df = df.drop("Unnamed: 0", 1)
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format='%Y-%m-%d %H:%M:%S').dt.hour
df.sort_values(by=['pickup_datetime'])
df.set_index(keys=['pickup_datetime'], drop=False, inplace=True)
pickup_datetime = df['pickup_datetime'].unique().tolist()
df_by_hour = [df.loc[df['pickup_datetime'] == i] for i in range(0, 24, 2)]
i = 0
for hour in df_by_hour:
    #hour = hour[hour.pickup_latitude > 39 and hour.pickup_longitude < -72]
    print(hour.columns[[0]])
    hour.drop(hour.columns[[0]], axis=1, inplace=True)
    hour = hour[(hour != 0).all(1)]
    hour.to_csv("df_concat_{}.csv".format(i))
    i += 2

