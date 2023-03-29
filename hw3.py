#!/usr/bin/env python
# coding: utf-8

# In[25]:


discount_rate = 0
def get_discount_rate():
    global discount_rate
    discount_rate = int(input("할인율은?"))
    return discount_rate


def get_fixed_price(discounted_price):
    fixed_price = discounted_price / (100 - discount_rate) * 100
    return fixed_price

def main():
    get_discount_rate()
    A_price = int(input("A상품의 할인된 가격은?"))
    B_price = int(input("B상품의 할인된 가격은?"))
    print("A상품의 정가는",get_fixed_price(A_price))
    print("B상품의 정가는",get_fixed_price(B_price))

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




