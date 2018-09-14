from matplotlib import pyplot as plt 
import numpy as np 

import argparse

parser = argparse.ArgumentParser(description= "binomial random variable plot")

parser.add_argument("--p",type = float,required = True , help = "Input the probability of getting heads")
args = parser.parse_args()

p = args.p
n = 100 ## number of coin tosses
x = np.arange(n+1)
y = []

def factorial(n):
    """
    Computes factorial of n
    """
    return(np.math.factorial(n))

def NCK(n,k):
    """
    Computes n c k 
    """
    return(factorial(n)/(factorial(k)*factorial(n-k)))

for i in range(len(x)):
    y.append(NCK(n,x[i])*(np.power(p,x[i]))*(np.power((1-p),n-x[i])))

plt.bar(x,y)
plt.xlabel("k")
plt.ylabel("Corresponding probability")
plt.title("Binomial random variable plot with p = {} \n Note it has a maximum at {} fraction of n".format(p,((np.argmax(y)+1)/len(y))))
plt.show()
