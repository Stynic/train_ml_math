#!/usr/bin/env python
# coding: utf-8

# # Функции
# ### Домашнее задание

# #### 1.
# Почему возникла ошибка? Объясните и исправьте.

# In[3]:


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

print(factorial(3))


# **Объяснение:** 
# <br>Because, we try to call the local variable of the function is factorial from global namespace<br>

# #### 2.
# Почему переменная S после запуска функции сохранила значение ноль?

# In[4]:


S = 0
def sum1(n, m):
    S = n + m
    return S

print(sum1(3, 4))
print(S)


# **Объяснение:** 
# <br>As, create the local variable S in the function sum1 and it shadows global variabe S<br>

# #### 3.
# Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере с `res`.

# In[5]:


def mult(q, w, e, r, t, y):
    return q + w + e + r + t + y
res = mult(1, 2, 3, 4, 5, 6)


# **Объяснение:** 
# <br>unnecessary argument is *<br>

# #### 4.
# Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере.

# In[11]:


def power(a, s, *, d):
    res = a ** s ** d
    print(res)
    
power(5, 6, d = 4)


# **Объяснение:** 
# <br>not correct order agruments in the call fuction<br>

# #### 5.
# Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере.

# In[12]:


def mult2(*args):
    res = 1
    for i in args:
        res += i
    return res

List = [1, 2, 3, 4, 5, 6, 7]
print(mult2(*List))


# **Объяснение:** 
# <br>Need to unpack variable with name is List<br>

# #### 6.
# Почему возникла ошибка? Объясните и исправьте.

# In[13]:


def some_function(a, b, *args, **kwargs):
    pass


# **Объяснение:** 
# <br>As in function had uncorrect order of the arguments<br>

# #### 7.
# Почему не был создан новый список при повторном запуске функции? Объясните и исправьте.

# In[17]:


def to_buy(*new_items, shopping_list = None):
    shopping_list = []
    for i in new_items:
        shopping_list.append(i)
    return shopping_list

monday = to_buy('яблоки', 'молоко', 'хлеб')
print(monday)

tuesday = to_buy('груши', 'йогурт', 'мясо', shopping_list=[])
print(tuesday)


# **Объяснение:** 
# <br>In function was the mutable type in value of the name arguments, it is not correct<br>

# #### 8.
# Измените данную функцию так, чтобы она распечатывала названия продуктов из словаря в примере.
# 

# In[23]:


def print_all(**kwargs):
    for v in kwargs.values():
        print(v)
        
products = {'1' : 'яблоки', '2' :'молоко', '3' : 'хлеб', '4' : 'груши', '5' : 'йогурт', '6' : 'мясо'}        
print_all(**products)


# #### 9.
# Программисты договорились, что переменные такого рода являются.. *(вопрос из лекции)*

# In[ ]:


TOKEN = ... 


# **Ответ:** 
# <br>
# CONSTANT
# <br>

# #### 10.
# Напишите функцию, которая с помощью рекурсии считает сумму последовательности с шагом m. В качестве аргументов подаются целые положительные числа n (последний элемент последовательности) и m (шаг последовательности). Считается, что все члены последовательности являются целыми положительными числами.
# 
# Пример:
# 
# ```
# sum_of_seq(5, 1)
# 15
#  
# sum_of_seq(5, 9)
# 5
# 
# sum_of_seq(8, 2)
# 20
# ```
# 

# In[42]:


### YOUR CODE HERE ###
def sum_range(n, step):
    result = 0
    if n <= 0:
        return n
    else:
        print(n - step, step)
        result = sum_range(n - step, step)
        

print(sum_range(5, 1))

# print(sum_range(5, 9))


# #### 11.
# Напишите функцию, которая возводит число в положительную степень с помощью рекурсии. В качестве аргументов подаются целые положительные числа n (число) и m (степень).

# In[ ]:


### YOUR CODE HERE ###


# #### 12.
# Напишите функцию, которая возводит число в отрицательную степень число с помощью рекурсии. В качестве аргументов подаются целое положительное число n (число) и целое отрицательное число m (степень).

# In[ ]:


### YOUR CODE HERE ###


# #### 13.
# 
# Напишите функцию, которая находит число Фиббоначи по его номеру. В качестве аргумента подается целое положительное число n (число).

# In[ ]:


### YOUR CODE HERE ###

