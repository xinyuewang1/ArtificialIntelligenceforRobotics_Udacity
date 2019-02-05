# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.
# import optimumPolicy
from pprint import pprint
import math

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]
#       R, -, L
cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    #     A* first...?
    # init = [4, 3, 0]  # given in the form [row,col,direction]
    # Goal: from init to goal, find best movement each step???
    # 3 dimension grid, x, y, heading
    value = [[[math.inf for row in range(len(grid[0]))] for col in range(len(grid))]
             for i in range(len(forward))]
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    # value: orient, x, y
    x, y, o = init
    value[0][x][y] = 0
    path = [[value[0][x][y], o, x, y]]
    # 不能单纯考虑某个位置， 而必须考虑整条线路的成本
    # every possibility shall be considered as a new route and calculate the overall
    # cost.
    while [x, y] != goal and path:
    #     possible move: R, #, L
    #     pprint(value)
    #     print(next)
    #     next.sort(reverse=True)
        c, o, x, y = path.pop()
        for orient in range(len(value)):
            # orient shall only be neighbor orientation
            # e.g. 0 have 3 and 1
            poss = 0
            if orient != (o + 2) % 4:  # only orient next/equal to current one
                poss += 1
                x2 = x + forward[orient][0]
                y2 = y + forward[orient][1]
                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] != 1:
                    act = (orient - o) % 4
                    if (orient - o) % 4 == 3:
                        act = -1
                    a = action.index(act)
                    # print(a)
                    fromThisNeighbor = value[o][x][y] + cost[a]
                    # next.append([fromThisNeighbor, orient, x2, y2])
                    if value[orient][x2][y2] > fromThisNeighbor:
                        value[orient][x2][y2] = fromThisNeighbor
                        path.append([fromThisNeighbor, orient, x2, y2])
                        policy2D[x][y] = action_name[a]

    policy2D[goal[0]][goal[1]] = '*'

    return policy2D


pprint(optimum_policy2D(grid, init, goal, cost))