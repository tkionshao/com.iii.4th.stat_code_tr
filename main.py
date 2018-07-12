
# coding: utf-8

# In[215]:


import pandas as pd
from math import cos


# # Function

# In[234]:


def stat_code_compute(x):
    scale_km = 0.5
    lat = x[6]
    lon = x[7]
    lat_to_km = lat*110.574
    lon_to_km = lon*(111.320*cos(lat))

    state_code_x = int(lat_to_km//scale_km)
    state_code_y = int(lon_to_km//scale_km)
    state_code = str(state_code_x)+str(state_code_y)
    return state_code


# # Pandas

# In[110]:


rst = pd.read_csv('restaurant_2018_06_22.csv')
type(rst)


# In[9]:


rst.head()


# In[13]:


price = rst['price'].head()
type(price)


# In[20]:


name = rst['name']


# In[26]:


rst.columns


# In[27]:


rst.shape


# In[58]:


rst.describe()


# In[59]:


rst.info()


# In[37]:


rst.sort_values(by='price',ascending=False).head()


# In[54]:


qry = rst[10:21]['Address']
type(qry)


# In[60]:


rst[(rst['price'] > 100) & (rst['price'] < 200)]


# # dplyr

# filter() 函數：SQL 查詢中的 where 描述<br>
# select() 函數：SQL 查詢中的 select 描述<br>
# mutate() 函數：SQL 查詢中的衍生欄位描述<br>
# arrange() 函數：SQL 查詢中的 order by 描述<br>
# summarise() 函數：SQL 查詢中的聚合函數描述<br>
# group_by() 函數：SQL 查詢中的 group by 描述<br>

# ### filter(), where: 
#     use & and | to add the condition of query

# In[92]:


rst[(rst['price'] >= 100) & (rst['name'] == '電商咖啡(信義吳興店)')].head()


# ### select(), select: 
#     put a series of columes as a list in the '[ ]'

# In[96]:


rst[['name','price']].head()


# In[ ]:


rst[['name','price']].head()


# #### mutate():
#     add results of calculations.

# # 1.

# In[98]:


rst['price'].apply(lambda x: x*10000).head()


# In[116]:


rst['priceAdd10000'] = rst['price'].apply(lambda x: x*10000)


# In[117]:


rst.info()


# In[118]:


rst = rst.drop(columns='priceAdd10000')


# In[119]:


rst.info()


# ### 2.

# In[193]:


df = pd.DataFrame({'col_1':[1,3,5,7,9],'col_2':[2,4,6,8,10],'col_3':['a','b','c','d','e']})
df.info()
df


# In[203]:


def f(x):
    return x[0],x[1]


# In[199]:


df.apply(f,axis=1)


# # This is the state code task!

# ## Restaurant

# In[235]:


lat = list(rst.columns).index('lat')
lon = list(rst.columns).index('lon')
(lat,lon)


# In[236]:


def calculation(x):
    return x[6],x[7]


# In[237]:


new_col = rst.apply(stat_code_compute,axis=1)
new_col.head()


# In[238]:


type(new_col)


# In[239]:


new_col.shape


# In[290]:


rst['state_code'] = new_col
new_col.head()


# In[241]:


rst.info()


# In[291]:


rst.to_csv('output/restaurant_statcode.csv','w')


# ## Job

# In[278]:


jb = pd.read_csv('jobs_2018_07_10.csv',header=None)


# In[279]:


jb.columns


# In[280]:


jb.head(1)
jb.columns = ['title','company','address','lat','lon','content','tool','others']
jb.head(2)


# In[281]:


def stat_code_compute_2(x):
    scale_km = 0.5
    lat = x[3]
    lon = x[4]
    lat_to_km = lat*110.574
    lon_to_km = lon*(111.320*cos(lat))

    state_code_x = int(lat_to_km//scale_km)
    state_code_y = int(lon_to_km//scale_km)
    state_code = str(state_code_x)+str(state_code_y)
    return state_code


# In[282]:


new_cl = jb.apply(stat_code_compute_2,axis=1)


# In[283]:


jb['state_code'] = new_cl


# In[284]:


jb.info()


# In[287]:


jb.to_csv('output/job_stat_code.csv','w')


# # Fini
