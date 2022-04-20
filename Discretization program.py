import pandas as pd
import numpy as np
data1=pd.read_csv('F:/Assignments/Assignment 4 data pre processing/DataSets/iris.csv')
data1.dtypes
data1.info()
data1.describe()
data1.columns
pd.cut(data1['Sepal.Length'],bins=3,labels=np.arange(3),right=False) #
pd.cut(data1['Sepal.Length'],bins=3,right=False) #used for binning
pd.cut(data1['Sepal.Width'],bins=3,labels=np.arange(3),right=False)
pd.cut(data1['Sepal.Width'],bins=3,right=False) #used for binning
pd.cut(data1['Petal.Length'],bins=4,labels=np.arange(4),right=False)
pd.cut(data1['Petal.Length'],bins=4,right=False) #used for binning
pd.cut(data1['Petal.Width'],bins=4,labels=np.arange(4),right=False)
pd.cut(data1['Petal.Width'],bins=4,right=False) #used for binning

data1
