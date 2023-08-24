# Jason Sy
# CSS 340: Applied Algorithmics
# 5/11/2022
# GreedyRobot class to locate number of paths to treasure

class GreedyRobot():
    #Constructor for points
    def __int__(self, x1, y1, x2, y2, pathway):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._pathway = pathway

    # Getters for points
    def get_x1(self):
        return self._x1

    def get_y1(self):
        return self._y1

    def get_x2(self):
        return self._x2

    def get_y2(self):
        return self._y2
    
    def get_pathway(self):
        return self._pathway

    # Setter for points
    def set_path(self, x1, y1, x2, y2, pathway):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._pathway = pathway

    #finds all path
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

