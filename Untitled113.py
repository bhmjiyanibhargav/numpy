#!/usr/bin/env python
# coding: utf-8

# # question 01
Yes, there is a difference in the data type of the variables list_ and array_list. list_ is a Python list object, while array_list is a NumPy array object.

To print the data types of both variables, you can use the type() function as follows:
# In[1]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print(type(list_))  # prints "<class 'list'>"
print(type(array_list))  # prints "<class 'numpy.ndarray'>"


# # question 02
To print the data type of each and every element of the list_ and array_list variables, you can use a loop to iterate through each element and then use the type() function to print its data type. Here's the code:
# In[2]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(list_)

# Print data types of elements in the list
for element in list_:
    print(type(element))

# Print data types of elements in the NumPy array
for element in array_list:
    print(type(element))


# # question 03
Yes, there will be a difference in the data type of the elements present in both the list_ and array_list variables after applying dtype=int to array_list. The dtype parameter specifies the data type of the elements in the array, and in this case, it is set to int.

To print the data types of each element in both variables, you can use a loop to iterate through each element and then use the type() function to print its data type. Here's the code:
# In[3]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(list_, dtype=int)

# Print data types of elements in the list
for element in list_:
    print(type(element))

# Print data types of elements in the NumPy array
for element in array_list:
    print(type(element))


# # question 04
To find the shape and size of the num_array variable, you can use the shape and size attributes of the NumPy array object, respectively. Here's the code:
# In[4]:


import numpy as np

num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(num_list)

# Find the shape of the NumPy array
print(num_array.shape)  # Output: (2, 3)

# Find the size of the NumPy array
print(num_array.size)  # Output: 6


# # question 05
To create a NumPy array of a 3x3 matrix containing only zeros, you can use the zeros function from the NumPy library. Here's the code:
# In[5]:


import numpy as np

# Create a NumPy array of a 3x3 matrix containing zeros only
zeros_array = np.zeros((3, 3))

# Print the NumPy array
print(zeros_array)


# # question 06
To create an identity matrix of shape (5, 5) using NumPy functions, you can use the identity function. Here's the code:
# In[6]:


import numpy as np

# Create an identity matrix of shape (5, 5)
identity_matrix = np.identity(5)

# Print the identity matrix
print(identity_matrix)


# In[ ]:




