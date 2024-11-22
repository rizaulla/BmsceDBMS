#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sqlite3
conn = sqlite3.connect('SuppliersDataBase1.db')
c = conn.cursor()


# In[18]:


c.execute("CREATE TABLE Suppliers( Suplier_id int,SName varchar(20),Address varchar(400) ,Primary Key(Suplier_id))")


# In[19]:


c.execute("CREATE TABLE Part( P_id int,PName varchar(20),Color varchar(400) ,Primary Key(P_id))")


# In[20]:



c.execute("CREATE TABLE Catalog( S_id int,P_id int,Cost real ,foreign key(S_id) references Suppliers(Suplier_id),foreign key(P_id) references Part(P_id))")


# In[21]:


Pe=[ ( "451", "Razza","BAllari"),
         ( "452" ,  "Arjun" , "BAnglore"),
          ( "453" ,  "Riza" , "Kodagu"),
           ( "454" ,  "Tejas" , "Banglore"),
           ( "455" ,  "Kushalappa" , "Manglore")]
c.executemany("INSERT INTO Suppliers Values(?,?,?)",Pe)


# In[22]:


Pe=[ ( "111", "bolt","grey"),
         ( "111" ,  "nut" , "grey"),
          ( "111" ,  "greeze" , "yellow"),
           ( "111" ,  "washer" , "golden"),
           ( "111" ,  "screw" , "black")
           ( "112", "bolt","grey"),
         ( "112" ,  "nut" , "grey"),
          ( "111" ,  "greeze" , "yellow"),
           ( "111" ,  "washer" , "golden"),
           ( "111" ,  "screw" , "black")]
c.executemany("INSERT INTO Part Values(?,?,?)",Pe)


# In[27]:


Pe=[ ( "451", "111","10000"),
         ( "451" ,  "112" , "10000"),
          ( "451" ,  "113" , "50000"),
           ( "451" ,  "114" , "15000"),
           ( "451" ,  "115" , "5000"),
           ( "452", "111","10000"),
         ( "452" ,  "112" , "10000"),
          ( "452" ,  "113" , "50000"),
           ( "453" ,  "114" , "15000"),
           ( "454" ,  "115" , "5000")]
c.executemany("INSERT INTO Catalog Values(?,?,?)",Pe)


# In[24]:


for row in c.execute("Select * From Suppliers "):
    print(row)


# In[25]:


for row in c.execute("Select * From Part "):
    print(row)


# In[28]:


for row in c.execute("Select * From Catalog "):
    print(row)


# In[35]:


for row in c.execute("Select s.Sname,c.color From Suppliers s, Catalog c ,part p where p.color=Yellow "):
    print(row)


# In[32]:


#find the p_names of parts supplied by acne widget/ supp 3
c.execute('''SELECT 
            
             )''')
for row in c.fetchall():
    print(row)


# In[ ]:




