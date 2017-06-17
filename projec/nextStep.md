Using cross_val_score, no need to use train_test_split(), because cross_validation itself
already split data into test and train

1st try feature removing https://miguelmalvarez.com/2015/02/23/python-and-kaggle-feature-selection-multiple-models-and-grid-search/

It seems that I need to do feature selection for each fold, this can be  
done in cross validation, the parameters of cross validation can be set   
inside GridSearchCV.  
```python
# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]  
clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5,
                       scoring='%s_macro' % score)
    clf.fit(X_train, y_train)
```  
up vote
47
down vote
accepted
If you perform feature selection on all of the data and then cross-validate,  
then the test data in each fold of the cross-validation procedure was also  
used to choose the features and this is what biases the performance analysis.  
The key idea is that cross-validation is a way of estimating the generalisation  
performance of a process for building a model, so you need to repeat the whole  
process in each fold. Otherwise you will end up with a biased estimate, or an   
under-estimate of the variance of the estimate (or both).  
https://stats.stackexchange.com/questions/27750/feature-selection-and-cross-validation/27751#27751
