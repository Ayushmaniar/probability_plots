from matplotlib import pyplot as plt 
import numpy as np 

import argparse

parser = argparse.ArgumentParser(description= "binomial random variable plot")

parser.add_argument("--lmda",type = float,required = True , help = "The parameter lambda")
parser.add_argument("--n",type = float,default = 100.0 , help = "The extent till which you want to display")
args = parser.parse_args()

lmda = args.lmda

n = args.n ## number of coin tosses
x = np.linspace(0,n+1,500)
y = []

for i in range(len(x)):
    y.append(lmda*np.exp(-(lmda*x[i])))

# print("The sum of all the probabilities is {}".format(np.sum(y)))
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("Corresponding probability")
plt.title("Exponential random variable plot with lamda = {}".format(lmda))
plt.show()