# -*- coding: utf-8 -*-
"""Project2Workbook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_HA0fdqJNAGfXcyUk2LufFQCiItYFx5f
"""

import calendar

pip install category_encoders

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
pd.options.display.max_columns = None
april20 = pd.read_csv('drive/My Drive/2020_04.csv')
march20 = pd.read_csv('drive/My Drive/2020_03.csv')
march19 = pd.read_csv('drive/My Drive/2019_03.csv')
april19 = pd.read_csv('drive/My Drive/2019_04.csv')



march19

AM20 = pd.concat([april20, march20], ignore_index=True)
AM20

AM19 = pd.concat([march19,april19], ignore_index=True)
AM19

AM20['starttime']= pd.to_datetime(AM20['starttime']) 
AM20['stoptime']= pd.to_datetime(AM20['stoptime']) 
AM19['starttime']= pd.to_datetime(AM19['starttime']) 
AM19['stoptime']= pd.to_datetime(AM19['stoptime']) 
#AM20['starttimeday']=AM20['starttime'].weekday()
AM20



AM20

#AM19['tripduration']=AM20['tripduration']
AM19['tripduration'] = AM19['tripduration'][AM19['tripduration'].between(AM19['tripduration'].quantile(.1), AM19['tripduration'].quantile(.9))]
AM20['tripduration'] = AM20['tripduration'][AM20['tripduration'].between(AM20['tripduration'].quantile(.1), AM20['tripduration'].quantile(.9))]

AM20['tripduration'].mean()

AM20['covid']='yes'
AM19['covid']='no'

AM19and20 = pd.concat([AM19, AM20], ignore_index=True)

AM19and20['starttimedayofweek']=AM19and20['starttime'].dt.day_name()


AM19and20['gender'].replace(1, 'Male',inplace=True)
AM19and20['gender'].replace(2, 'Female',inplace=True)
AM19and20['gender'].replace(0, 'Unspecified',inplace=True)


AM19and20

AM19and20['starttimehour'] = AM19and20['starttime'].dt.hour
AM19and20

#AM19and20['start station id'].replace('', np.nan, inplace=True)
#AM19and20['start station id'].replace('?', np.nan, inplace=True)

AM19and20['start station id'] = AM19and20['start station id'].dropna()
AM19and20['end station id'] = AM19and20['end station id'].dropna()
AM19and20['birth year'] = AM19and20['birth year'].dropna()

#AM19and20['start station id'] = AM19and20['start station id'].astype(int)

AM19and20['start station id'].isnull().sum()

AM19and20.dtypes

train, test = train_test_split(AM19and20, test_size=0.20, random_state=42)
train, val = train_test_split(train, test_size=0.20,random_state=41)

train.shape , test.shape , val.shape

#train = train.drop(target, axis=1)
train

train.dtypes

target = 'covid'
features = [ 'birth year' , 'tripduration' , 'starttimedayofweek' , 'starttimehour', 'gender']

pipeline.predict([[1985, 600, 'Monday', 8, 'Male' ]])

x_train = train[features]
y_train = train[target]
x_test = test[features]
y_test = test[target]
x_val=val[features]
y_val=val[target]

y_train.value_counts(normalize=True)

from sklearn.linear_model import LogisticRegression
import category_encoders as ce
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder

pipeline = make_pipeline( 
    ce.OneHotEncoder(use_cat_names=True), 
    SimpleImputer(strategy='median'), 
    RandomForestClassifier(random_state=0, max_depth=11,  n_jobs=3, verbose=True)
)

pipeline.fit(x_train,y_train)

pipeline.score(x_val,y_val)

rf = pipeline.named_steps['randomforestclassifier']

x_val.head(
    
)

x_train.head()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

# Get feature importances
rf = pipeline.named_steps['randomforestclassifier']
importances = pd.Series(rf.feature_importances_[0:5], features)

# Plot top n feature importances
n = 5
plt.figure(figsize=(10,n/2))
plt.title('Most predictive features')
importances.sort_values()[-n:].plot.barh();

AM19and20.plot(kind='scatter',x='gender',y='tripduration',color='red')

AM19['birth year'].mean()

AM19and20['gender'].value_counts(normalize=True)

AM20['gender'].value_counts(normalize=True)

AM20['start station latitude']

import seaborn as sns

plt.ticklabel_format(style='plain', axis='y')
sns.countplot(AM19and20['covid'],palette="Set3");



"""BASELINE:

I looked at spring CitiBike rides in NYC in 2020 and compared to 2019. I used data from March and April of each year for my analysis. 81.5% of these spring trips took place in 2019, much simpler times those were!

The features that I used for my model were gender, trip duration, hour of start time, and day of the week. There were no features that leaked information about the target, however there are many that overlap with each other such as information about the starting location.
For instance, what is the relationship between start time, duration of trip, and end time? You can see that they are linked together so therefore it does not make sense to use all 3. 


I started by running a logistic regression on the data with the target being whether the bike ride took place before the pandemic or during.
This test yielded better results than the baseline at 84.4%.
Our random forest model yielded a score of 0.8373 on test data.
"""

pipeline = make_pipeline( 
    ce.OneHotEncoder(use_cat_names=True), 
    SimpleImputer(strategy='median'), 
    LogisticRegression(solver='lbfgs')
)

pipeline.fit(x_train, y_train)

pipeline.score(x_test,y_test)