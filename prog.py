#!/bin/python3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from loadData import loadFloatData
from vec2Dto3D import convertTo3D

left = loadFloatData('imageA.dat')
right = loadFloatData('imageB.dat')

# 400 pixels == 3.66 blender units
# 399 pixels == 3.648 blender units
conv = 3.66 / 400 # scale factor

# convert pixel units to blender units
for i in range(0, len(left), 2):
    left[i] = (left[i]-400)*conv
    left[i+1] = (left[i+1]-300)*conv

for i in range(0, len(right), 2):
    right[i] = (right[i]-400)*conv
    right[i+1] = (right[i+1]-300)*conv

# account camera movement
for i in range(0, len(right), 2):
    right[i] -= 0.1 # distance from left to right camera


# convert to 3D
x1, y1, z1, x2, y2, z2 = convertTo3D(left[8], left[9], left[10], left[11], right[12], right[13], right[14], right[15])

print("Coordinates from blender model (y is upside-down): x:%.3f y:%.3f z:%.3f" % (0.402, -0.981, -1.987))
print("Vector: x1:%.3f y1:%.3f z1:%.3f  x2:%.3f y2:%.3f z2:%.3f" % (x1, y1, z1, x2, y2, z2))


# create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# left image
for i in range(0, len(left), 4):
    ax.plot3D([left[i+0], left[i+2]], [left[i+1], left[i+3]], [0, 0], color='red', linewidth=0.5)

# right image
for i in range(0, len(right), 4):
    ax.plot3D([right[i+0], right[i+2]], [right[i+1], right[i+3]], [0, 0], color='cyan', linewidth=0.5)

# NOTE: vector used
ax.plot3D([left[8], left[10]], [left[9], left[11]], [0, 0], color='black')

ax.view_init(elev=-90, azim=-90)
ax.dist = 5.5

# add labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

