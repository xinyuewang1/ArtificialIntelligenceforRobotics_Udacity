# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up


def sense(p, colors, measure, sensor_right):
    q = []
    for x in range(len(p)):
        q.append([])
        for y in range(len(p[0])):
            hit = (measure == colors[x][y])
            q[x].append(p[x][y] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
    s = sum(map(sum, q))
    # print(q)
    for x in range(len(q)):
        for y in range(len(q[0])):
            if q[x][y] != 0:
                q[x][y] /= s
    return q


def move(p, motion, p_move):
    q = []
    for x in range(len(p)):
        q.append([])
        for y in range(len(p[0])):
            s = p_move * p[(x-motion[0]) % len(p)][(y-motion[1]) % len(p[0])]
            # if motion[0] == 0 and motion[1] == 0:
                
            if motion[0] == 0 and motion[1] != 0:  # x isn't moving, but y is
                s += (1 - p_move) * p[(x-motion[0]) % len(p)][y % len(p[0])]
            elif motion[0] != 0 and motion[1] == 0:
                s += (1 - p_move) * p[x % len(p)][(y-motion[1]) % len(p[0])]

            q[x].append(s)
    return q


def localize(colors, measurements, motions, sensor_right, p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    # >>> Insert your code here <<<
    # move, sense
    for i in range(len(motions)):
        p = move(p, motions[i], p_move)
        # print(p)
        p = sense(p, colors, measurements[i], sensor_right)

    return p


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print ('[' + ',\n '.join(rows) + ']')


# test 1
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'G'],
#           ['G', 'G', 'G']]
# measurements = ['R']
# motions = [[0, 0]]
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors, measurements, motions, sensor_right, p_move)
# show(p)
# correct_answer = (
#     [[0.0, 0.0, 0.0],
#      [0.0, 1.0, 0.0],
#      [0.0, 0.0, 0.0]])


# test 2
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R']
# motions = [[0,0]]
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# show(p)
# correct_answer = (
#     [[0.0, 0.0, 0.0],
#      [0.0, 0.5, 0.5],
#      [0.0, 0.0, 0.0]])


# test 3
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R']
# motions = [[0,0]]
# sensor_right = 0.8
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# show(p)
# correct_answer = (
#     [[0.06666666666, 0.06666666666, 0.06666666666],
#      [0.06666666666, 0.26666666666, 0.26666666666],
#      [0.06666666666, 0.06666666666, 0.06666666666]])


# test 4
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 0.8
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# show(p)
# correct_answer = (
#     [[0.03333333333, 0.03333333333, 0.03333333333],
#      [0.13333333333, 0.13333333333, 0.53333333333],
#      [0.03333333333, 0.03333333333, 0.03333333333]])


# test 5
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 1.0
# p_move = 1.0
# p = localize(colors,measurements,motions,sensor_right,p_move)
# show(p)
# correct_answer = (
#     [[0.0, 0.0, 0.0],
#      [0.0, 0.0, 1.0],
#      [0.0, 0.0, 0.0]])

# test 6
# colors = [['G', 'G', 'G'],
#           ['G', 'R', 'R'],
#           ['G', 'G', 'G']]
# measurements = ['R', 'R']
# motions = [[0,0], [0,1]]
# sensor_right = 0.8
# p_move = 0.5
# p = localize(colors,measurements,motions,sensor_right,p_move)
# show(p)
# # print(sum(map(sum,p)))
# correct_answer = (
#     [[0.0289855072, 0.0289855072, 0.0289855072],
#      [0.0724637681, 0.2898550724, 0.4637681159],
#      [0.0289855072, 0.0289855072, 0.0289855072]])




#############################################################
# For the following test case, your output should be
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R', 'G', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'G', 'R'],
          ['R', 'R', 'R', 'R', 'R']]
measurements = ['G', 'G', 'G', 'G', 'G']
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
p = localize(colors, measurements, motions, sensor_right=0.7, p_move=0.8)
show(p)  # displays your answer
