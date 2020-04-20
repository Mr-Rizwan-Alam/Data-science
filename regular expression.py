#!/usr/bin/env python
# coding: utf-8

# # re.match()

# In[3]:


import re
str='love to learn python'
x=re.match('love',str)
print(x)


# In[6]:


x=re.match('python',str)
print(x)


# # # re.search()

# In[10]:


str='love to learn python'
x=re.search('python',str)
print(x)


# ##re.findall()

# In[15]:


str= r'i founded coursera, I also founded deep learning'
x=re.findall('founded', str)
print(x)


# # special sequences

# \b returns a match where specified pattern is at the end of a word

# In[17]:


str= r'analytics vidhya is the largest analytics community in india'
x=re.findall(r'ics\b',str)
print(x)


# \d returns a match when a string contain digits

# In[19]:


str='2 million views was a sucessful attempt in jan19'
x=re.findall(r'\d+',str)
print(x)


# \D returns non numberical data in the string

# In[20]:


x=re.findall(r'\D+',str)
print(x)


# \w and \W helps us to get alphanumeric and non alphanumeric data

# In[23]:


str='i am really Excited for the 20_party!! #@live'
x=re.findall(r'\w+',str)
print(x)


# In[24]:


str='i am really Excited for the 20_party!! #@live'
x=re.findall(r'\W+',str)
print(x)


# In[ ]:




