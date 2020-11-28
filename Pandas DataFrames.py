#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)


# In[3]:


df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df


# In[4]:


type(df)


# In[13]:


type(df[['W','X']])


# In[12]:


df[['W','X']]


# In[14]:


type(df['W'])


# In[28]:


df['Q']=df['W']+df['X']
df


# In[29]:


df.drop('Q',axis=1)
df


# In[30]:



df


# In[31]:


df.drop('Q',axis=1,inplace=True)
df


# In[32]:


df


# In[33]:


df.drop('A')


# In[34]:


df


# In[35]:


df.loc['A']


# In[36]:


df.loc[['A','B']]


# In[37]:


df


# In[38]:


df.loc[['B','C','D'],['X','Y']]


# In[39]:


df>0


# In[40]:


df<0


# In[41]:


df[df>0]


# In[42]:


df['W']>0


# In[43]:


df[df['W']>0]


# In[45]:


df[df['W']>0][['X','Y']]


# In[53]:


df[(df['W']>0)&(df['Y']>0)]


# In[54]:


df.reset_index()


# In[56]:


df['name']='2 3 4 5 6'.split()
df


# In[58]:


df.set_index('name')


# In[59]:


df.loc['new_raw']=[1,2,3,4,5]
df


# In[70]:


dff=pd.DataFrame({'A':[1,2,np.nan],
                 'B':[5,np.nan,np.nan],
                 'C':[1,2,3]})


# In[71]:


dff


# In[72]:


dff.dropna()


# In[73]:


dff.dropna(axis=1)


# In[74]:


dff.dropna(thresh=2)


# In[75]:


dff.dropna(axis=1,thresh=2)


# In[77]:


dff.fillna(value=0)


# In[78]:


dff['A'].fillna(value=dff['A'].mean())


# In[81]:


data={'company':'GOOG GOOG MSFT MSFT FB FB'.split(),
    'Person':'sam charlie amy vanessa carl saraha'.split(),
    'Sales':[200,120,340,124,234,350]}


# In[83]:


DaFr=pd.DataFrame(data)
DaFr


# In[84]:


x=DaFr.groupby('company')


# In[85]:


x.mean()


# In[86]:


x.sum()


# In[87]:


x.std()


# In[89]:


x.sum().loc['FB']


# In[92]:


DaFr.groupby('company').max().loc['GOOG']


# In[95]:


DaFr.groupby('company').describe().transpose()


# In[96]:


'a'+'bc'


# In[ ]:




