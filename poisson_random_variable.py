from matplotlib import pyplot as plt 
import numpy as np 

import argparse

parser = argparse.ArgumentParser(description= "binomial random variable plot")

parser.add_argument("--lmda",type = float,required = True , help = "Input the probability of getting heads")
parser.add_argument("--n",type = float,required = True , help = "The first time you get heads")
args = parser.parse_args()


lmda = args.lmda

n = args.n ## number of coin tosses
x = np.arange(n+1)
y = []

def factorial(n):
    """
    Computes factorial of n
    """
    return(np.math.factorial(n))

for i in range(len(x)):
    y.append((np.exp(-lmda)*np.power(lmda,x[i])/(factorial(x[i]))))

print("The sum of all the probabilities is {}".format(np.sum(y)))
plt.bar(x,y)
plt.xlabel("k")
plt.ylabel("Corresponding probability")
plt.title("Poisson random variable plot with lamda = {}".format(lmda))
plt.show()