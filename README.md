# 3D-object-viewer
Can view any 3d .obj file in 3d with controls to rotate and transform position.

Requirements:
  Python 3.10 or above
  Numpy 1.14 or above (for multidimensional arrays)
  Pygame 2.4.0 or above (for graphics)
  Numba (for faster calculations)

Initialization:
  In the main.py, change the string "file" to the location of your .obj file.
  There are some pre-working .obj files in "3Dobjects" folder.

Controls:
Arrow keys UP and DOWN: rotate along x-axis
Arrow keys LEFT and RIGHT: rotate along y-axis
W and S keys: zoom in and out
A and D keys: change relative position of camera left and right
Q and E keys: change relative position of camera up and down

Warnings:
.obj files of objects that have multiple edged faces (for example: including both triangles and squares) can't run on numpy version greater than 1.14. 
