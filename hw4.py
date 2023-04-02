#!/usr/bin/env python
# coding: utf-8

# In[42]:


def rep_char(c,n):
    print(c*n)
    
def draw_line_string(msg1):
    global msg2
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if(len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(f'{msg1}')
    print(f'{msg2}')
    rep_char('-',nstr)

name = input('Input his/her name:')
msg1 = 'hello, ' + name 
draw_line_string(msg1)


# In[ ]:




