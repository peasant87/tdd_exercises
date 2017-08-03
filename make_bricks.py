'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks.
font: http://codingbat.com/prob/p118406
'''

def make_bricks(small, big, goal):
    big_size = 5
    big_times = int(goal / big_size)
    if big_times <= big:
        goal = goal - (big_times * big_size)
    else:
        goal = goal - (big * big_size)
    if goal <= small:
        return True
    else:
        return False

assert make_bricks(1000000, 1000, 1000100) == True
assert make_bricks(2, 1000000, 100003) == False
assert make_bricks(3, 1 ,8) == True
assert make_bricks(3, 1 ,9) == False
assert make_bricks(3, 2 ,10) == True
assert make_bricks(3, 2, 9) == False
assert make_bricks(1, 4, 12) == False
assert make_bricks(3, 2, 8) == True

assert make_bricks(3, 1, 8) == True
assert make_bricks(3, 1, 9) == False
assert make_bricks(3, 2, 10) == True
assert make_bricks(3, 2, 8) == True
assert make_bricks(3, 2, 9) == False
assert make_bricks(6, 1, 11) == True
assert make_bricks(6, 0, 11) == False
assert make_bricks(1, 4, 11) == True
assert make_bricks(0, 3, 10) == True
assert make_bricks(1, 4, 12) == False
assert make_bricks(3, 1, 7) == True
assert make_bricks(1, 1, 7) == False
assert make_bricks(2, 1, 7) == True
assert make_bricks(7, 1, 11) == True
assert make_bricks(7, 1, 8) == True
assert make_bricks(7, 1, 13) == False
assert make_bricks(43, 1, 46) == True
assert make_bricks(40, 1, 46) == False
assert make_bricks(40, 2, 47) == True
assert make_bricks(40, 2, 50) == True
assert make_bricks(40, 2, 52) == False
assert make_bricks(22, 2, 33) == False
assert make_bricks(0, 2, 10) == True
assert make_bricks(1000000, 1000, 1000100) == True
assert make_bricks(2, 1000000, 100003) == False
assert make_bricks(20, 0, 19) == True
assert make_bricks(20, 0, 21) == False
assert make_bricks(20, 4, 51) == False
assert make_bricks(20, 4, 39) == True