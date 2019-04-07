'''
Gambler's problem.  The gambler has a stake s between 0 and 100.  At each 
play he wagers an integer <= s.  He wins that much with prob p, else he
loses that much.  If he builds his stake to 100 he wins (thus he never 
wagers more than (- 100 s)); if his stake falls to 0 he loses.
'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(seed=42)

p_H = 0.4  # Probability of landing heads
num_states = 100  # Number of states, ie goal to be reached.
values = np.zeros(shape=(num_states+1), dtype=np.float32)  # For storing the value function outputs for each state.
policy = np.zeros(shape=(num_states+1), dtype=np.float32)  # For storing the amount to be bet for each state.

reward = np.zeros(shape=(num_states+1), dtype=np.float32)  # Stores the individual reward for each state.
reward[100] = 1

theta = 0.000001  # Tolerance
gamma = 0.99 # Discount factor

def valueIteration():
    while True:
        delta = 0
        for s in range(num_states):
            v = values[s]

            # Applying the Bellman Equation...
            maximum_value = 0
            for bet in range(0, s+1):
                win_amount = min(s + bet, 100)  # To prevent out of bounds error, when the winning amount exceeds 100.
                lose_amount = s - bet
                average = p_H * (reward[win_amount] + gamma * values[win_amount]) + \
                          (1-p_H) * (reward[lose_amount] + gamma * values[lose_amount])

                if average > maximum_value:
                    policy[s] = bet
                    maximum_value = average
                    values[s] = average

            diff = np.abs(v - values[s])
            delta = max(delta, diff)
        if delta < theta:
            break

def plotPolicy():
    x = np.array(range(0, num_states+1))
    y = policy
    plt.xlabel("Amount available (Current State)")
    plt.ylabel('Recommended betting amount')
    plt.title("Optimal policy for Gambler's problem (goal:${} and win probability={})".format(num_states, p_H))
    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    valueIteration()
    plotPolicy()