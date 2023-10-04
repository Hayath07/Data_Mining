import numpy as np

n = 7 # Total number of objects
m = 3 # Count of dimensions
kmin = 2 # minimum value of the parameter to be tested in K-means
kmax = 4 # maximum value of the parameter to be tested in K-means 

# Generate random data.
rand_data = np.random.rand(n, m)

# Write data to a file named "test.dat".
with open('test.dat', 'w') as file:
    file.write(f"{n} {m} {kmin} {kmax}\n")  # Write metadata: n, m, kmin, and kmax
    for row in rand_data:
        file.write(' '.join(map(str, row)) + '\n')  # Write data object rows

# Function to calculate Euclidean distance between two data points
def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# Function to calculate the sum of squared errors (SSE) for a given clustering
def calculate_sse(data, centroids, cluster_assignment):
    sse = 0
    for i in range(len(data)):
        # Calculate the squared Euclidean distance and accumulate it for each data point
        sse += euclidean_distance(data[i], centroids[cluster_assignment[i]])**2
    return sse

# Function to perform K-means clustering
def kmeans(data, k):
    # Initialize centroids randomly by selecting k data points from the dataset
    centroids = data[np.random.choice(len(data), k, replace=False)]
    
    max_num_iterations = 20  # Number of iterations for the K-means algorithm
    for _ in range(max_num_iterations):
        # Assign each data point to the nearest centroid
        cluster_assignment = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=2), axis=1)
        
        # Update centroids based on the mean of data points in each cluster
        for i in range(k):
            cluster_points = data[cluster_assignment == i]
            if len(cluster_points) > 0:
                centroids[i] = np.mean(cluster_points, axis=0)
    
    # Calculate the sum of squared errors (SSE) for this clustering
    sse = calculate_sse(data, centroids, cluster_assignment)
    return sse

# Read input from "test.dat" file
with open("test.dat", "r") as file:
    n, m, Kmin, Kmax = map(int, file.readline().split())  # Read metadata from the first line
    data = np.loadtxt(file, delimiter=" ")  # Load data from the remaining lines

# Initialize results list to store SSE values for different values of K
results = []

# Perform K-means clustering for each value of K from Kmin to Kmax
for k in range(Kmin, Kmax + 1):
    sse = kmeans(data, k)  # Run K-means clustering for the current K
    results.append((k, sse))  # Append K and its corresponding SSE to the results list

# Write results to an "test.res" output file
with open("test.res", "w") as output_file:
    for k, sse in results:
        output_file.write(f"{k} {sse}\n")  # Write K and SSE to the output file

print("Clustering completed and results written to 'test.res' file.")