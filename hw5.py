#!/usr/bin/env python
# coding: utf-8

# In[3]:


def read_single_digit(num):
    if num == 0:
        return '영'
    elif num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'
    
def read_number(num):
    return f'{read_single_digit(num//100)} {read_single_digit((num%100)//10)} {read_single_digit(num%10)}'

num = int(input('세 자리 정수를 입력하시오'))
read_number(num)


# In[ ]:


()

