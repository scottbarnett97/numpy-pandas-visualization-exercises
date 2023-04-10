#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np


# In[31]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# # 1
# How many negative numbers are there?

# In[7]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a <0)


# In[8]:


# this breaks out the list of negatives
a[a < 0]


# In[9]:


# this counts the list
len(a[a < 0])


# # 2 
# How many positive numbers are there?
# 
# 
# 
# 

# In[10]:


# this breaks out the list of positives
a[a > 0]


# In[11]:


# this counts the list
len(a[a > 0])


# # 3
# How many even positive numbers are there?
# 

# In[12]:


# this breaks out the list of positives
a[a > 0]


# In[13]:


# this breaks out the evens
b = a[a>0]
b[b % 2 == 0] 


# In[14]:


# counts the positve even
len(b[b % 2 == 0] )


# In[ ]:





# # 4
# If you were to add 3 to each data point, how many positive numbers would there be?
# 

# In[20]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# add 3 to array
c = a + 3
print(c)


# In[22]:


# break out the positives
d = c [c>0]
print(d)


# In[23]:


len(d)


# In[ ]:





# # 5
# If you squared each number, what would the new mean and standard deviation be?

# In[33]:


g=a**2
print(g)


# In[36]:


# this is the mean
np.mean(g)


# In[37]:


# this is the standard deviation

np.std(g)


# # 6
# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
# 
# subtract the std from every value in the set

# In[38]:


a- (np.std(a))


# # 7
# 
# Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# #### Z=x-μ/σ
# where:
# 
# X is a single raw data value
# μ is the population mean
# σ is the population standard deviation
# 

# In[45]:


x = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[47]:


# STD
o=np.std(x)
print(o)


# In[48]:


#Mean
m=np.mean(x)
print(m)


# In[57]:


z= (x-m)/o

print(z)


# In[ ]:





# from review
Use the following code for the questions below:
import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a
array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])
How many negative numbers are there?
a < 0
array([False, False, False, False,  True,  True, False, False, False,
        True, False,  True])
a[a<0]
array([-2, -1, -6, -7])
len(a[a<0])
4
How many positive numbers are there?
len(a[a>0])
5
How many even positive numbers are there?
pos_nums = a[a>0]
pos_nums
array([ 4, 10, 12, 23,  3])
pos_nums[pos_nums % 2 == 0]
array([ 4, 10, 12])
len(pos_nums[pos_nums % 2 == 0])
3
if you were to add 3 to each data point, how many positive numbers would there be?
a+3
array([ 7, 13, 15, 26,  1,  2,  3,  3,  3, -3,  6, -4])
len(a[(a+3)>0])
10
If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2
a_squared
array([ 16, 100, 144, 529,   4,   1,   0,   0,   0,  36,   9,  49])
a_squared.mean()
74.0
a_squared.std()
144.0243035046516
A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0.
centered_a = a - a.mean()
centered_a
array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0.,
       -10.])
centered_a.mean()
0.0
Calculate the z-score for each data point.
z_scores = centered_a / a.std()
z_scores
array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
        0.        , -1.24034735])
Use the more numpy practice link and follow the questions within it.
Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Use python's built in functionality/operators to determine the following:
Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
type(a)
list
sum(a)
55
Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min(a)
1
Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max(a)
10
Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
sum(a) / len(a)
5.5
Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
prod_a = 1
for n in a:
    prod_a *= n
prod_a
3628800
Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
[n ** 2 for n in a]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
[n for n in a if n % 2 != 0]
[1, 3, 5, 7, 9]
Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
[n for n in a if n % 2 == 0]
[2, 4, 6, 8, 10]
What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b2 = np.array(b)
b
[[3, 4, 5], [6, 7, 8]]
b2
array([[3, 4, 5],
       [6, 7, 8]])
Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. Hint, you'll first need to make sure that the "b" variable is a numpy array
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b
33
b2.sum()
33
Exercise 2 - refactor the following to use numpy.
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b
3
b2.min()
3
Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b
8
b2.max()
8
# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b
5.5
b2.mean()
5.5
Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b
20160
b2.prod()
20160
np.prod(b2)
20160
Exercise 6 - refactor the following to use numpy to find the list of squares
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b
[9, 16, 25, 36, 49, 64]
np.square(b2)
array([[ 9, 16, 25],
       [36, 49, 64]])
b2 ** 2
array([[ 9, 16, 25],
       [36, 49, 64]])
Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b
[3, 5, 7]
b2[b2 % 2 != 0]
array([3, 5, 7])
Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b
[4, 6, 8]
b2[b2 % 2 == 0]
array([4, 6, 8])
Exercise 9 - print out the shape of the array b.
b2.shape
(2, 3)
Exercise 10 - transpose the array b.
b2
array([[3, 4, 5],
       [6, 7, 8]])
b2.transpose()
array([[3, 6],
       [4, 7],
       [5, 8]])
Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b2.reshape(1,6)
array([[3, 4, 5, 6, 7, 8]])
Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b2.reshape(6,1)
array([[3],
       [4],
       [5],
       [6],
       [7],
       [8]])
Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)
Exercise 1 - Find the min, max, sum, and product of c.
c.min(), c.max(), c.sum(), c.prod()
(1, 9, 45, 362880)
Exercise 2 - Determine the standard deviation of c.
c.std()
2.581988897471611
Exercise 3 - Determine the variance of c.
c.var()
6.666666666666667
Exercise 4 - Print out the shape of the array c
c.shape
(3, 3)
Exercise 5 - Transpose c and print out transposed result.
c.transpose()
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
Exercise 6 - Get the dot product of the array c with c.
np.dot(c, c)
array([[ 30,  36,  42],
       [ 66,  81,  96],
       [102, 126, 150]])
Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
np.sum(c * c.transpose())
261
Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
np.prod(c * c.transpose())
131681894400
Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
        -0.80115264],
       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
         0.        ],
       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
        -0.80115264]])
Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
        -0.59846007],
       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
         1.        ],
       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
        -0.59846007]])
Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
         1.33869021],
       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
         0.        ],
       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
         1.33869021]])
Exercise 4 - Find all the negative numbers in d
d[d < 0]
array([-90, -30, -45, -45])
Exercise 5 - Find all the positive numbers in d
d[d>0]
array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])
Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])
Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
11
Exercise 8 - Print out the shape of d.
d.shape
(3, 6)
Exercise 9 - Transpose and then print out the shape of d.
d.transpose().shape
(6, 3)
Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9,2))
array([[ 90,  30],
       [ 45,   0],
       [120, 180],
       [ 45, -90],
       [-30, 270],
       [ 90,   0],
       [ 60,  45],
       [-45,  90],
       [-45, 180]])
