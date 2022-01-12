#!/usr/bin/env python3

"""
Script for rendering ATP molecule splitting a phosphate.
Note: pypovray and it's dependencies have to be installed.
Instructions at:
https://nbviewer.org/urls/bitbucket.org/mkempenaar/pypovray/raw/master/manual/install_and_configure.ipynb

This script has to be located in the folder of the cloned git repository.
"""


__author__ = 'SL de Haan'
__version__ = '0.0.1'


from vapory import Scene, LightSource, Camera, Pigment, Finish, Interior
from pypovray import pypovray, pdb, SETTINGS, models
from math import pi

def frame(step):
    """
    Frame of molecule ATP
    param : int ->  step
    returns : tuple -> scene
    """

    camera = Camera('location', [0, 10, -35], 'look_at', [0, 0, 0])
    ATP = pdb.PDBMolecule('{}/pdb/atp.pdb'.format(SETTINGS.AppLocation), center=True)

    frames = eval(SETTINGS.NumberFrames)

    if step < (frames / 4):
       ATP_divide = ATP.divide([1], 'water', offset=[0, 0, 0])
    else:
        ATP_divide = ATP.divide([12, 13, 14, 15, 16], 'phosphate', offset=[0, ((step - (frames / 4)) * 0.1), 0])
        ATP_divide.rotate([0, 1, 0], 0.2* (step - (frames / 4)))

    light_middle = LightSource([0, 0, -50], 1.2)
    light_left = LightSource([-100, 50, 30], 1.2)
    light_right = LightSource([100,50, 30], 1.2)


    # One rotation for the ATP molecule in the animation.
    stepsize = (2*pi) / frames

    # Rotate ATP 2pi
    ATP.rotate([1, 0, 0], stepsize*step)


    return Scene(camera, objects=[light_middle, light_left, light_right] 
            + ATP.povray_molecule + ATP_divide.povray_molecule) 


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame)

