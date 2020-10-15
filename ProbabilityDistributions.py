#!/usr/bin/env python
# coding: utf-8

# # Probability Distributions and plots using Python

# In[1]:


#importing all necessary python modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#setting seaborn styles
sns.set(color_codes=True)


# In[3]:


#setting plot size
sns.set(rc={'figure.figsize':(5,5)})


# In[4]:


#reading csv- marks of 60 students out of 50
data = pd.read_csv('fictional_marks.csv')


# In[5]:


#first five rows of the dataset
data.head()


# In[6]:


#relational plot of students' marks and claiming the response eg.student with marks 25 doesn't want extra class
#by default scatterplot
ax = sns.relplot(x='Response for Extra Class',y='Total Marks',data=data)


# In[7]:


#line plot 
ax = sns.relplot(x='Response for Extra Class',y='Total Marks',data=data,kind='line')


# In[8]:


#column marks - array
marks = data['Total Marks']


# In[9]:


# a histogram 
ax = sns.distplot(
    marks,
    hist=True,
    bins=50,
    color='skyblue',
    hist_kws={'linewidth':20,'alpha':1}
)


# # Another Dataset Analysis

# In[10]:


Data_2 = pd.read_csv('fictional_studentinfo.csv')


# In[11]:


Data_2.head()


# In[ ]:





# # Probability Distributions

# # By using sns.displot():

# # Uniform Distribution:

# In[12]:


#importing uniform function from scipy stats
from scipy.stats import uniform


# In[13]:


# generating uniform distributed random numbers starting from 10 with scale of 20 and size 1000
n=1000
start=10
width=20
data_uniform = uniform.rvs(size=n,loc=start,scale=width)


# In[14]:


ax= sns.displot(
    data_uniform,
    bins=100,
    kde=True,
    color='skyblue'
)
ax.set(xlabel='Uniform Distribution',ylabel='Frequency')


# # Normal Distribution:

# In[15]:


#importing normal function from scipy stats
from scipy.stats import norm


# In[16]:


#generating normal distributed random variables;loc,scale being mean and standard deviation respectively
data_normal = norm.rvs(size=1000,loc=0,scale=1)


# In[17]:


ax= sns.displot(
    data_normal,
    bins=100,
    kde=True,
    color='skyblue'
)
ax.set(xlabel='Normal Distribution',ylabel='Frequency')


# # Poisson Distribution:

# In[18]:


#importing poisson function from scipy stats
from scipy.stats import poisson


# In[19]:


#generating poisson distributed random varibales 
data_poisson = poisson.rvs(mu=6,size=1000)


# In[20]:


ax= sns.displot(
    data_poisson,
    bins=100,
    kde=False,
    color='skyblue',
)
ax.set(xlabel='Poisson Distribution',ylabel='Frequency')


# # By using sns.distplot():

# # Poisson Distribution:

# In[21]:


ax= sns.distplot(
    data_poisson,
    bins=100,
    kde=False,
    color='skyblue',
    hist_kws={'linewidth':15,'alpha':1}
)
ax.set(xlabel='Poisson Distribution',ylabel='Frequency')


# # Normal Distribution:

# In[22]:


ax= sns.distplot(
    data_normal,
    bins=100,
    kde=True,
    color='skyblue',
    hist_kws={"linewidth":20,"alpha":1}
)
ax.set(xlabel='Normal Distribution',ylabel='Frequency')


# # Uniform Distribution:

# In[23]:


ax = sns.distplot(
    data_uniform,
    bins=100,
    kde=True,
    color='skyblue',
    hist_kws={'linewidth':20,'alpha':1}
)
ax.set(xlabel='Uniform Distribution',ylabel='Frequency')


# # Bernoulli Distribution

# In[ ]:





# In[ ]:




