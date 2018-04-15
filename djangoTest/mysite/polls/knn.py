import numpy as np
import sys
from scipy.spatial import KDTree as sci

sys.setrecursionlimit(10000)

def kevin(longitude, latitude, hour):
    hour = int(hour)
    longitude = np.float64(longitude)
    latitude = np.float64(latitude)
    h = min([0, 4, 8, 12, 16, 20], key=lambda x : abs(x - hour))
    c = np.delete(np.load("polls/centroids_{}.npy".format(h))[0], 0, axis=1)
    p = np.load("polls/processed_centroids.npy")[h // 4]
    tree = sci(c)
    distances, indices = tree.query([longitude, latitude], k=10)
    k = 10
    weights = [p[indices[i]]/distances[i] for i in range(k)]
    # print(weights)
    rlon = np.sum([c[indices[i]][0]*weights[i] for i in range(k)])/np.sum(weights)
    rlat = np.sum([c[indices[i]][1]*weights[i] for i in range(k)])/np.sum(weights)

    f = open("neighbour.txt", "w")
    f.write('{}\n'.format(rlat))
    f.write('{}\n'.format(rlon))

    return rlat, rlon

# we are doing longitude, latitude
# they are doing latitude, longitude
