class KMeans():
    def __init__(self, initial_clusters, data):
        self.clusters = initial_clusters
        self.data = data
        self.centers = {n: self.get_centers(self.clusters[n]) for n in self.clusters}

    def get_centers(self, indices):
        centroid = self.data[indices[0]]

        for index in indices[1:]:
            centroid = [centroid[n] + self.data[index][n] for n in range(len(centroid))]

        return [n / len(indices) for n in centroid]

    def get_distance(self, data_point, centeroid):
        return sum([(data_point[n] - centeroid[n]) ** 2 for n in range(len(data_point))]) ** 0.5 

    def get_nearest_center(self, index):
        key_of_nearest_center = list(self.centers.keys())[0]
        smallest_distance = self.get_distance(self.data[index], self.centers[key_of_nearest_center])

        for key in self.centers:
            if self.get_distance(self.data[index], self.centers[key]) < smallest_distance:
                key_of_nearest_center = key
                smallest_distance = self.get_distance(self.data[index], self.centers[key])

        return key_of_nearest_center

    def reset_clusters(self):
        new_clusters = {n: [] for n in self.clusters}

        for n in range(len(self.data)):
            new_clusters[self.get_nearest_center(n)].append(n)

        if new_clusters == self.clusters:
            return True

        self.clusters = new_clusters
        return False

    def update_clusters_once(self):
        self.centers = {n: self.get_centers(self.clusters[n]) for n in self.clusters}
        self.reset_clusters()

    def run(self):
        while True:
            self.centers = {n: self.get_centers(self.clusters[n]) for n in self.clusters}

            if self.reset_clusters():
                break