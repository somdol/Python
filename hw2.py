#!/usr/bin/env python
# coding: utf-8

# In[6]:


def exchange(money):
    c500 = money // 500
    money %= 500
    c100 = money // 100
    money %= 100
    c50 = money // 50
    money %= 50
    c10 = money // 10
    print('500원:',c500,'개')
    print('100원:',c100,'개')
    print('50원:',c50,'개')
    print('10원:',c10,'개')

def get_integer(prompt):
    res = int(input(prompt))
    return res

money = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(money)


# In[ ]:




