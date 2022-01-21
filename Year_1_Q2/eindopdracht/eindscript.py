#!/usr/bin/env python3

"""
A script for rendering an animation of the NMDA molecule.
Note: pypovray and it's dependencies have to be installed.
Instructions at:
https://nbviewer.org/urls/bitbucket.org/mkempenaar/pypovray/raw/master/manual/install_and_configure.ipynb

This script has to be located in the folder of the cloned git repository.
"""


__author__ = 'SL de Haan'
__version__ = '0.0.1'


from pypovray import pypovray, pdb, models, SETTINGS, load_config
from vapory import Scene, LightSource, Camera, Pigment, Finish, Interior, Sphere, Cylinder


def static_objects():
    """
    Function for environmental static objects.
    Param : None
    Returns: List
    """

    # Middle NMDA receptor
    N2A = Cylinder([-2, -3, 2], [-2, 3, 2], 1.2, Pigment('color', [1, 0, 1]))
    N2B = Cylinder([2, -3, 2], [2, 3, 2], 1.2, Pigment('color', [1, 0, 1]))
    N1_1 = Cylinder([-2, -3, -2], [-2, 3, -2], 1.2, Pigment('color', [1, 0, 1]))
    N1_2 = Cylinder([2, -3, -2], [2, 3, -2], 1.2, Pigment('color', [1, 0, 1]))

    # Right NMDA receptor
    N2A_R = Cylinder([14, -3, 2], [14, 3, 2], 1.2, Pigment('color', [1, 0, 1]))
    N2B_R = Cylinder([18, -3, 2], [18, 3, 2], 1.2, Pigment('color', [1, 0, 1]))
    N1_1_R = Cylinder([14, -3, -2], [14, 3, -2], 1.2, Pigment('color', [1, 0, 1]))
    N1_2_R = Cylinder([18, -3, -2], [18, 3, -2], 1.2, Pigment('color', [1, 0, 1]))
    sphere_R = Sphere([16, 0, 0], 1, Pigment('color', [255, 255, 204]), Finish('phong', 0.8))

    # Left NMDA receptor
    N2A_L = Cylinder([-14, -3, 2], [-14, 3, 2], 1.2, Pigment('color', [1, 0, 1]))
    N2B_L = Cylinder([-18, -3, 2], [-18, 3, 2], 1.2, Pigment('color', [1, 0, 1]))
    N1_1_L = Cylinder([-14, -3, -2], [-14, 3, -2], 1.2, Pigment('color', [1, 0, 1]))
    N1_2_L = Cylinder([-18, -3, -2], [-18, 3, -2], 1.2, Pigment('color', [1, 0, 1]))
    sphere_L = Sphere([-16, 0, 0], 1, Pigment('color', [255, 255, 204]), Finish('phong', 0.8))

    # To the right of the NMDA receptor
    cell_wall_1 = Sphere([3.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_2 = Sphere([4.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_3 = Sphere([5.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_4 = Sphere([6.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_5 = Sphere([7.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_6 = Sphere([8.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_7 = Sphere([9.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_8 = Sphere([10.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_9 = Sphere([11.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_10 = Sphere([12.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_11 = Sphere([13.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))

    # Right right
    cell_wall_12 = Sphere([19.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_13 = Sphere([20.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_14 = Sphere([21.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_15 = Sphere([22.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_16 = Sphere([23.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_17 = Sphere([24.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_18 = Sphere([25.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_19 = Sphere([26.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))

    # To the left of the NMDA receptor
    cell_wall_20 = Sphere([-3.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_21 = Sphere([-4.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_22 = Sphere([-5.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_23 = Sphere([-6.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_24 = Sphere([-7.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_25 = Sphere([-8.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_26 = Sphere([-9.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_27 = Sphere([-10.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_28 = Sphere([-11.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_29 = Sphere([-12.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_30 = Sphere([-13.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))


    # Left left
    cell_wall_31 = Sphere([-19.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_32 = Sphere([-20.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_33 = Sphere([-21.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_34 = Sphere([-22.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_35 = Sphere([-23.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_36 = Sphere([-24.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_37 = Sphere([-25.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))
    cell_wall_38 = Sphere([-26.4, 0, 0], 1, Pigment('color', [1, 0, 0]), Finish('phong', 0.8))

    NMDA = [N2A, N2B, N1_1, N1_2, cell_wall_1, cell_wall_2, cell_wall_3, cell_wall_4, cell_wall_5, cell_wall_6, cell_wall_7, cell_wall_8, cell_wall_9, cell_wall_10, cell_wall_11, cell_wall_20, cell_wall_21, cell_wall_22, cell_wall_23, cell_wall_24, cell_wall_25, cell_wall_26, cell_wall_27, cell_wall_28, cell_wall_29, cell_wall_30, N2A_R, N2B_R, N1_1_R, N1_2_R, sphere_R, N2A_L, N2B_L, N1_1_L, N1_2_L, sphere_L, cell_wall_12, cell_wall_13, cell_wall_14, cell_wall_15, cell_wall_16, cell_wall_17, cell_wall_18, cell_wall_19, cell_wall_31, cell_wall_32, cell_wall_33, cell_wall_34, cell_wall_35, cell_wall_36, cell_wall_37, cell_wall_38]

    return NMDA



def frame(step):
    """
    frame combines all static and moving objects
    and adds camera and light to it.
    : param : Int
    : returns : Scene
    """

    # Setting up variables for framecount to adjust the animation for different framecounts.
    frame_count = eval(SETTINGS.NumberFrames)
    step_size = 15 / (frame_count/3)
    frame_part = frame_count/3    



    if step < frame_part: # 0 to 1/3 part of the animation.
        ATP = pdb.PDBMolecule("/homes/sldehaan/doc/ultrapov/pypovray/pdb/glutamate.pdb", offset=[-5, 18-(step*step_size), 0])
        sphere_1 = Sphere([0, 0, 0], 1, Pigment('color', [255, 255, 204]), Finish('phong', 0.8))
        object_list = [sphere_1]
    elif step < frame_part*2: # 1/3 to 2/3 part of the animation.
        ATP = pdb.PDBMolecule("/homes/sldehaan/doc/ultrapov/pypovray/pdb/glutamate.pdb", offset=[-5, 3, 0])
        sphere_1 = Sphere([0, 0.2*(step-frame_part), 0], 1, Pigment('color', [255, 255, 204]), Finish('phong', 0.8))
        object_list = [sphere_1]
    else: # 2/3 to 3/3 part of the animation.
        ATP = pdb.PDBMolecule("/homes/sldehaan/doc/ultrapov/pypovray/pdb/glutamate.pdb", offset=[-5, 3, 0])
        sphere_1 = Sphere([0, (-0.3*(step-(frame_part*2)))+20, 1], 0.7, Pigment('color', [0, 100, 0]), Finish('phong', 0.8)) # Representing Calcium
        sphere_2 = Sphere([0, (-0.3*(step-(frame_part*2)))+25, 1], 0.7, Pigment('color', [2, 1, 0]), Finish('phong', 0.8)) # Representing Sodium
        sphere_3 = Sphere([0, (-0.3*(step-(frame_part*2)))+30, 1], 0.7, Pigment('color', [0, 100, 0]), Finish('phong', 0.8)) # Representing Calcium
        sphere_4 = Sphere([0, (-0.3*(step-(frame_part*2)))+35, 1], 0.7, Pigment('color', [2, 1, 0]), Finish('phong', 0.8)) # Representing Sodium
        sphere_5 = Sphere([0, (-0.3*(step-(frame_part*2)))+40, 1], 0.7, Pigment('color', [0, 100, 0]), Finish('phong', 0.8)) # Representing Calcium
        sphere_6 = Sphere([0, (0.3*(step-(frame_part*2)))-22, -1], 0.7, Pigment('color', [128, 0, 128]), Finish('phong', 0.8)) # Representing Potassium in Purple
        object_list = [sphere_1, sphere_2, sphere_3, sphere_4, sphere_5, sphere_6]

    # Importing static objects
    NMDA = static_objects()

    # Camera moving on the Y-axis with step_size depending on the amount of frames you have in default.ini
    camera = Camera('location', [0, (step*step_size)*0.7, -20], 'look_at', [0, 0, 0])

    # Lights to light up the scene
    light_middle = LightSource([0, 0, -50], 1.2)
    light_left = LightSource([-100, 50, 30], 1.2)
    light_right = LightSource([100,50, 30], 1.2)

    return Scene(camera, objects=[light_middle, light_left, light_right] + object_list + NMDA + ATP.povray_molecule) 


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame)
