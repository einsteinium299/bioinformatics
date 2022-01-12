**Materials**  

*   Molecule atp.pdb  
    
*   Software  
    *   Debian 5.10.46-4  
        
    *   Pypovray 2018-11-08
        
    *   Povray 3.7.0.8  
        
    *   Python 3.9.2 with libraries:  
        *   Vapory 0.1.01  
            
        *   ffmpy 0.3.0  
            
        *   moviepy 1.0.3  
            
        *   numpy 1.21.4  
            
        *   scipy 1.7.3  
            
        *   pathos 0.2.8  
            

**Methods**  

The animation is written in Python 3.9.2. In the script the functions pypovray, vapory and math are imported to make the script possible. The script has to be executed in the pypovray folder cloned from bitbucket. Read the readme.txt to understand how to run this script.  To change the molecule, go find a different .pdb file and find which atoms need to be split from the main molecule.  

Edit the pdb file by changing the filename in this line:  

*   ATP = pdb.PDBMolecule('{}/pdb/atp.pdb'.format(SETTINGS.AppLocation), center=True)  
    

Edit this line to split the molecule, edit the numbers in the divide function. You can find out these atom numbers by printing out ATP and looking at the X,  Y and Z coordinates to see which ones you need. Getting the right molecules can be difficult, you may have to run this script a couple of times to figure it out.  

*   ATP\_divide = ATP.divide(\[12, 13, 14, 15, 16\], 'phosphate', offset=\[0, ((step - 25) \* 0.1), 0\])  
    

The animation result will be located in the movies folder with the name simulation.mp4  

To change the length of the animation, edit in default.ini the values Duration and RenderFPS to your liking.
