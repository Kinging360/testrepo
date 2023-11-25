#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem
# 

# In this notebook, Data Science Tools and Ecosystem are summarized.

# Some of the popular languages that Data Scientists use are:

# In[2]:


data_science_languages = [
    "Python",
    "R",
    "SQL",
    "Java"
]
numbered_list = "\n".join(f"{i+1}. {language}" for i, language in enumerate(data_science_languages))
print(numbered_list)


# Some of the commonly used libraries used by Data Scientists include:

# In[9]:


data_science_libraries = [
    "Numpy",
    "Pandas",
    "Matplotlib",
    "Scikit-learn"
]
numbered_list = "\n".join(f"{i+1}. {library}" for i, library in enumerate(data_science_libraries))
print(numbered_list)


# In[10]:


header = "Data Science Tools"
tools = ["Jupyter Notebook", "RStudio", "Apache Zeppelin"]
table_width = len(header)
print(f"|{header.center(table_width)}|")
print("|" + "-" * table_width + "|")
for tool in tools:
    print(f"|{tool.center(table_width)}|")


# ### Below are a few examples of evaluating arithmetic expressions in Python
# 

# In[16]:


(3*4)+5
#This a simple arithmetic expression to mutiply then add integers


# In[18]:


x = 200/60
print("200 minutes is equal to", x)


# **Objectives**

# In[20]:


data_science_languages = ["Python", "R", "SQL", "Java", "Julia", "Scala", "MATLAB"]

for language in data_science_languages:
    print(language)


# ## Author
# 
# Chukwuemerie Igbokwe

# In[ ]:




