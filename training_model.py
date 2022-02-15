#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as ps 
df = ps.read_csv('Bankdata.csv')


df.drop(['CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1, inplace=True)
df.drop('Avg_Utilization_Ratio',axis=1, inplace=True )
df.drop('Avg_Open_To_Buy',axis=1, inplace=True )
df.Attrition_Flag.replace(('Existing Customer','Attrited Customer'), (0,1), inplace=True)
df.Education_Level.replace(('Graduate','High School', 'Unknown','Uneducated','College','Post-Graduate','Doctorate'), (0,1,2,3,4,5,6), inplace=True)
df.Gender.replace(('M','F'),(0,1), inplace=True)
df.Marital_Status.replace(('Married','Single','Unknown','Divorced'),(0,1,2,3), inplace=True)
df.Income_Category.replace(('Less than $40K','$40K - $60K','$80K - $120K','$60K - $80K','Unknown','$120K +'),(0,1,2,3,4,5), inplace=True)
df.Card_Category.replace(('Blue','Silver','Gold','Platinum'),(0,1,2,3), inplace=True)


from sklearn.model_selection import train_test_split
y = df['Attrition_Flag']
x = df.drop('Attrition_Flag', axis=1)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.1)


import pickle 
from sklearn.ensemble import RandomForestClassifier


randomforest = RandomForestClassifier()
randomforest.fit(x_train.values, y_train)
y_pred = randomforest.predict(x_val)



filename = 'test.sav'
pickle.dump(randomforest, open(filename, 'wb'))


# In[ ]:




