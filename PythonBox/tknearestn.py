# videos 1

'''unsupervised learning 
-> there are no labels for the training data but we have historical data
eg : 
1.customer segmentation -> common purchase of the customer transactions
2.text clustering -> class the files
3.logisitcs optimization -> daily fleet movement data to plan the route to make smooth path/ moevemnt

we need to make an algorithm to find common cluster and put it into that group

K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabelled dataset into 'K' different clusters.
K defines the number of predefined clusters that need to be created in the process, as if K = 2, there will be two 
clusters, and for K = 3, there will be three clusters, and so on.
'''
# videos 2
'''objective -> To group similar data points together and discover underlying patterns. to achieve this objective, Kmeans looks
for a fixed number (k) of clusters in a dataset
    
a cluster refers to a collection of data points aggregated together because of certain similarities

k -> refer to a number of centroids
k-means algorithm identifies k number of centroids, and then allocates every data point to the nearest cluster.
means in the k-means refer to averaging pf the data, that is finding the centroid

basis and steps
1. determine the value "k" , the value "k" represent the number of cluster
2. randomly select "k" distinct centroid (new data points as cluster initialization)
3. measure the distance(euclidean distance) between each point and the centroid
4. assign the each point to the nearest cluster
5. calculate the mean of each cluster as new centroid
6. repeat step 3-5 with the new center of cluster till Sum of Square Distances between all Data Points stabilize

d(p,q) = sqrt((qx - px)^2 + (qy - py)^2)  <= euclidean distance

x and y are not predicted value, it is just feature of the datasets'''


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset from the CSV file
df = pd.read_csv("input.csv")
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
# Split the data into features (X) and target (y)
# X = df.drop("class", axis = 1)
# y = df["class"]

# Encode the target labels to numeric values
Label_encoder = LabelEncoder()
df['class'] = Label_encoder.fit_transform(df['class'])

# Split the data into features (X) and target (y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Create a KNN classifier with K=11
knn = KNeighborsClassifier(n_neighbors = 11)

# Train the model on the training data
knn.fit(X_train,y_train)

user_data = input("Enter the test vector in comma separated format\n").split(",")

list_user_data = []
for data in user_data:
    list_user_data.append(float(data))

# Predict the class using the trained model
predicted_class = knn.predict([list_user_data])[0]

print(predicted_class)

