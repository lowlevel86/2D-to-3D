
def getZ(x1, x2):
    zDist = 8.0 # distance from camera to "z = 0"
    xDist = 0.1 # distance from left to right camera
    
    para = x2 - x1 # parallax
    persp = xDist / (para + xDist) # perspective projection
    
    return (persp - 1) * zDist # return z coordinate


def adjustLineToY(x1, y1, x2, y2, y):
    return x1 - (y1 - y) / (y1 - y2) * (x1 - x2)


def convertTo3D(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):

    if By1 == By2:
        z1 = getZ(Ax1, Bx1)
        z2 = getZ(Ax2, Bx2)
    else:
        # contract or extend line until By1 is equal to Ay1 and return Bx1
        Bx1_new = adjustLineToY(Bx1, By1, Bx2, By2, Ay1)
    
        # contract or extend line until By2 is equal to Ay2 and return Bx2
        Bx2_new = adjustLineToY(Bx1, By1, Bx2, By2, Ay2)
        
        z1 = getZ(Ax1, Bx1_new)
        z2 = getZ(Ax2, Bx2_new)
    
    # undo the perspective projection
    zDist = 8.0
    x1 = (z1 / zDist + 1) * Ax1
    y1 = (z1 / zDist + 1) * Ay1
    x2 = (z2 / zDist + 1) * Ax2
    y2 = (z2 / zDist + 1) * Ay2
    
    return [x1, y1, z1, x2, y2, z2]

