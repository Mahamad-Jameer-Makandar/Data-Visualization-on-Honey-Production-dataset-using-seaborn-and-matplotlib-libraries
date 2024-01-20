#!/usr/bin/env python
# coding: utf-8

# ### 1. Import required libraries and read the dataset.

# In[74]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


# ### 2. Check the first few samples, shape, info of the data and try to familiarize yourself with different features.

# In[4]:


honey = pd.read_csv(r"C:\Users\Jameer_Ibn_Hasan\Downloads\honeyproduction.csv")


# In[5]:


honey.head(10)


# In[6]:


honey.tail(10)


# In[8]:


honey.shape


# In[7]:


honey.info()


# In[9]:


honey.nunique()


# In[14]:


honey.describe(include="all")


# ### 3. Display the percentage distribution of the data in each year using the pie chart.
# 

# In[28]:


honey.year.nunique()


# In[24]:


prod_dist = honey.groupby("year")["state"].count()


# In[31]:


honey.year.unique()


# In[34]:


labels= [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
       2009, 2010, 2011, 2012]

plt.pie(prod_dist, autopct= "%.1f%%", labels=labels)

plt.show()


# ### 4. Plot and Understand the distribution of the variable "price per lb" using displot, and write your findings.
# 

# In[38]:


sns.displot(honey.priceperlb, bins=10)
plt.title("distribution of price_per_lb")
plt.show()


# ### 5. Plot and understand the relationship between the variables 'numcol' and 'prodval' through scatterplot, and write your findings.
# 

# In[46]:


sns.scatterplot(x=honey.numcol, y=honey.prodvalue)
plt.title('''number of honey producing colonies
          \n VS value of production''')
plt.show()


# ### 6. Plot and understand the relationship between categorical variable 'year' and a numerical variable "prodvalue" through boxplot, and write your findings.

# In[50]:


honey.year.unique()


# In[58]:


fig, a1 = plt.subplots(1,figsize=(10,8))
sns.boxplot(honey.year, honey.prodvalue)
plt.show()


# ### 7. Visualize and understand the relationship between the multiple pairs of variables throughout different years using pairplot and add your inferences. (use columns 'numcol', 'yield percol', 'total prod', 'prodvalue','year')
# 

# In[66]:


sns.pairplot(honey)
plt.show()


# ### 8. Display the correlation values using a plot and add your inferences. (use columns 'numcol', 'yield percol', 'total prod', 'stocks', 'price per lb', 'prodvalue')

# In[73]:


sns.heatmap(honey.corr(), annot = True, cmap = 'hot')
plt.title("correletion of all variables")
plt.show()


# ### Heatmap provides the correlation between all the variables
# ### 1) prodvalue and yieldpercol, numcol and prodvalue are positiely correleted.
# ### 2) year and totalprod are negatively corelated.

# In[ ]:




