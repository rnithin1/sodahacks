import numpy as np
import pandas as pd

string = '/datasets/local/NYUTaxiTripData/'
dft = []
print("Starting")
for i in [1, 6]:
    csv_string = string + "trip_data_" + str(i) + ".csv"
    dft.append(pd.read_csv(csv_string))
    print(i)
totals = []
for arr in dft:
    totals.append(arr.values[:, [5, 10, 11]])
    print("attaching complete")
totals = tuple(totals)
concat = np.vstack(totals)
print(len(concat))
np.save('vstackedPoints.dat', concat)
