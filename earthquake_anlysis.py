#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[69]:


earth_quake = pd.read_csv("earthquake_data.csv")


# In[70]:


earth_quake.T


# In[71]:


earth_quake.columns


# In[72]:


earth_quake.isnull().sum()


# In[ ]:


# Here,many null values are present in the different column of dataset.Also, the columns that we are going to use are cleaned i.e no error is present.


# In[73]:


e_data = earth_quake[["Date","Time","Latitude","Longitude","Magnitude","Depth","Type"]]


# In[ ]:


# Selection of required columns.


# In[74]:


e_data.T


# In[96]:


e_data["Date"] = pd.to_datetime(e_data["Date"],utc=True,)


# In[ ]:


# Conversion of dates


# In[97]:


e_data['Date']


# In[98]:


e_data.pivot_table(index = "Type", values = "Magnitude", aggfunc=len)


# In[144]:


# From the above table, we have number of occurence of Earthquake,Explosion,Nuclear Explosion and Rock Burst values.


# In[145]:


minimum = e_data["Magnitude"].min()
maximum = e_data["Magnitude"].max()
average = e_data["Magnitude"].mean()

print("Minimum:", minimum)
print("Maximum:",maximum)
print("Mean",average)


# In[146]:


#  So,the highest magnitude of earthquake is 9.10 and lowest is 5.5.
#  The mean magnitude of earthquake is 5.88


# In[152]:


e_data.groupby('Magnitude').count().T


# In[148]:


#  The above table shows the number of earthquake occurs at differentt magnitude.


# In[100]:


(n,bins, patches) = plt.hist(e_data["Magnitude"], range=(0,10), bins=10)
plt.xlabel("Earthquake Magnitudes")
plt.ylabel("Number of Occurences")
plt.title("Overview of earthquake magnitudes")

print("Magnitude" +"   "+ "Number of Occurence")
for i in range(5, len(n)):
    print(str(i)+ "-"+str(i+1)+"         " +str(n[i]))


# In[101]:


plt.boxplot(e_data["Magnitude"])
plt.show()


# In[102]:


highly_affected = e_data[e_data["Magnitude"]>=8]


# In[103]:


print(highly_affected.shape)


# In[106]:


e_data["Month"] = e_data['Date'].dt.month


# In[107]:


month_occurrence = e_data.groupby("Month").groups
print(len(month_occurrence[1]))

month = [i for i in range(1,13)]
occurrence = []

for i in range(len(month)):
    val = month_occurrence[month[i]]
    occurrence.append(len(val))

print(occurrence)
print(sum(occurrence))


# In[ ]:


# As per the result above, the chances of having earthquakes is more in the month of March,August and Decemmber.


# In[108]:


fig, ax = plt.subplots(figsize = (10,8))
bar_positions = np.arange(12) + 0.5

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
num_cols = months
bar_heights = occurrence

ax.bar(bar_positions, bar_heights)
tick_positions = np.arange(1,13)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation = 90)
plt.title("Frequency by Month")
plt.xlabel("Months")
plt.ylabel("Frequency")
plt.show()


# In[109]:


e_data["Year"] = e_data['Date'].dt.year


# In[112]:


year_occurrence = e_data.groupby("Year").groups
year = [i for i in range(1965,2017)]
occurrence = []

for i in range(len(year)):
    val = year_occurrence[year[i]]
    occurrence.append(len(val))

maximum = max(occurrence)
minimum = min(occurrence)
print("Maximum",maximum)
print("Minimum",minimum)


# In[153]:


# The maximum Earthquake that occurs in a year is 713 and minimum 234.


# In[154]:


fig = plt.figure(figsize=(10,6))
plt.plot(year,occurrence)
plt.xticks(rotation = 90)
plt.xlabel("Year")
plt.ylabel("Number of Occurrence")
plt.title("Frequency of Earthquakes by Year")
plt.xlim(1965,2017)
plt.show()


# In[114]:


plt.scatter(e_data["Magnitude"],e_data["Depth"])


# In[155]:


# The above graph shows the relationship between Depth and the magnitude.


# In[157]:


supermoon_date = ["2016-11-14","2016-11-16","2016-11-15"] 
#( one day before and after)
supermoon = e_data[e_data['Date'].isin(supermoon_date)]

supermoon


# In[158]:


# The above table shows the occurence of earthquake on the FullMoon with their magnitude.


# In[159]:


#  So, this is all about Earthquake analysis.

#  AKHIL BHALL


# In[ ]:




