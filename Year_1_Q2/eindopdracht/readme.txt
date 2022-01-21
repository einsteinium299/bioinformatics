Author: Stijn de Haan
Date: 01-21-2022
Version: 0.0.1

Name
NMDA receptor visualised.

Description
Renders an animation of an NMDA receptor with glutamine binding with the receptor, magnesium moving out of the receptor opening up a pathway for sodium and calcium. The animation is rendered with povray through the pypovray library. Pypovray is a python library that talks to the povray language made by teachers from Hanzehogeschool bioinformatics. The sphere moves in a triangle-like line from left to right and vice versa. the framed can be changed to your liking to make the sphere move faster or slower.


Installation
To install pypovray, enter the commands in this guide[https://nbviewer.org/urls/bitbucket.org/mkempenaar/pypovray/raw/master/manual/install_and_configure.ipynb]. Povray only works on linux with Python 3, if you use windows, go find a linux machine or start a virtual machine. Make sure to remove the version numbers from requirements.txt. 


From this:

ffmpy==0.2.2
moviepy==1.0.1
numpy==1.17.4
scipy==1.3.2
# Python multiprocessing using extended pickle serialization with
# dill: https://github.com/uqfoundation/dill
# and pathos: https://github.com/uqfoundation/pathos
pathos==0.2.5 

to this:

ffmpy
moviepy
numpy
scipy
# Python multiprocessing using extended pickle serialization with
# dill: https://github.com/uqfoundation/dill
# and pathos: https://github.com/uqfoundation/pathos
pathos


Make sure you change the path to your pypovray folder in default.ini

The source of the PDB file is https://molview.org/?cid=33032, this is a .mol filetype. Make sure to convert it to .pdb with BabelWeb http://cdb.ics.uci.edu/cgibin/BabelWeb.py

make sure this file is located in the pdb folder under the pypovray directory.


Usage

To render this script, go to your cloned directory and run:
> python3 eindscript.py

You should get an output like this:

INFO:pypovray: Using config file "default.ini"

Wait a few seconds for it to render and look inside the images directory to see your result.


Support
If your program returns errors, make sure to read them carefully. In case you cannot fix these yourself, you can always mail me at pypovrayteam@povmail.com for help online or go to the bitbucket repository issue tracker.


Authors and acknowledgment
We appreciate the creators of pypovray mkempenaar, rWedema and other contributors. We would also like to give our deepest respect to the developers of povray David Kirk Buck, Aaron A. Collins and Alexander Enzmann.
