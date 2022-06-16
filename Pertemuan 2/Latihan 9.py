#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Konversi Tekanan')
kilopascal = float(input('tekanan(kilopascal) ='))
psi = kilopascal*0.1450377
mmHg = kilopascal*7.50062
atm = kilopascal*0.00986923

print('tekanan =',kilopascal,'kilopascal')
print('        =',psi,'psi')
print('        =',mmHg,'mmHg')
print('        =',atm,'atm')

