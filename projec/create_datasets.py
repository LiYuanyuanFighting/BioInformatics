import numpy as np
from sklearn.datasets import make_classification

# Generate and save 10 imbalanced datasets:
# Each dataset should be saved as a txt, tab-delimited,
# using the method to_csv()
# - 5% - 95%, 2 classes, 500 samples, 1000 features
# - 10% - 90%, 2 classes, 500 samples, 1000 features
# - 15% - 85%, 2 classes, 500 samples, 1000 features
# - 20% - 80%, 2 classes, 500 samples, 1000 features
# - 25% - 75%, 2 classes, 500 samples, 1000 features
# - 30% - 70%, 2 classes, 500 samples, 1000 features
# - 35% - 65%, 2 classes, 500 samples, 1000 features
# - 40% - 60%, 2 classes, 500 samples, 1000 features
# - 45% - 55%, 2 classes, 500 samples, 1000 features
# - 50% - 50%, 2 classes, 500 samples, 1000 features

weightsFrom = 0.0
weightsTo = 1.0

for i in range(0,10):
    weightsFrom += 0.05 
    weightsTo -= 0.05
    x, y = make_classification(n_classes=2, class_sep=2,weights=[weightsFrom, weightsTo], n_informative=3, n_redundant=1, flip_y=0,
n_features=1000, n_clusters_per_class=1, n_samples=500, random_state=10, scale=1.0)
    fileNameX = "datasets/datasetX" + str(i) + ".csv";
    fileNameY = "datasets/datasetY" + str(i) + ".csv";
    # Save an array to a text file.
    np.savetxt(fileNameX, x, delimiter='\t')
    np.savetxt(fileNameY, y, delimiter='\t')
    
