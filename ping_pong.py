#!/usr/bin/env python3

"""
A script that makes a .gif file of a ball moving from left to right and back,
while also moving up and down in the process.

Note: pypovray and it's dependencies have to be installed.
Instructions at:
https://nbviewer.org/urls/bitbucket.org/mkempenaar/pypovray/raw/master/manual/install_and_configure.ipynb

This script has to be located in the folder of the cloned git repository.

Edit the Duration and RenderFPS in default.ini to your desired values.
"""


__author__ = 'SL de Haan & Lara Cisci'
__version__ = '0.0.1'


from vapory import Scene, LightSource, Camera, Sphere, Texture, Pigment, Plane, Finish
from pypovray import pypovray, SETTINGS
from math import sin, cos, pi


# CONSTANTS
n_frames = eval(SETTINGS.NumberFrames) # contains amount of frames in default.ini
step_rate = 320/n_frames # the rate at which each frame changes, depending on the amount of frames in default.ini


def ball(ball_position):
    """
    ball creates a frame of a sphere according to it's frame number.
    : param : ball_position
    : returns : ball

    """

    # x position sphere: (step_rate * ball_position)-((n_frames/4))*step_rate 
    # : Moves left to right back to left.
    # y position sphere: sin((step_rate * ball_position)*0.2)*15
    # : Moves the ball up and down with the sinus function.

    ball = Sphere([(step_rate * ball_position)-((n_frames/4))*step_rate, sin((step_rate * ball_position)*0.2)*15 ,0], 4, 
            Texture(Pigment('color', [0, 1, 1]), Finish('phong', 0.6, 'reflection', 0.4)))

    return ball 


def frame(step):
    """
    frame collects all the objects and scenary for the final render.
    : param : step
    : returns : Scene
    """


    # Moving the variable ball_position up half way the frame count and back down.
    if step < n_frames/2:
        ball_position = step
    else:
        stepsize = step - n_frames/2
        ball_position = n_frames/2 - stepsize


    # Defining all objects
    ball_object = ball(ball_position)
    
    plane_ground = Plane([0, 1, 0], -20, Texture(Pigment('checker', 'color', [1, 1, 0], 'color', [0, 1, 1], 'scale', 30)))
    plane_sky = Plane([0, 1, 0], 50, Texture(Pigment('color', [0, 1, 5])))
    camera = Camera('location', [0, 3, -140], 'look_at', [0, 0, 0])

    light_middle = LightSource([0, 30, -20], 0.8)
    light_left = LightSource([-20, 10, 30], 0.8)
    light_right = LightSource([20 ,10, 30], 0.8)

    return Scene(camera, objects=[ball_object, light_middle, light_left, light_right, plane_ground, plane_sky])


if __name__ == '__main__':
    pypovray.render_scene_to_gif(frame)

