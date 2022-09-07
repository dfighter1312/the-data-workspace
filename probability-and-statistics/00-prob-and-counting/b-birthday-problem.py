import numpy as np

if __name__ == "__main__":
    # Number of people
    k = 23
    trials = 100000
    success = 0

    for trial in range(trials):
        b = np.random.randint(1, 366, size=k)
        # Find number of unique dates, if it is less than k
        # then there are 1 pair of people have the same birthday
        unique = np.unique(b)
        pair_exists = unique.size < b.size
        if pair_exists:
            success += 1
    p = success / trials
    print("Matched probability:", p)
    print("Theoretical computation:", round(1 - (np.math.factorial(365) / (np.math.factorial(365 - k) * (365 ** k))), 4))

