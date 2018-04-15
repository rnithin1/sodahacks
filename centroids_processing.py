import numpy as np

processed_centroids = []

for i in range(0,24,4):
    centroid_string = 'centroids_' + str(i) + '.npy'
    data = np.load(centroid_string)
    centroid_location = data[0]
    point_location = data[1]
    frequency_param = [0 for i in range(len(centroid_location))]
    for point in point_location:
        frequency_param[point] += 1

    # print(i)
    # print(frequency_param[:20])
    
    processed_centroids.append(frequency_param)

np.save('processed_centroids.npy', processed_centroids)
