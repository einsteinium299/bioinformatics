#!/usr/bin/env python3

"""
A script for rotating a camera around multiple objects.

Note: pypovray and it's dependencies have to be installed.
Instructions at:
https://nbviewer.org/urls/bitbucket.org/mkempenaar/pypovray/raw/master/manual/install_and_configure.ipynb

This script has to be located in the folder of the cloned git repository.

Edit the Duration and RenderFPS in default.ini to your desired values.
"""

__author__ = 'SL de Haan & Lara Cisci'
__version__ = '0.0.1'

from vapory import Scene, LightSource, Camera, Background, Plane, Texture, Pigment, Cylinder, Cone, Finish, Sphere, Box
from pypovray import pypovray, models
from math import sin, cos


def cube(x_axis, y_axis, z_axis):
    """
    Creates a sphere and places this in a scene
    : param : floats
    : returns: all objects in a list called cube_list
    """

    color = Texture(Pigment('color', [0, 1, 1], 'filter', 0),
        Finish('phong', 0, 'reflection', 0.5))
    color2 = Texture(Pigment('color', [1, 1, 0], 'filter', 0),
        Finish('phong', 0, 'reflection', 0.5))

    # Object
    sphere = Sphere([x_axis, y_axis, z_axis+4], 2.5, color2)

    box1 = Box([x_axis-5, y_axis-5, z_axis], [x_axis+5, y_axis-3, z_axis+8], color)
    box2 = Box([x_axis-5, y_axis-5, z_axis], [x_axis-3, y_axis+5, z_axis+8], color)
    box3 = Box([x_axis+5, y_axis-5, z_axis], [x_axis+3, y_axis+5, z_axis+8], color)
    box4 = Box([x_axis-5, y_axis+3, z_axis], [x_axis+5, y_axis+5, z_axis+8], color)

    cone1 = Cone([x_axis+5, y_axis, z_axis+4], 2.5, [x_axis+8, y_axis, z_axis+4], 0, color2)
    cone2 = Cone([x_axis-5, y_axis, z_axis+4], 2.5, [x_axis-8, y_axis, z_axis+4], 0, color2)
    cone3 = Cone([x_axis, y_axis+5, z_axis+4], 2.5, [x_axis, y_axis+8, z_axis+4], 0, color2)
    cone4 = Cone([x_axis, y_axis-5, z_axis+4], 2.5, [x_axis, y_axis-8, z_axis+4], 0, color2)

    cube_list = [sphere, box1, box2, box3, box4, cone1, cone2, cone3, cone4]

    return cube_list


def yellow_sphere(step):
    """
    yellow sphere with a variable on the y axis.
    : param : step
    : returns: yellow_sphere
    """
    
    yellow_sphere = Sphere([-5, step-10, 20], 5, Texture(Pigment('color', [1, 1, 0])))

    return yellow_sphere


def purple_sphere(step):
    """
    : purple sphere with a variable on the z axis.
    : param : step
    : returns : purple_sphere
    """
    
    purple_sphere = Sphere([-5, 10, step-100], 5, Texture(Pigment('color', [1, 0, 1])))

    return purple_sphere


def legend(x_axis, y_axis, z_axis):
    """
    Given x, y and z coordinates it returns a list of objects together forming a legend.
    : param coordinates : float
    : returns : list
    """

    cylinderx = Cylinder([x_axis-5, y_axis, z_axis], [x_axis, y_axis, z_axis],
            0.05, Pigment('color',[1, 0 , 0]))
    cylindery = Cylinder([x_axis-5, y_axis, z_axis], [x_axis-5, y_axis+5, z_axis],
            0.05, Pigment('color',[0, 0 , 1]))
    cylinderz = Cylinder([x_axis-5, y_axis, z_axis], [x_axis-5, y_axis, z_axis+5],
            0.05, Pigment('color',[0, 1 , 0]))

    conex = Cone([x_axis, y_axis, z_axis], 0.2, [x_axis+1, y_axis, z_axis], 0,
            Pigment('color',[1, 0 , 0]))
    coney = Cone([x_axis-5, y_axis+5, z_axis], 0.2, [x_axis-5, y_axis+6, z_axis], 0,
            Pigment('color',[0, 0 , 1]))
    conez = Cone([x_axis-5, y_axis, z_axis+5], 0.2, [x_axis-5, y_axis, z_axis+6], 0,
            Pigment('color',[0, 1 , 0]))

    # Return scene object for rendering

    legend_list = [cylinderx, cylindery, cylinderz, conex, coney, conez]

    return legend_list


def frame(step):
    """
    frame collects all the objects and scenary for the final render.
    : param : step
    : returns : Scene
    """

    # X & Z axis rotation, Y axis moving up and down.
    camera = Camera('location', [(sin(step/30))*120, (sin(step/30)*15)+25, (cos(step/30))*120], 'look_at', [0, 12, 0])
    
    # The position of the legend and cube can be changed
    # by changing the x, y, z coordinates.
    legend_list = legend(-15, 10, 0)
    cube_list = cube((sin(step/30))*10, (sin(step/30)*20)+5, (cos(step/30))*10)

    sun = yellow_sphere((sin(step/30)*15)+10) # Sphere moving up and down
    asteroid = purple_sphere(step) # Sphere moving away for infinity

    light1 = LightSource([-5, step-10, 20], 0.5)
    light2 = LightSource([-10, 15, -20], 0.5)
    light3 = LightSource([0, 5, -20], 1.2)
    light4 = LightSource([-15, -20, -20], 0.5)
    light5 = LightSource([10, -20, -20], 0.5)

    plain_ground = Plane([0, 1, 0], -20, Texture(Pigment('checker', 'color', [1, 1, 1], 'color', [0, 1, 1], 'scale', 20)))
    background = Background([0.7, 0.9, 0.9])

    return Scene(camera, objects=[sun, asteroid, plain_ground, light1, light2, light3, light4, light5, background]
            + cube_list + legend_list)


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame)
