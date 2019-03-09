
# coding: utf-8

# In[10]:


import pandas as pd


# In[11]:


d={'Text':['a great game','the election was game over','the very clean match and was a well fought election','a clean but forgettable game','it was a close and clean election'],'class':['sports','not sports','sports','sports','not sports']}
df=pd.DataFrame(data=d)
print(df)


# In[12]:


a=df.groupby('class').get_group('sports')
b = a['Text'].str.cat(sep=' ')
print(b)


# In[13]:


a1=df.groupby('class').get_group('not sports')
b1 = a1['Text'].str.cat(sep=' ')
print(b1)


# In[14]:


from collections import Counter


# In[15]:


list1=b.split()
counts = Counter(list1)
print(counts)
print(type(counts))

list1=b1.split()
counts1 = Counter(list1)
print(counts1)
#print(type(counts))


# In[16]:


df1 = pd.DataFrame.from_dict(counts, orient='index').reset_index()
#print(df1)
#dfw=df1.rename(columns = {'words':'counts'})
#print(dfw)
df1 = df1.rename(columns={'index': 'words', 0: 'counts'})
print(df1)
#print(df1.loc[df1['words'] == 'the']['counts'].iloc[0])


# In[17]:


df2 = pd.DataFrame.from_dict(counts1, orient='index').reset_index()

df2 = df2.rename(columns={'index': 'words', 0: 'counts'})
print(df2)
#print(df2.loc[df2['words'] == 'the']['counts'].iloc[0])
print


# In[18]:


test=input("Enter a sentence")


# In[19]:


test1=test.split()
print(test1)
testcount=Counter(test1)
print(df1.index[-1]+df1.index[3])
print(df1['counts'].sum())


# In[32]:


x=1
for i in range(0,len(test1)):
    
    var = df1.loc[df1['words'] == test1[i]]['counts']
    if(len(var)==0):
        x=1/((df1['counts'].sum())+(df1.index[-1]+1))
        
    else:
        x=x*((df1.loc[df1['words'] == test1[i]]['counts'].iloc[0])/18)
        
    
ans1=x*0.6
print(ans1)
#f=1/((df2['counts'].sum())+(df2.index[-1]+1))
#print(f)
#var=df2.loc[df2['words'] == test1[2]]['counts']
#print(var)


# In[33]:


f=1
for i in range(0,len(test1)):
    var = df2.loc[df2['words'] == test1[i]]['counts']
    if(len(var)==0):
        f=1/((df2['counts'].sum())+(df2.index[-1]+1))
    else:
        f=f*((df2.loc[df2['words'] == test1[i]]['counts'].iloc[0])/12)
        
        
        
ans2=f*0.4
print(ans2)
        

    


# In[34]:


if(ans1>ans2):
    print("the given documnet belongs to sports")
else:
    print("the given document belongs to not sports")
    

