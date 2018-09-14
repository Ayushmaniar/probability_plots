from matplotlib import pyplot as plt 
import numpy as np 

import argparse

parser = argparse.ArgumentParser(description= "binomial random variable plot")

parser.add_argument("--p",type = float,required = True , help = "Input the probability of getting heads")
parser.add_argument("--n",type = float,required = True , help = "The first time you get heads")
args = parser.parse_args()

p = args.p
n = args.n ## number of coin tosses
x = np.arange(n+1)
y = []

for i in range(len(x)):
    y.append(np.power(1-p,x[i]-1)*p)


print("The sum of all the probabilities is {}".format(np.sum(y)))
plt.bar(x+1,y)
plt.xlabel("n ( The first time you get an heads)")
plt.ylabel("Probability of X = n where X is # tosses required for heads first time")
plt.title("Geometric random variable plot with p = {} ".format(p))
plt.show()
