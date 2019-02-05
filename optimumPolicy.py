# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------
from pprint import pprint
import numpy as np

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    # I think the logic shall be from higher density going towards lower density.

    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    tree = {}

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    # print("before")
                    # pprint(value)
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and \
                                grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                tree[(x, y)] = (x2, y2)
                    # print('after')
                    # pprint(value)

    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    policy[goal[0]][goal[1]] = '*'
    # print(tree)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            # get rid of obstacles
            if value[x][y] != 99 and [x, y] != goal:
                _ = np.subtract(tree[(x, y)], (x, y))
                # print(_.tolist())
                policy[x][y] = delta_name[delta.index(list(np.subtract(tree[(x, y)], (x, y))))]

    # return policy
    return policy

pprint(optimum_policy(grid, goal, cost))