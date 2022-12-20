#!/usr/bin/env python
# coding: utf-8

# In[37]:


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
tab = pd.read_csv('tabela.csv')
display(tab)
plt.plot(tab['Vendedor(a)'], tab['TV'], label='TV', color='black')
plt.plot(tab['Vendedor(a)'], tab['Smartphone'],'--', label='Smartphone')
plt.axis([-0.75,5.75,0,25])
plt.xlabel('Vendedor(a)')
plt.ylabel('Unidade')
plt.title('Quantidade de Produtos Vendidos')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




