import numpy as np
from experiment_function import conduct_experiment

prob = 0.006
N = 90
n = 10000

d = conduct_experiment(prob, N, n)
print("=========Experiment=========")
print("Probability of each pull = " + str(prob*100) + "%")
print("The Guaranteed Pull: " + str(N))
print("# of trials = " + str(n))
print("It takes on average " + str(d['ET']) + " pulls to obtain a grand prize.")
print("It takes on average " + str(d['ETstar']) + " pulls to obtain a featured prize.")