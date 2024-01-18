#!/usr/bin/env python
# coding: utf-8

# In[1]:


#statistics(used for data preprocessing)
#Numerical Data:(Numerical data, also known as quantitative or continuous data, consists of measurable quantities that represent different magnitudes of the same variable).
#properties
#Discrete Data: Consists of distinct, separate values. For example, the number of cars in a parking lot or the number of students in a classroom.
#Continuous Data: Can take any value within a given range. For example, height or weight can have any value within a specific range.
#Categorical Data:(Categorical data, also known as qualitative or nominal data, represents categories or labels and cannot be measured in terms of numerical values)
#Properties
#Nominal Data: Categories with no inherent order or ranking. For example, colors or types of fruits.
#Ordinal Data: Categories with a meaningful order or ranking. For example, educational levels such as high school, bachelor's, master's, and doctoral degrees..



# In[4]:


#MEAN
#In statistics, the mean is a measure of central tendency that represents the average value of a set of numbers. It is calculated by adding up all the values in a data set and then dividing the sum by the total number of values. The mean is often denoted by the symbol "μ" for a population mean or "x̄" for a sample mean.
#MEDIAN
# The median is the middle value of a dataset when it is ordered from least to greatest. If there is an even number of observations, the median is the average of the two middle values.
#MODE
#The mode is the value that appears most frequently in a dataset.


# In[10]:


import pandas as pd
import numpy as np
df5 = pd.DataFrame({'col' : [1,2, 10, np.nan, 56], 
                   'col2': [8, 10, 30, 40 ,50],
                   'col3': [1,2,3,4,5.0]})


# In[11]:


df5


# In[12]:


df5.corr()


# In[13]:


df5.mean()


# In[14]:


df5.count()


# In[15]:


df5.max()


# In[16]:


df5.min()


# In[17]:


df5.median()


# In[20]:


df5.std()


# In[ ]:





# In[ ]:




