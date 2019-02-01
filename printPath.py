# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------
from pprint import pprint

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    # logic: dijkstra? going backward? shortest path to each position?
    # start with end, backward to find start. This is because the g2 marked the shortest path.
    # I imagine it's a tree-like structure.

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    # a whole 0 matrix? what about the obstacles?
    closed[init[0]][init[1]] = 1
    # close the (0, 0)

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    tree = {}
    dis = None

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
                dis = g
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            # if it's not visited, not an obstacle
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = g2
                            if g2 in tree:
                                tree[g2].append((x2, y2))
                            else:
                                tree[g2] = [(x2, y2)]
                            # interesting, using a matrix to mark visited instead of set or list I was using.
                            # this will make put unvisited into -1 so much easier.

    pat = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    pat[goal[0]][goal[1]] = '*'
    curX, curY = tree[g][0]
    for i in range(g - 1, 0, -1):
        for x, y in tree[i]:
            # delta_name = ['^', '<', 'v', '>']
            if abs(curX - x) + abs(curY - y) == 1:  # gap can only be one
                pat[x][y] = delta_name[delta.index([curX - x, curY - y])]
                curX, curY = x, y

    pat[init[0]][init[1]] = delta_name[delta.index([curX - init[0], curY - init[1]])]

    return pat  # make sure you return the shortest path


pprint(search(grid, init, goal, cost))
