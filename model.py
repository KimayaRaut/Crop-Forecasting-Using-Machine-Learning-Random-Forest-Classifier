#!/usr/bin/env python
# coding: utf-8

# # Random Forest Classification

# ## Importing the libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


# ## Importing the dataset

# In[2]:


dataset = pd.read_csv('Crop_recommendation.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[3]:


print(X)


# In[4]:


print(y)


# # Encoding the Dependent Variable

# In[5]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


# In[6]:


print(y)


# ## Splitting the dataset into the Training set and Test set

# In[7]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# In[8]:


print("X Train Size:",len(X_train))
print(X_train)


# In[9]:


print("X Test Size:",len(X_test))
print(X_test)


# In[10]:


print("Y Train Size:",len(y_train))
print(y_train)


# In[11]:


print("X Test Size:",len(y_test))
print(y_test)


# ## Feature Scaling

# ## Training the Random Forest Classification model on the Training set

# In[12]:


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)


# ## Making the Confusion Matrix

# In[13]:


from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

## Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))

# Saving model to disk
pickle.dump(classifier, open('model.pkl','wb'))

