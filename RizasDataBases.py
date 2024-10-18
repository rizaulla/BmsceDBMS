#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sqlite3
conn = sqlite3.connect('InsuranceDB.db')
c = conn.cursor()


# In[5]:


c.execute("CREATE TABLE Person( Driver_id varchar(10), Name varchar(20), Address varchar(30),Primary Key(Driver_id))")


# In[6]:


Pe=[ ( "451", "Razza","BAllari"),
         ( "452" ,  "Arjun" , "BAnglore"),
          ( "453" ,  "Riza" , "Kodagu"),
           ( "454" ,  "Tejas" , "Banglore"),
           ( "455" ,  "Kushalappa" , "Manglore")]
c.executemany("INSERT INTO Person Values(?,?,?)",Pe)


# In[7]:


for row in c.execute("Select * From Person"):
    print(row)


# In[8]:


c.execute("CREATE TABLE Car( Reg_num varchar(12), Model varchar(20), Year Int(4),Primary Key(Reg_num))")


# In[9]:


Pe=[ ( "KA12E2536", "Mahindra Xuv500 ","2013"),
         ( "KA51EZ6970" ,  "Skoda Octivia" , "2002"),
          ( "KA09MP5236" ,  "Ford Escort" , "2000"),
           ( "KA13Z2585" ,  "VW polo" , "2015"),
           ( "KA15X0101" ,  "HM Contessa" , "1992")]
c.executemany("INSERT INTO Car Values(?,?,?)",Pe)


# In[10]:


for row in c.execute("Select * From Car"):
    print(row)


# In[11]:


c.execute("CREATE TABLE Accident( Report_num varchar(12), Accident_date date, Location varchar(30),Primary Key(Report_num))")


# In[12]:


Pe=[ ( "KA12E3636", "Mahindra Xuv700 ","2016"),
         ( "KA053408" ,  "Skoda Octivia" , "2003")]
c.executemany("INSERT INTO Car Values(?,?,?)",Pe)
for row in c.execute("Select * From Car"):
    print(row)


# In[13]:


Pe=[ ( "11", "10/8/2024","Banglore"),
         ( "12", "9/10/2024","Mysore"),
          ( "13", "13/5/2024","Banglore"),
           ( "14", "10/4/2024","Kodagu"),
           ( "15", "22/8/2024","Hassan")]
c.executemany("INSERT INTO Accident Values(?,?,?)",Pe)
for row in c.execute("Select * From Accident"):
    print(row)


# In[14]:


for row in c.execute("Select * From Car"):
    print(row)


# In[15]:


c.execute("CREATE TABLE Owns( Driver_id varchar(10),Report_num varchar(12),Primary Key(Driver_id,Report_num), foreign key(Driver_id) references Person(Driver_id), foreign key (Report_num) references Accident(Report_num))")


# In[16]:


Pe=[ ( "451", "11"),
         ( "452" ,  "12"),
          ( "453" , "13"),]
c.executemany("INSERT INTO Owns Values(?,?)",Pe)
    


# In[17]:


for row in c.execute("Select * From Owns"):
    print(row)


# In[18]:


c.execute("CREATE TABLE Participated( Driver_id varchar(10),Reg_num varchar(12),Report_num varchar(12),Damage_amount int(200000000),Primary Key(Driver_id,Report_num,Reg_num), foreign key(Driver_id) references Person(Driver_id), foreign key (Report_num) references Accident(Report_num),foreign key (Reg_num) references Car(Reg_num))")


# In[19]:


Pe=[ ( "451","KA12E2536", "11", 20000),
         ( "452" ,"KA053408",  "12", 15000),
          ( "453" ,"KA09MP5236", "13", 30000),]
c.executemany("INSERT INTO Participated Values(?,?,?,?)",Pe)


# In[20]:


for row in c.execute("Select * From Participated"):
    print(row)


# In[21]:


cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()
for table in tables:
    print(table[0])


# In[22]:


for row in c.execute("Select * From Participated"):
    
    print(row)


# In[23]:


for row in c.execute("Select * From Person"):
    print(row)


# In[24]:


for row in c.execute("Select * From Car"):
    print(row)

