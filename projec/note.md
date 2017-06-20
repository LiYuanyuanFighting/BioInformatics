feature_selection_simple_20%
feature_selection_simple_20%(No test.transform(Xtest))
The two use Xtest = test.transform(Xtest) compared with pred = clf.best_estimator_.predict(Xtest[Xtrain.columns])
the results are very different, because with transorm(), Xtest will be reduced to the selected features. Without
transform() but ...predict(Xtest[Xtrain.columns]), it will just use all features ..?

Regression: the output variable takes continuous values.

Classification: the output variable takes class labels.
1. didn't use class Score, because it always have problem in finding the right method  
inside it, when I write the whole parameters to call it, it will have other errors.  


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
http://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html
scikit-learn provides an object that, given data, computes the score during the fit of an estimator on a parameter grid and chooses the parameters to maximize the cross-validation score. This object takes an estimator during the construction and exposes an estimator API:
>>>
>>> from sklearn.model_selection import GridSearchCV, cross_val_score
>>> Cs = np.logspace(-6, -1, 10)
>>> clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs),
...                    n_jobs=-1)
>>> clf.fit(X_digits[:1000], y_digits[:1000])        
GridSearchCV(cv=None,...
>>> clf.best_score_                                  
0.925...
>>> clf.best_estimator_.C                            
0.0077...

>>> #Prediction performance on test set is not as good as on train set
>>> clf.score(X_digits[1000:], y_digits[1000:])      
0.943...  

RandomForestClassifier  
A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and use averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement if bootstrap=True (default).
By default, the GridSearchCV uses a 3-fold cross-validation. However, if it detects that a classifier is passed, rather than a regressor, it uses a stratified 3-fold.  

Nearest cleaning rule(NCR)  
https://books.google.de/books?id=Swq7BQAAQBAJ&pg=PA216&lpg=PA216&dq=Neighbourhood+Cleaning+Rule&source=bl&ots=cZ8VcP096y&sig=YVTWmag05Lu8VDHPUf-aROe-o7o&hl=zh-CN&sa=X&ved=0ahUKEwigpNn8-L_UAhXLfRoKHXbxBvIQ6AEIcTAN#v=onepage&q=Neighbourhood%20Cleaning%20Rule&f=false  
The problem is not SMOTE since it is generating the data one used alone.
However, I think that the issue is coming from your sample generation and more precisely by setting the number of dimension to 1000. In this high-dimensional space, SMOTE is probably always generating at least one sample which is close to the other class. Therefore, the rule of the ENN for the selection which is by default 'all' will actually remove all the samples from this class. you could enlarge the number of neighbors in the ENN and set the selection kind to mode. But in all the cases I am not convince about that high dimensional feature space.
