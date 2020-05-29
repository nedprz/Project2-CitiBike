<<<<<<< Updated upstream
pip install plotly_express
#pip install category_encoders
import calendar
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
pd.options.display.max_columns = None
april20 = pd.read_csv('assets/2020_04.csv')
march20 = pd.read_csv('assets/2020_03.csv')
march19 = pd.read_csv('assets/2019_03.csv')
april19 = pd.read_csv('assets/2019_04.csv')



AM20 = pd.concat([april20, march20], ignore_index=True)
AM19 = pd.concat([march19,april19], ignore_index=True)

AM20['starttime']= pd.to_datetime(AM20['starttime']) 
AM20['stoptime']= pd.to_datetime(AM20['stoptime']) 
AM19['starttime']= pd.to_datetime(AM19['starttime']) 
AM19['stoptime']= pd.to_datetime(AM19['stoptime']) 



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


AM19and20['start station id'].isnull().sum()

train, test = train_test_split(AM19and20, test_size=0.30, random_state=42)
=======
pip install plotly_express
#pip install category_encoders
import calendar
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
pd.options.display.max_columns = None
april20 = pd.read_csv('assets/2020_04.csv')
march20 = pd.read_csv('assets/2020_03.csv')
march19 = pd.read_csv('assets/2019_03.csv')
april19 = pd.read_csv('assets/2019_04.csv')



AM20 = pd.concat([april20, march20], ignore_index=True)
AM19 = pd.concat([march19,april19], ignore_index=True)

AM20['starttime']= pd.to_datetime(AM20['starttime']) 
AM20['stoptime']= pd.to_datetime(AM20['stoptime']) 
AM19['starttime']= pd.to_datetime(AM19['starttime']) 
AM19['stoptime']= pd.to_datetime(AM19['stoptime']) 



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


AM19and20['start station id'].isnull().sum()

train, test = train_test_split(AM19and20, test_size=0.30, random_state=42)
>>>>>>> Stashed changes
