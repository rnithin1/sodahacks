import numpy as np
from scipy.cluster.vq import *

totals = np.load("vstackedPoints.dat.npy")
intersections = kmeans2(totals, 12000)
np.save('centroids.npy', intersections)
