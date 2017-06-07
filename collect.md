**AUC ROC**  
When using normalized units, the area under the curve (often referred to as simply the AUC) is equal to the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one (assuming 'positive' ranks higher than 'negative')  
在比較不同的分類模型時，可以將每個模型的ROC曲線都畫出來，比較曲線下面積做為模型優劣的指標。  
ROC曲線下方的面積（英语：Area under the Curve of ROC (AUC ROC)），其意義是：

    因為是在1x1的方格裡求面積，AUC必在0~1之間。
    假設閾值以上是陽性，以下是陰性；
    若隨機抽取一個陽性樣本和一個陰性樣本，分類器正確判斷陽性樣本的值高於陰性樣本之機率 = A U C {\displaystyle =AUC} {\displaystyle =AUC}[1]。
    簡單說：AUC值越大的分類器，正確率越高。
[reference](https://zh.wikipedia.org/wiki/ROC%E6%9B%B2%E7%BA%BF)  


**To reduce imbalance**  
You can change the dataset that you use to build your predictive model to have more balanced data.

This change is called sampling your dataset and there are two main methods that you can use to even-up the classes:

    You can add copies of instances from the under-represented class called over-sampling (or more formally sampling with replacement), or
    You can delete instances from the over-represented class, called under-sampling.

These approaches are often very easy to implement and fast to run. They are an excellent starting point.

In fact, I would advise you to always try both approaches on all of your imbalanced datasets, just to see if it gives you a boost in your preferred accuracy measures.  

Consider testing under-sampling when you have an a lot data (tens- or hundreds of thousands of instances or more)
Consider testing over-sampling when you don’t have a lot of data (tens of thousands of records or less)  

Oversampling randomly replicates minority instances to increase their population. Undersampling randomly downsamples the majority class. Some data scientists (naively) think that oversampling is superior because it results in more data, whereas undersampling throws away data. But keep in mind that replicating data is not without consequence—since it results in duplicate data, it makes variables appear to have lower variance than they do. The positive consequence is that it duplicates the number of errors: if a classifier makes a false negative error on the original minority data set, and that data set is replicated five times, the classifier will make six errors on the new set. Conversely, undersampling can make the independent variables look like they have a higher variance than they do.  


还有一个比较有用的函数是train_test_split
功能：从样本中随机的按比例选取train data和test data。调用形式为：
X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_data, train_target, test_size=0.4, random_state=0)
test_size是样本占比。如果是整数的话就是样本的数量。random_state是随机数的种子。不同的种子会造成不同的随机采样结果。相同的种子采样结果相同。  
