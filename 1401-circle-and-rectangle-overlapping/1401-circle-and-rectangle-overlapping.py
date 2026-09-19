class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Closest x-coordinate in the rectangle
        closestX = max(x1, min(xCenter, x2))

        # Closest y-coordinate in the rectangle
        closestY = max(y1, min(yCenter, y2))

        # Distance squared
        dx = closestX - xCenter
        dy = closestY - yCenter

        return dx * dx + dy * dy <= radius * radius