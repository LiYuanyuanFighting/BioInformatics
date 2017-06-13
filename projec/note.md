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
