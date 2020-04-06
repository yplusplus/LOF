import distance

class LOF(object):

    def __init__(self, points, k_neighbors, dist_strategy=distance.euclid_dist):
        self.points = points
        self.points_num = len(points)
        self.k_neighbors = k_neighbors
        self.k_distance = []
        self.lrd = []
        self.lof = []
        self.neighbors = []
        self.dist = dist_strategy

    def calc(self):
        if not self.lof:
            self.calc_k_dist()
            self.calc_lrd()
            self.calc_lof()

        return self.lof

    def calc_k_dist(self):
        for i in xrange(self.points_num):
            dist_list = [ (self.dist(self.points[i], self.points[j]), j) for j in xrange(self.points_num) if j != i ]
            dist_list.sort()
            l = [t for dis, t in dist_list[0: self.k_neighbors]]
            self.k_distance.append(dist_list[self.k_neighbors][0])
            self.neighbors.append(l)

    def calc_reach_dist(self, p, o):
        return max(self.k_distance[o], self.dist(self.points[p], self.points[o]))

    def calc_lrd(self):
        for p in xrange(self.points_num):
            sm = sum([self.calc_reach_dist(p, o) for o in self.neighbors[p]])
            self.lrd.append(len(self.neighbors) / sm)

    def calc_lof(self):
        for p in xrange(self.points_num):
            sm = sum([self.lrd[o] for o in self.neighbors[p]])
            sm = sm / self.lrd[p] / len(self.neighbors[p])
            self.lof.append(sm)
        
def local_outlier_factor(points, k_neighbors, dist_strategy=distance.euclid_dist):
    lof = LOF(points, k_neighbors, dist_strategy)
    lof_values = lof.calc()
    return zip(points, lof_values)
