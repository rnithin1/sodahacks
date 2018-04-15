import numpy as np
import pandas as pd
from scipy.cluster.vq import *

print("Starting")
df_by_hour = []
for i in range(0, 24, 2):
    df = pd.read_csv("df_concat_{}.csv".format(i))
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    df_by_hour.append(df)
print("Starting kmeans")
intersections_by_hour = []
for df in df_by_hour:
    print("Beginning")
    #df = whiten(df)
    intersections_by_hour.append(kmeans2(df.values, 12460))
for i in range(len(intersections_by_hour)):
    np.save('centroids_{}.npy'.format(i * 2), intersections_by_hour[i])
