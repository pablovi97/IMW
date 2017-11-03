
# coding: utf-8

# In[76]:


import sys
dinero = int(sys.argv[1])

billete_50 = dinero //50
resto = dinero % 50  
if billete_50 > 0 : 
    print(billete_50, "billetes de 50")
    
billete_20 = resto //20
resto = dinero % 20    
if billete_20 > 0 :     
    print(billete_20, "billetes de 20")
    
billete_10 = resto// 10
resto = dinero % 10
if billete_10 > 0 :  
    print(billete_10,"billetes de 10" )
    
billete_5 = resto// 5
resto= resto % 5
if billete_5 > 0 : 
    print(billete_5,"billetes de 5")
    
mondea_2 = resto// 2
resto= resto % 2
if moneda_2 > 0 : 
    print(moneda_2,"monedas de 2")

mondea_1 = resto// 1
resto= resto % 2
if moneda_1 > 0 : 
    print(moneda_1,"monedas de 2")

