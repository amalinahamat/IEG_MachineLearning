# introduction to K-Means Clustering

'''
a technique in vector quantization
objective => to divide a set of n observations into k clusters,  with each observation
assigned to the cluster whose mean (cluster center or centroid) is closest, thereby acting as
a representative of that closest

an unsupervised learning

to group similar data points together in a process known as clustering
by grouping things together into - you guessed it - clusters

first property of clusters
1) the points within a cluster should be similar to each other.
=> our aim here is to minimize the distance between the points within a cluster 

second property of clusters
1) The data points from different clusters should be as different as possible

k-means is a centroid-based algorithm or a distance-based algorithm,
where we calculate the distances to assign a point to a cluster. each cluster is
associated with a centroid
    
main objective => to minimize the sum of distances between the points and their respective cluster centroid

optimization process in k-means clustering algorithm => the goal to find the best set of centroids that 
minimizes the sum of squared distances between each data point and its closest centroid.


how it works :
1. Initialization: Start by randomly selecting K points from the dataset. These points will act as the initial cluster centroids.
2. Assignment: For each data point in the dataset, calculate the distance between that point and each of the K centroids. 
Assign the data point to the cluster whose centroid is closest to it. This step effectively forms K clusters.
3. Update centroids: Once all data points have been assigned to clusters, recalculate the centroids of the clusters by 
taking the mean of all data points assigned to each cluster.
4. Repeat: Repeat steps 2 and 3 until convergence. Convergence occurs when the centroids no longer change significantly 
or when a specified number of iterations is reached.
5. Final Result: Once convergence is achieved, the algorithm outputs the final cluster centroids and the assignment of each data point to a cluster.

an objective:
1. Grouping similar data points: K-means aims to identify patterns in your data by grouping data points that share similar characteristics together. 
This allows you to discover underlying structures within the data.
2. Minimizing within-cluster distance: The algorithm strives to make sure data points within a cluster are as close as possible to each other, 
as measured by a distance metric (usually Euclidean distance). This ensures tight-knit clusters with high cohesiveness.
3. Maximizing between-cluster distance: Conversely, k-means also tries to maximize the separation between clusters. Ideally, 
data points from different clusters should be far apart, making the clusters distinct from each other.

eg : bank
cluster :- high income, average income, low income
clustering :- process of creating these groups

Clustering is the process of dividing the entire data into groups (also known as clusters) based on the patterns in the data.

In clustering, we do not have a target to predict// data not have label. We look at the data, try to club similar observations, and form different groups. Hence it is an unsupervised learning problem.

Inertia
=> calculates the sum of distances of all the points within a cluster from the centroid of that cluster
. use euclidean distance as the distance metric for numeric
. use manhattan distance for the most of the features are categorical

the final inertial value is the sum of all these distances. This distance within the clusters is known as intracluster distance. So, inertia gives us the sum of intracluster distances:
Hence, the distance between them should be as low as possible.
the lesser the inertia value, the better our clusters are.

dunn index :
Along with the distance between the centroid and points, the Dunn index also takes into account the distance between two clusters. This distance between the centroids of two different clusters is known asinter-cluster distance.

dunn index = min(inter cluster distance) / max(inter cluster distance)
The more the value of the Dunn index, the better the clusters will be
The maximum distance between the cluster centroids and the points should be minimum, eventually ensuring that the clusters are compact.

A silhouette score close to 0 suggests overlapping clusters, and a negative score suggests poor clustering solutions.

k => the number of cluster we want to have

Full example:

we have 8 points

1. choose the number of clusters k => we want to have 2 cluster, so k = 2
2. select k random points from the data as centroids, c1 and c2
3.assign all the points to the closest cluster centroid
4. recompute the centroids of newly formed clusters
5. repeat step 3 and 4 <= iteration method

stopping criteria to stop recompute
1. centroids of newly formes clusters do not change
2. points remain in the same cluster
3. maximum number of iterations is reached

it says that, algorithm is not learning any new pattern and it is a sign to stop the training
initially, we set the number of iterations as 100

It is important to choose the right value of k, as a small value can result in under-clustered data, 
and a large value can cause over-clustering.

there is an algorithm called K-Means++ that can be used to choose the initial values, or the initial cluster centroids, for K-Means.

K-Means++ helps. It specifies a procedure to initialize the cluster centers before moving forward with the standard k-means clustering algorithm.

Steps to Initialize the Centroids Using K-Means++
1. The first cluster is chosen uniformly at random from the data points we want to cluster. This is similar to what we do in K-Means, but instead of randomly picking all the centroids, we just pick one centroid here
2. Next, we compute the distance (D(x)) of each data point (x) from the cluster center that has already been chosen
3. Then, choose the new cluster center from the data points with the probability of x being proportional to (D(x))2
4. We then repeat steps 2 and 3 until k clusters have been chosen

'''
# I Design
# 1
# K-Means Clustering for Classification Prediction
# Write a Python program uses the K-Means clustering algorithm to predict the classification for a new case based on a given dataset.Dataset is provided as a part of template code, which specify classifications for nine combinations of VAR1 and VAR2.predict a classification for a case where VAR1=0.906 and VAR2=0.606, using the result of k- means clustering with 3 means (ie., 3 centroids) use random state as 0.
# Dataset is given as a part of template code.
# Steps: 
# Imports necessary libraries, including pandas for data manipulation.
# Read data from a CSV file named 'dataset.csv'.
# Perform K-Means cluster with 3 centroids using KMeans from sklearn.cluster.
# Fit the model to the data.
# Get input  from the user. VAR1 and VAR2 are used to define the new case for which we want to predict the cluster.
# Predicts the cluster for the new case using the predict method and print the predicted result. 
# Sample Input and Output: 
# Enter Var1: 
# 0.0906
# Enter Var2:
# 0.606
# Predicted Cluster for New Case: 0

import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.simplefilter("ignore")
# Read the data from the CSV file
#Fill your code here
data = pd.read_csv("dataset.csv")

# Select the features (VAR1 and VAR2)
#Fill your code here
first_input = float(input("Enter VAR1: \n"))
second_input = float(input("Enter VAR2: \n "))

# Perform k-means clustering with 3 centroids
#Fill your code here
kmeans = KMeans(n_clusters = 3, random_state = 0)
kmeans.fit(data[['VAR1','VAR2']])

# Define the new case to predict
#Fill your code here
new_case = [[first_input, second_input]]

# Predict the cluster for the new case
#Fill your code here
predicted_cluster = kmeans.predict(new_case)[0]

# Print the predicted cluster
#Fill your code here
print(f"Predicted Cluster for New Case: {predicted_cluster}")


# I Assess
# 1
# K-Means
# Create a Python program to visualize the K-Means clustering algorithm on a set of data points in two-dimensional space.
# Steps:
# Prompt the user to enter the number of features (n) and the features themselves. Each feature should be entered in the format (x, y) and separated by commas.
# Initialize the K-Means clustering algorithm by selecting every other data point as the initial centroids.
# Use scikit-learn's KMeans implementation with 2 clusters to perform K-Means clustering on the input data.
# Plot the original data points with different colors representing the clusters they belong to.
# Plot the cluster centroids.
# Save the resulting plot as 'kmeans_op.png'.
# Sample Input and Output :
# Enter the number of features
# 10
# Enter the features in comma separated format
# 5,3
# 10,15
# 15,12
# 24,10
# 30,45
# 85,70
# 71,80
# 60,78
# 55,52
# 80,91

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

number = int(input("Enter the number of features\n"))
print("Enter the features in comma separated format")

features = []
for feature in range(number):
    feature_num = input("").split(",")
    features.append((float(feature_num[0]), float(feature_num[1])))

feature_ = np.array(features)

kmeans = KMeans(n_clusters = 2, init='k-means++', n_init=10)

kmeans.fit(feature_)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure()

plt.scatter(feature_[labels==0, 0], feature_[labels==0, 1], c='purple', marker='o', label='Cluster 1')
plt.scatter(feature_[labels==1, 0], feature_[labels==1, 1], c='yellow', marker='o', label='Cluster 2')

plt.scatter(centroids[:, 0], centroids[:,1], marker = "o", c = "blue", s = 200, label='Centroids')

plt.savefig("kmeans_op.png")
# plt.show()

    




 

