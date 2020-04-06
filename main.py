import lof
import distance
import matplotlib.pyplot as plt
import random_data

if __name__ == "__main__":
    points = []
    points.extend(random_data.get_circle_random_points((20, 20), 20, 500))
    points.extend(random_data.get_circle_random_points((100, 100), 5, 150))
    points.extend(random_data.get_box_random_points((0, 0), (100, 100), 150))
    exception_threshold = 1.2
    k_neighbors = 10

    lofs = lof.local_outlier_factor(points, k_neighbors, dist_strategy=distance.euclid_dist)
    print "dist_strategy:manhattan, k_neighbors=%d" % k_neighbors
    for p, val in lofs:
        print p, val
        c = 'b' if val <= exception_threshold else 'r'
        plt.scatter(p[0], p[1], c=c)

    plt.show()
