# Jason Sy
# CSS 340: Applied Algorithmics
# 5/11/2022
# GreedyRobot class to locate number of paths to treasure

class GreedyRobot():

    def findPath(x1, y1, x2, y2, pathway):
        totalPaths = 0
        if (x1 == x2 and y1 == y2): # destination reached
            print(pathway)
            totalPaths += 1
            return totalPaths


        if(y1 < y2):
            paths = GreedyRobot.findPath(x1, y1 + 1, x2, y2, pathway + "N")
            totalPaths += paths #moving north

        elif(y1 > y2):
            paths = GreedyRobot.findPath(x1, y1 - 1, x2, y2, pathway + "S")
            totalPaths += paths #moving south

        if(x1 < x2):
            paths = GreedyRobot.findPath(x1 + 1, y1, x2, y2, pathway + "E")
            totalPaths += paths #moving east

        elif(x1 > x2):
            paths = GreedyRobot.findPath(x1 - 1, y1, x2, y2, pathway + "W")
            totalPaths += paths #moving west


        return totalPaths # return total paths






#Temporary Driver
if __name__ == '__main__':
    x1 = eval(input("Input x position of the robot: "))
    y1 = eval(input("Input y position of the robot: "))
    x2 = eval(input("Input x position of the treasure: "))
    y2 = eval(input("Input y position of the treasure: "))

    pathway = ""

    print("(", x1, ",", y1, ")", "-> ", "(", x2, ",", y2, ")")
    print()

    totalPaths = GreedyRobot.findPath(x1, y1, x2, y2, pathway)

    print("Number of paths: ", totalPaths)