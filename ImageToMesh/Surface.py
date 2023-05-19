# -*- coding: utf-8 -*-
"""
Created on Sat Feb 08 16:00:31 2020
version:2.0
@author: Juan G. Diosa
Improved with chatGPT on Sat Mar 18 2023

###############################################################################
#     UNIVERSIDAD DE ANTIOQUIA - PURDUE UNIVERSITY - UNIVERSIDAD CES          #
###############################################################################
#                  ***************************************                    #
#++++++                          Juan Diosa                             ++++++#
#                  ***************************************                    #
###############################################################################
# Use this source code is under CC BY-ND license, Any warranties are disclaimed.
###############################################################################

Creates a FEBio mesh for four skin layers from a png file or a sinusoidal surface
given the amplitude and period.

"""
#------------------------------------------------------------------------------ 
# Time calculation of the script running
import timeit 
tic = timeit.default_timer()

#------------------------------------------------------------------------------ 
# Getting the file path to open
import os 
import glob
import pathlib

#https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
#answered by Aminius Feb 26 19 at 18:36
folder = str(pathlib.Path(__file__).parent.absolute())


############################################################################### 
# Surface dimensions 
#------------------------------------------------------------------------------ 
xDimension = 3.5 #<--------------------------------------------- Here X maximum value
yDimension = 3.5 #<--------------------------------------------- Here Y maximum value
height = 0.16#<------------------------------------------- Here Z maximun value

#------------------------------------------------------------------------------
# There are two treatments for the dot cloud :
# 1 Smoothing process using averages 3x3
# 2 Gaussian filter 5x5,a sigma value is required. 1 is used by default
TreatmentMod = 2; sigma = 0.75##<--------------------Write here the treatment option
# -------------------0 None, 1 to Smoothing, 2 to Gaussian and define sigma

# There are two options for the mesh:
# 0 Mesh WITHOUT addtional nodes to have a transtion from random height to zero
# 1 Mesh with addtional nodes to have a transtion from random height to zero
AdditionalNodesOption = 1
# Surface options 
# There are two surface options :
# 1 Base on a picture
# 2 Sinusoidal
SurfaceOption = 2 #<--------------------------------------------- Here X maximum value
#%%

###############################################################################
#-----------------------------------------------------------------------------
# Define amplitude, frequency, square size, and meshgrid divisions
# If the sinusoidal surface is used, It is recommended not to use additional nodes
amplitude = 0.09
frequency = 6
squareSize = 4
divisions = 144

#------------------------------------------------------------------------------
# Png information and surface parameters
from PIL import Image
fileName = '7080Sq3000.png'                         #<-Write the Image Name here
filePath = folder+'/'+fileName
ImportedImage = Image.open(filePath, 'r')

#%%
###############################################################################
#------------------------------------------------------------------------------
# Surface options
if SurfaceOption == 1:
    from DotsFromPicture import DotsFromPicture
    Dots, columns, rows = DotsFromPicture(ImportedImage, height, TreatmentMod, sigma)
else:
    from SinusoidalSurface import SinusoidalSurface
    # Call the create_sinusoidal_surface function
    Dots, columns, rows = SinusoidalSurface(amplitude, frequency, squareSize, divisions)
    
#%%
#------------------------------------------------------------------------------
# Option additional elements
from AdditionalNodes import AdditionalNodes
if AdditionalNodesOption == 0:
    DotsMod = Dots
else:
    if SurfaceOption == 1:
        DotsMod = AdditionalNodes(Dots)
    else:
        from Filters import Smoothing
        DotsMod = Smoothing(divisions, 
                            divisions, 
                            AdditionalNodes(Dots))
#%%

###############################################################################
#------------------------------------------------------------------------------
# FEBIO Hexahedral mesh:
# Mesh with transition between rough to flat in the layers,
# multiplying the surface info by a percentage the skin surface

dy = yDimension/(rows-1)
dx = xDimension/(columns-1)

from MeshFeBioTransition import MeshFeBioTransition
MeshInfo=  MeshFeBioTransition(dx,dy,DotsMod)


###############################################################################
#------------------------------------------------------------------------------ 
# Stop the time calculation of the script running
toc=timeit.default_timer()
T=(toc-tic)/60