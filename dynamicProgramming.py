# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
from pprint import pprint

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    # this is similar to my original idea, retrieve from goal.
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[goal[0]][goal[1]] = 1

    value = [[99 for y in range(len(grid[0]))] for x in range(len(grid))]
    # initial with an empty grid

    total = len(grid) * len(grid[0])
    x, y = goal
    step = 0
    neighbor = [[step, x, y]]
    visitNum = 0
    through, resign = False, False

    while not through and not resign:
        # print(value)
        if not neighbor:
            resign = True
            return value
        else:
            # print(neighbor)
            neighbor = sorted(neighbor, reverse=True)
            step, x, y = neighbor.pop()
            # print(step)
            value[x][y] = step
            step += cost
            visitNum += 1

            if visitNum == total:
                through = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if grid[x2][y2] == 0 and closed[x2][y2] == 0:
                        # if grid[x2][y2] == 0 and value[x2][y2] == 99:
                        #     print(step)
                        #     step2 = step + cost
                            neighbor.append([step, x2, y2])
                            closed[x2][y2] = 1

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value


pprint(compute_value(grid, goal, cost))