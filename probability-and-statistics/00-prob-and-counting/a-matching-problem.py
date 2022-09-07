import numpy as np

if __name__ == "__main__":
    n = 100
    trials = 100000
    success = 0
    for trial in range(trials):
        r = np.random.random_integers(1, n, trials) == np.arange(trials)
        success += np.sum(r) >= 1
    p = success / trials
    print("Matching probability:", p, "(with size", trial, ")")
    print("1 - 1/e =", round(1 - (1 / np.exp(1)), 4))