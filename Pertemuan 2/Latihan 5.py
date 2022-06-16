#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Convert tinggi bandan')
T_Kaki = float(input('Berapa kaki ='))
T_Inci = float(input('Lebih berapa Inci ='))

Tinggi = ((T_Kaki*12) + T_Inci)*2.54
print('Tinggi =',Tinggi,'Cm')

