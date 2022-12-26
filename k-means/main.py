import matplotlib.pyplot as plt
import numpy as np

kkk = 0
jck = []
min = 1
isMinKIsFound = False

def random_point(n):
    points = []
    for i in range(n):
        points.append(np.random.randint(1, 100, 2))
    return points

def init_centroids(points, k):
    x_c = 0
    y_c = 0
    for i in range(len(points)):
        x_c += points[i][0]
        y_c += points[i][1]
    x_c /= len(points)
    y_c /= len(points)
    R = 0
    for i in range(len(points)):
        if R < dist([x_c, y_c], points[i]):
            R = dist([x_c, y_c], points[i])
    centroids = []
    for i in range(k):
        x_cntr = R * (np.cos(2 * np.pi * i / k)) + x_c
        y_cntr = R * (np.sin(2 * np.pi * i / k)) + y_c
        centroids.append([x_cntr, y_cntr])
    return centroids

def mean_clusters(points, clusters, k, centroids):
    for i in range(0, k):
        z_x, z_y = [], []
        for j in range(0, len(clusters)):
            if clusters[j] == i:
                z_x.append(points[j][0])
                z_y.append(points[j][1])
        centroids[i][0] = np.mean(z_x)
        centroids[i][1] = np.mean(z_y)
    return centroids

def dist(p_i, p_j):
    return np.sqrt((p_i[0] - p_j[0]) ** 2 + (p_i[1] - p_j[1]) ** 2)

def check(points, centroids, cluster, k):
    global min
    global isMinKIsFound
    global kkk
    x_old = []
    y_old = []
    for i in range(0, len(centroids)):
        x_old.append(centroids[i][0])
        y_old.append(centroids[i][1])
    new_cluster = find_nearest(points, centroids)
    new_centroids = mean_clusters(points, new_cluster, k, centroids)
    plot(points, centroids, cluster, k)
    count = 0
    for i in range(0, k):
        clusterSum = 0
        for j in range(0, len(new_cluster)):
            if (new_cluster[j] == i):
                clusterSum += dist(points[j], centroids[i]) ** 2
        count += clusterSum
    jck.append(count)
    if (len(jck) > 2):
        if ((jck[len(jck) - 2] - jck[len(jck) - 1]) / (jck[len(jck) - 3] - jck[len(jck) - 2])) > min:
            isMinKIsFound = True
            kkk = k
        else:
            min = (jck[len(jck) - 2] - jck[len(jck) - 1]) / (jck[len(jck) - 3] - jck[len(jck) - 2])
    return True

def plot(points, centroids, cluster, k):
    clr = ['b', 'g', 'y', 'pink', 'c', 'm', 'k', 'purple', 'orange', 'grey']
    clrs = []
    points_x = []
    points_y = []
    for i in range(len(points)):
        points_x.append(points[i][0])
        points_y.append(points[i][1])
        clrs.append(clr[int(cluster[i])])
    centroids_x = []
    centroids_y = []
    for i in range(len(centroids)):
        centroids_x.append(centroids[i][0])
        centroids_y.append(centroids[i][1])
    plt.scatter(points_x, points_y, color=clrs)
    plt.scatter(centroids_x, centroids_y, color='r')
    plt.show()

def find_nearest(points, centroids):
    cluster = np.zeros(len(points))
    for i in range(len(points)):
        min_dist = np.infty
        for j in range(len(centroids)):
            if min_dist > dist(points[i], centroids[j]):
                min_dist = dist(points[i], centroids[j])
                cluster[i] = j
    return cluster

def kmeans(k, points):
    centroids = init_centroids(points, k)
    cluster = find_nearest(points, centroids)
    plot(points, centroids, cluster, k)
    while not check(points, centroids, cluster, k):
        check(points, centroids, cluster, k)

n = 100
points = random_point(n)
for i in range(1, 10):
    if not isMinKIsFound:
        kmeans(i, points)
    else:
        break
