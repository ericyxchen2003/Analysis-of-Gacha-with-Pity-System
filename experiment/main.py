import numpy as np
from experiment_function import conduct_experiment
import time

'''
Parameters:
    prob - the initial probability to obtain a grand prize for each pull
    N - the guarantee
    n - # of trials conduct
'''

prob = 0.006
N = 90
n = 10000

tic = time.time()
d = conduct_experiment(prob, N, n)
toc = time.time()

print("=========Experiment=========")
print("Probability of each pull = " + str(prob*100) + "%")
print("Guarantee = " + str(N))
print("# of trials = " + str(n))
print("It takes on average " + str(d['ET']) + " pulls to obtain a grand prize.")
print("It takes on average " + str(d['ETstar']) + " pulls to obtain the featured prize.")
print("Runtime: " + str((toc-tic)) + "s")