import numpy as np
import pandas as pd
import sys
import csv
import random
import pickle # for saving the result
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score, make_scorer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import LabelBinarizer
from imblearn.combine import SMOTETomek, SMOTEENN 
from imblearn.over_sampling import  RandomOverSampler, ADASYN, RandomOverSampler, SMOTE
from imblearn.under_sampling import ClusterCentroids, CondensedNearestNeighbour
### Library
#class Score:

#  @staticmethod
#  def _mclass_roc_auc(truth, pred, average="macro"):
 # def _mclass_roc_auc(truth, pred):
#    lb = LabelBinarizer()
#    lb.fit(truth)

#    truth = lb.transform(truth)
#    pred = lb.transform(pred)

#    return roc_auc_score(truth, pred, average="macro")

  # def get(scorer, average="macro"):
  # If a non-static method is member of a class, you have to define it like that: def Method(self, atributes..)
#  @staticmethod
#  def get(scorer, average="macro"):
#
#     if scorer == "roc_auc":
#       # return Score._mclass_roc_auc()
#       return make_scorer(Score._mclass_roc_auc)

### Actual script

def _mclass_roc_auc(truth, pred, average="macro"):
 # def _mclass_roc_auc(truth, pred):
    print "Calculating score"
    if len(np.unique(truth)) != 2:
        print "Only one class label"
        return 0
        #return roc_auc_score(truth, pred, average="macro")
    lb = LabelBinarizer()
    lb.fit(truth)

    truth = lb.transform(truth)
    pred = lb.transform(pred)

    return roc_auc_score(truth, pred, average="macro")

# create a matrix to store the result for each method and dataset
#matrix = np.full((7, 10), 0)
filePathX = "datasets/datasetX"
filePathY = "datasets/datasetY"
# full methods
myMethods = [ClusterCentroids, CondensedNearestNeighbour, ADASYN, RandomOverSampler, SMOTE, SMOTEENN, SMOTETomek]
myMethodName = ["ClusterCentroids", "CondensedNearestNeighbour", "ADASYN", "RandomOverSampler", "SMOTE", "SMOTEENN", 
                "SMOTETomek"]
# full datasets
Dataset = ["Dataset0", "Dataset1", "Dataset2", "Dataset3", "Dataset4", "Dataset5", "Dataset6", "Dataset7", "Dataset8", "Dataset9"]
#matrix = np.zeros(len(myMethodName), dtype=[('heads','a14'),('vals','f4',(10,))])
ii = 0 
j = 0
#myResult = np.array([ ["Dataset", "Method", "Score"] ])

# for full version use:
for ii in range(0, 7):
#for ii in range(0, 2):
   #matrix[ii][j] = myMethodName[ii]
   sub_array = np.zeros(shape=(10,1))
   # for full version use:
   for j in range(0, 10):
   #for j in range(0, 2):
       # Load dataset
       # take care: be consistent with the sep created for the file
       print "Begins to check file ", j
       filePathXFull = filePathX+str(j)+".csv"
       X = pd.read_table(filePathXFull, sep='\t', index_col=False)
       # print X.iloc[0].head(1)
       # without adding index_col = 0 here, cz it will consider 1st column as ind
       # without it, it will consider the rowNum as index, then there will be one column
       filePathYFull = filePathY+str(j)+".csv"
       y = pd.read_table(filePathYFull, sep='\t', index_col=False)
       # Split the dataset into training and test set
       # y.iloc[:, 0]: the : in the first position indicates all rows, 0 means 1st column
       Xtrain, Xtest, ytrain, ytest = train_test_split(
       #  X, y, test_size=1/3, random_state=42), 1/3 will be 0, don't work
       X, y.iloc[:, 0], test_size=0.3, random_state=42, stratify=y.iloc[:, 0])

       # print(repr(Xtrain))
       #Xtrain = Xtrain.convert_objects(convert_numeric=True)
       #print Xtrain.iloc[0].head(1)
       # Xtrain_float = [float(v) for v in Xtrain.values.str.strip().split('\r\n')]
       # TO Balance dataset
       # See methods at http://contrib.scikit-learn.org/imbalanced-learn/auto_examples/index.html
       # bal = SMOTETomek(random_state=42)#TODO, e.g. SMOTETomek(random_state=42)
       f = myMethods[ii]
       bal = f(random_state=42)

       Xtrain, ytrain = bal.fit_sample(Xtrain.values, ytrain.values.ravel())
       # f'smp{i}' is used in python3.6, Xtrain.shape[0] returns the first dimension of the array
       indices = np.random.permutation(ytrain.shape[0])
       Xtrain = Xtrain[indices]
       ytrain = ytrain[indices]
       samples = [ 'smp{i}'.format(i=i) for i in range(Xtrain.shape[0])]
       Xtrain = pd.DataFrame(Xtrain, index=samples, columns=X.columns)
       ytrain = pd.DataFrame(ytrain, index=samples, columns=y.columns)
       mincls = ytrain.iloc[:, 0].value_counts().min()
       ntests = 4
       auc = make_scorer(_mclass_roc_auc)

       # Training the classifier
       rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)
       # Exhaustive search over specified parameter values for an estimator.
       clf = GridSearchCV(rfc, param_grid={
             'n_estimators': np.linspace(100, 500, ntests, dtype=int),
             'min_samples_split': np.linspace(2, mincls, ntests, dtype=int)},
             # scoring='roc_auc', verbose=2, n_jobs=-1)
             scoring=auc, error_score=0, verbose=2, n_jobs=-1)
       # numpy.ndarray.ravel:Return a flattened array
       #try:
        
       clf.fit(Xtrain.values, ytrain.values.ravel())
       #except:
       #print("Oops!",sys.exc_info()[0],"occured.")
       #print('Next entry')
       print('Best macro ROC/AUC score: {score}'.format(score = clf.best_score_))
       sub_array[j] = clf.best_score_
       print j
       print sub_array
       if j==0 and ii==0:
         myResult = np.array([ ['Dataset', 'Method', 'Score'], [Dataset[j], myMethodName[ii], sub_array[j][0]] ])
       else:
         temp = np.array([Dataset[j], myMethodName[ii], sub_array[j][0]])
         myResult = np.vstack([myResult, temp])
       print myResult
       #matrix[ii][j+1] = clf.best_score_
       
       # Getting testing performance
       truth = ytest.values.ravel()
       pred = clf.best_estimator_.predict(Xtest[Xtrain.columns])
       cm = pd.DataFrame(confusion_matrix(truth, pred))
       # index=names, columns=names)

       print('Testing confusion matrix:\n{cm}'.format( cm = cm ))
       
format = '%s,%s,%s'
np.savetxt('result.csv', myResult, fmt=format, delimiter='\t')
