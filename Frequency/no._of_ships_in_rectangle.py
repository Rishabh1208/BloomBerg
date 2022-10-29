
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """


# Optimize time complexity from O(mn) [Before I started coding].
# Base of the logarithmic time complexity of the code.
# If call is made 1million times, what changes in the existing algorithm must be implemented to 
# accomodate this?

# TC: O(log2max(m,n)). S 
# SC: O(log2max(m,n))
class Sea(object):
    def hasShips(self, topRight, bottomLeft):
        pass


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
    # If the current rectangle does not contain any ships, return 0.
    if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y):
        return 0
    if not sea.hasShips(topRight, bottomLeft):
        return 0

    # If the rectangle represents a single point, a ship is located.
    if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
        return 1

    # Recursively check each of the 4 sub-rectangles for ships.
    mid_x = (topRight.x + bottomLeft.x) // 2
    mid_y = (topRight.y + bottomLeft.y) // 2
    res = self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1)) + self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + self.countShips(sea, Point(topRight.x, mid_y),
                                                                                                                                                                                                                                 Point(mid_x + 1, bottomLeft.y))
    return res
