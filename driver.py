# Jason Sy
# CSS 340: Applied Algorithmics
# 5/11/2022
# Driver for greedyrobot

import sys

if __name__ == '__main__':
    from greedyrobot import GreedyRobot
    #allows for input on command line e.g. C:\users\n>python driver.py 1 2 3 5
    if len(sys.argv) == 5:
        x1 = int(sys.argv[1])
        y1 = int(sys.argv[2])
        x2 = int(sys.argv[3])
        y2 = int(sys.argv[4])
    #if no inputs are given on the side of the command line
    else:
        print("Four arguments were not given")
        print()
        x1 = eval(input("Input the argument for x position of the robot (x1): "))
        y1 = eval(input("Input the argument for y position of the robot (y1): "))
        x2 = eval(input("Input the argument for x position of the treasure (x2): "))
        y2 = eval(input("Input the argument for y position of the treasure (y2): "))

    pathway = ""
    print("(", x1, ",", y1, ")", "-> ", "(", x2, ",", y2, ")")

    
    print()
    position = GreedyRobot.findPath(x1, y1, x2, y2, pathway)
    

    print("Number of paths: ", position)
