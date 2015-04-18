# Program that estimates the average number of stones required so that 2 stones
# become adjascent in an nxn goban. I want to plot the distribution of number
# of stones vs numbers of trial, i.e. an histogram.
import random
import numpy as np
import matplotlib.pyplot as plt

# Size of the board
n = 19

# Number of trials
trials = 10000
# Initialize the board list of lists to 0. 0 means no stone, 1 means stone.
# Note that board[0][0] is the first element and board[20][20] is the last one
# , for when n=19. That's because I define the board
# as n+2 x n+2 for the edges...
board = [[0]*(n+2) for i in range(n+2)]
counter = 0
# Generate random coordinates inside of the 19x19 board
x_coordinates, y_coordinates = random.randint(1, n), random.randint(1, n)

# Now define a boolean function that I'll use as a condition in a while loop


def check_if_stones(x_coordinates, y_coordinates):
    if (board[x_coordinates-1][y_coordinates] == 1
    or board[x_coordinates][y_coordinates-1] == 1
    or board[x_coordinates+1][y_coordinates] == 1
    or board[x_coordinates][y_coordinates+1] == 1):
        return False
    else:
        return True

trial_list = []
for j in range(trials):
    counter = 0
    board = [[0]*(n+2) for i in range(n+2)]
    while check_if_stones(x_coordinates, y_coordinates):
        if board[x_coordinates][y_coordinates] == 0:
            # Now replace a random element by 1
            board[x_coordinates][y_coordinates] = 1
            counter += 1
            x_coordinates, y_coordinates = random.randint(1, n), random.randint(1, n)
        x_coordinates, y_coordinates = random.randint(1, n), random.randint(1, n)
    # Update the counter when the boolean function returns false. Do this outside of the while loop.
    counter += 1
    trial_list.append(counter)
    x_coordinates, y_coordinates = random.randint(1, n), random.randint(1, n)
print('The average number of stones is', np.mean(trial_list))

# print(trial_list)
plt.xlabel('number of stones until 2 are adjascent')
plt.ylabel('occurrency')
plt.grid(True)
plt.hist(trial_list, 40)
plt.show()
print(trial_list)
