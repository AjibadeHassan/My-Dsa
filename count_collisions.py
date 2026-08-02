class Solution:

    def countCollisions(self, directions):
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")
        return directions.count("R") + directions.count("L")
