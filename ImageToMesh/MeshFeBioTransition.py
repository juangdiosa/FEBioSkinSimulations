# -*- coding: utf-8 -*-
"""
Mesh Febio Transition
Creates a mesh of five elements with a transition between rough surface to
flat for a Febio format
Created on Tue Feb 11 20:47:12 2020
@author: Juan G. Diosa
ver:2.0

The lowest cloud value must be 0 !!!!

"""
def MeshFeBioTransition(dx,dy,dots):
  import numpy as np
  #############################################################################
  #Bias and preparation
  #############################################################################
  #---------------------------------------------------------------------------#
  #Distance between Layers
  #Thickness for the layers
  #---------------------------------------------------------------------------#
  Epidermis = 0.07
  Stratum = 0.02
  Dermis = 0.84
  Hypodermis = 2
  thicknessViable = Epidermis-Stratum
  
  
  #---------------------------------------------------------------------------#
  #Number of levels and Bias for each one
  #---------------------------------------------------------------------------#
  LevelsEpi = 3
  BiasEpi = 1.3
  LevelsDermis = 8
  BiasDermis = 1.3
  LevelsHypo=6
  Biashipo = 1.1
  dz = np.zeros((LevelsEpi + LevelsDermis + LevelsHypo - 1, 1))
  
  
  #---------------------------------------------------------------------------#
  # Depth for each Level
  # Modify acording to the number of levels !!!!!!!!!
  #---------------------------------------------------------------------------#
  #---------------------------------------------------------------------------#
  #Viable Epidermis & Stratum Corneum
  dz[1,0] = Stratum
  from Bias import BiasV
  ZEpi = BiasV(LevelsEpi, thicknessViable, BiasEpi)
  dz[2,0] = Stratum + ZEpi[1,0]
  dz[3,0] = Epidermis
  
  #---------------------------------------------------------------------------#
  #Dermis
  ZDermis = BiasV(LevelsDermis, Dermis, BiasDermis)
  dz[4,0] = Epidermis + ZDermis[1,0]
  dz[5,0] = Epidermis + ZDermis[2,0]
  dz[6,0] = Epidermis + ZDermis[3,0]
  dz[7,0] = Epidermis + ZDermis[4,0]
  dz[8,0] = Epidermis + ZDermis[5,0]
  dz[9,0] = Epidermis + ZDermis[6,0]
  dz[10,0] = Epidermis + Dermis
  #---------------------------------------------------------------------------#
  #Hypodermis
  ZHypo = BiasV(LevelsHypo, Hypodermis, Biashipo)
  dz[11,0] = dz[10,0] + ZHypo[1,0]
  dz[12,0] = dz[10,0] + ZHypo[2,0]
  dz[13,0] = dz[10,0] + ZHypo[3,0]
  dz[14,0] = dz[10,0] + ZHypo[4,0]
  dz[15,0] = dz[10,0] + Hypodermis
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

  #############################################################################
  #Nodes Heights in each layer
  #############################################################################

  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  #Modify according the levels !!!!!!!!!
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  rows = dots.shape[0]
  columns = dots.shape[1]
  level2 = dots - dz[1,0] * np.ones((rows, columns))
    
  level3 = np.zeros((rows, columns))
  level4 = np.zeros((rows, columns))
  level5 = np.zeros((rows, columns))
  for i in range(1, rows+1):
      for j in range(1, columns+1):
          level3[i-1,j-1] = 0.75 * dots[i-1,j-1] - dz[2,0]
          level4[i-1,j-1] = 0.5 * dots[i-1,j-1] - dz[3,0]
          level5[i-1,j-1] = 0.25 * dots[i-1,j-1] - dz[4,0]

  level6 = -dz[5,0] * np.ones((rows, columns))
  level7 = -dz[6,0] * np.ones((rows, columns))
  level8 = -dz[7,0] * np.ones((rows, columns))
  level9 = -dz[8,0] * np.ones((rows, columns))
  level10 = -dz[9,0] * np.ones((rows, columns))
  level11 = -dz[10,0] * np.ones((rows, columns))
  level12 = -dz[11,0] * np.ones((rows, columns))
  level13 = -dz[12,0] * np.ones((rows, columns))
  level14 = -dz[13,0] * np.ones((rows, columns))
  level15 = -dz[14,0] * np.ones((rows, columns))
  level16 = -dz[15,0] * np.ones((rows, columns))


  #############################################################################
  #Nodes label and coordinates
  #############################################################################

  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  #Modify according the levels !!!!!!!!!
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  Nc=[]
  Nx=[]
  Ny=[]
  Nz=[]
  CountPos = 1
  #--------------------------------------------------------------------------#
  #Stratum Corneum Nodes
  for column in range(1, columns+1):
      for row in range(1, rows+1):
          for k in range(2, 0, -1):
            Nc.append(CountPos)
            Nx.append(dx * (column-1))
            Ny.append(-dy * (row-1))
            if k==1:
                Nz.append(dots[row-1,column-1])
            else:
                Nz.append(level2[row-1,column-1])
            CountPos += 1
  #--------------------------------------------------------------------------#
  #Viable epidermis Nodes
  for column in range(1, columns+1):
      for row in range(1, rows+1):
          for k in range(LevelsEpi-1, 0, -1):
            Nc.append(CountPos)
            Nx.append(dx * (column-1))
            Ny.append(-dy * (row-1))
            if k == 1:
                Nz.append(level3[row-1,column-1])
            else:
                Nz.append(level4[row-1,column-1])
            CountPos += 1
  #--------------------------------------------------------------------------#
  #Dermis Nodes
  for column in range(1, columns+1):
      for row in range(1, rows+1):
          for k in range(LevelsDermis-1, 0, -1):
            Nc.append(CountPos)
            Nx.append(dx * (column-1))
            Ny.append(-dy * (row-1))
            if k == 1:
                Nz.append(level5[row-1,column-1])
            if k == 2:
                Nz.append(level6[row-1,column-1])
            if k == 3:
                Nz.append(level7[row-1,column-1])
            if k == 4:
                Nz.append(level8[row-1,column-1])
            if k == 5:
                Nz.append(level9[row-1,column-1])
            if k == 6:
                Nz.append(level10[row-1,column-1])
            if k == 7:
                Nz.append(level11[row-1,column-1])
            CountPos+= 1
  #--------------------------------------------------------------------------#
  #Hypodermis Nodes
  for column in range(1,columns+1):
      for row in range(1,rows+1):
          for k in range(LevelsHypo-1, 0, -1):
            Nc.append(CountPos)
            Nx.append(dx * (column-1))
            Ny.append(-dy * (row-1))
            if k == 1:
                Nz.append(level12[row-1,column-1])
            if k == 2:
                Nz.append(level13[row-1,column-1])
            if k == 3:
                Nz.append(level14[row-1,column-1])
            if k == 4:
                Nz.append(level15[row-1,column-1])
            if k == 5:
                Nz.append(level16[row-1,column-1])
            CountPos += 1


  #############################################################################
  #Elements
  #############################################################################
  #Elements
  #Coordinate system Z is normal to the screen
  #This code creates the conectivity for each skin layer, it begins from the
  #upper left corner in the deepest level for each skin layer
  #(starting stratum, viable epidermis, .....,Hypodermis). The following
  #nodes are wich are above (from deeper to closest to the surface) until
  #reach the outer level of that skin layer. the CountPosing increses from the
  #first row to the last and continue to the next column.
  #-------------------------------------------------------------------------#
  #Stratum Corneum Elements
  Ec = []
  E1 = []
  E2 = []
  E3 = []
  E4 = []
  E5 = []
  E6 = []
  E7 = []
  E8 = []
  CountPos = 1
  
  # THIS PART IS VALID FOR STRATUM CORNEUM ONLY !!!!!
  #Ec has the node label base on count
  #E5: 2*i-1+ rows * 2 * (j-1);
  # (2*i-1) is the row term,It begins from deeper layer and gives a label for
  # each node of the matrix. 2 is the number of layers of stratum corneum,
  # i the row, and -1 helps to continue being in the deeper layer.
  # (rows*2*(j-1)) is the column term, where 2 it is the number of layer of
  # stratum corneum, and with rows help to give the proper label in each
  # column. (j-1) is a swith.
  #E6 is in the same row of E5 but in the next column = E5 + Rows * 2, where 2 is the number of layers
  #E7 is above of E7: E6 + 2, where 2 is the number of layers
  #E8 is above of E5: E5 + 2, where 2 is the number of layers
  #E1,E2,E3 and E4 are in the next row of E5,E6,E7 and E8 respectibily
  
  for j in range(1, columns):
      for i in range(1, rows):
          Ec.append(CountPos)
          E5.append(2 * i-1+rows * 2 * (j-1))
          E6.append(E5[CountPos-1]+2 * rows)
          E7.append(E6[CountPos-1]+2)
          E8.append(E5[CountPos-1]+2)
          E1.append(E5[CountPos-1]+1)
          E2.append(E6[CountPos-1]+1)
          E3.append(E7[CountPos-1]+1)
          E4.append(E8[CountPos-1]+1)
          CountPos += 1
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  # STRATEGY OF VIABLE EPIDERMIS, DERMIS AND HYPODERMIS
  #Ec has the node label acording to the general counting
  #E5: [(PreviousLayers)*rows*colum]+[(#LevelsOfLayers-1)*i-(#LevelsOfLayers-2)]
  # +(k-1)+[(#LevelsOfLayers-1)*rows*(j-1)];
  #(~) [(PreviousLayers)*rows*colum], It gives initial number of node for each
  # layers
  #(~) [(#LevelsOfLayers-1)*i-(#LevelsOfLayers-2)] is the row term,
  # It begins from deeper layer and gives a label for each node of the matrix.
  # where i is the row parameter of for loop
  #(~)(k-1) is the element deep term, k is the deep parameter of for loop
  # and It is number of levels of layers minus 1
  #(~)[(#LevelsOfLayers-1)*rows*(j-1)] is the column term, (j-1) is a swith
  # where j is the column parameter of for loop
  #E6 is in the same row of E5 but in the next column = E5 + Rows * N, where
  #N is the number of levels minus 1
  #E7 is above of E6: E6 + N, N is the number of levels
  #E8 is above of E5: E5 + N, N is the number of levels
  # If k=(#LevelsOfLayers-1) E1,E2,E3 and E4 are E5 (without (k-1)term), E6,
  # E7 and E8 of previous layers, otherwise
  #E1,E2,E3 and E4 are in the next row of E5,E6,E7 and E8 respectibily (E1=E5+1)
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
  #-------------------------------------------------------------------------#
  #Viable Epidermis
  Ec2 = []
  E12 = []
  E22 = []
  E32 = []
  E42 = []
  E52 = []
  E62 = []
  E72 = []
  E82 = []
  position = 1
  for j in range(1, columns):
      for i in range(1, rows):
          for k in range(1, LevelsEpi):
              Ec2.append(CountPos)
              E52.append(2 * rows * columns+(LevelsEpi-1) * i-(LevelsEpi-2)+(k-1)+(LevelsEpi-1) * rows * (j-1))
              E62.append(E52[position-1]+(LevelsEpi-1) * rows)
              E72.append(E62[position-1]+2)
              E82.append(E52[position-1]+2)
              if k == LevelsEpi-1:
                  E12.append(2 * i-1+rows * 2 *(j-1))
                  E22.append(E12[position-1]+2 * rows)
                  E32.append(E22[position-1]+2)
                  E42.append(E12[position-1]+2)
              else:
                  E12.append(E52[position-1]+1)
                  E22.append(E62[position-1]+1)
                  E32.append(E72[position-1]+1)
                  E42.append(E82[position-1]+1)
              CountPos += 1
              position += 1
              
  #-------------------------------------------------------------------------#
  #Dermis
  Ec3 = []
  E13 = []
  E23 = []
  E33 = []
  E43 = []
  E53 = []
  E63 = []
  E73 = []
  E83 = []
  position = 1
  for j in range(1, columns):
      for i in range(1, rows):
          for k in range(1, LevelsDermis):
              Ec3.append(CountPos)
              E53.append((2+LevelsEpi-1) * rows * columns+(LevelsDermis-1) * i-(LevelsDermis-2)+(k-1)+(LevelsDermis-1) * rows * (j-1))
              E63.append(E53[position-1]+(LevelsDermis-1) * rows)
              E73.append(E63[position-1]+(LevelsDermis-1))
              E83.append(E53[position-1]+(LevelsDermis-1))
              if k == LevelsDermis-1:
                  E13.append(2 * rows * columns+(LevelsEpi-1) * i-(LevelsEpi-2)+(LevelsEpi-1) * rows * (j-1))
                  E23.append(E13[position-1]+(LevelsEpi-1) * rows)
                  E33.append(E23[position-1]+(LevelsEpi-1))
                  E43.append(E13[position-1]+(LevelsEpi-1))
              else:
                  E13.append(E53[position-1]+1)
                  E23.append(E63[position-1]+1)
                  E33.append(E73[position-1]+1)
                  E43.append(E83[position-1]+1)
              CountPos += 1
              position += 1
  #-------------------------------------------------------------------------#
  #Hypodermis
  Ec4 = []
  E14 = []
  E24 = []
  E34 = []
  E44 = []
  E54 = []
  E64 = []
  E74 = []
  E84 = []
  position = 1
  for j in range(1, columns):
      for i in range(1, rows):
          for k in range(1, LevelsHypo):
              Ec4.append(CountPos)
              E54.append((2+LevelsEpi-1+LevelsDermis-1) * rows * columns+(LevelsHypo-1) * i-(LevelsHypo-2)+(k-1)+(LevelsHypo-1) * rows * (j-1))
              E64.append(E54[position-1]+(LevelsHypo-1) * rows)
              E74.append(E64[position-1]+(LevelsHypo-1))
              E84.append(E54[position-1]+(LevelsHypo-1))
              if k == LevelsHypo-1:
                  E14.append((2+LevelsEpi-1) * rows * columns+(LevelsDermis-1) * i-(LevelsDermis-2)+(LevelsDermis-1) * rows * (j-1))
                  E24.append(E14[position-1]+(LevelsDermis-1) * rows)
                  E34.append(E24[position-1]+(LevelsDermis-1))
                  E44.append(E14[position-1]+(LevelsDermis-1))
              else:
                  E14.append(E54[position-1]+1)
                  E24.append(E64[position-1]+1)
                  E34.append(E74[position-1]+1)
                  E44.append(E84[position-1]+1)
              CountPos += 1
              position += 1

  #############################################################################
  #FeBio Mesh File
  #############################################################################
  from FeBioFileMultilayer import FeBioFile
  mesh=dict();
  mesh['Nc']=Nc
  mesh['Nx']=Nx
  mesh['Ny']=Ny
  mesh['Nz']=Nz
  
  mesh['Ec']=Ec
  mesh['E1']=E1
  mesh['E2']=E2
  mesh['E3']=E3
  mesh['E4']=E4
  mesh['E5']=E5
  mesh['E6']=E6
  mesh['E7']=E7
  mesh['E8']=E8
  
  mesh['Ec2']=Ec2
  mesh['E12']=E12
  mesh['E22']=E22
  mesh['E32']=E32
  mesh['E42']=E42
  mesh['E52']=E52
  mesh['E62']=E62
  mesh['E72']=E72
  mesh['E82']=E82
  
  mesh['Ec3']=Ec3
  mesh['E13']=E13
  mesh['E23']=E23
  mesh['E33']=E33
  mesh['E43']=E43
  mesh['E53']=E53
  mesh['E63']=E63
  mesh['E73']=E73
  mesh['E83']=E83
  
  mesh['Ec4']=Ec4
  mesh['E14']=E14
  mesh['E24']=E24
  mesh['E34']=E34
  mesh['E44']=E44
  mesh['E54']=E54
  mesh['E64']=E64
  mesh['E74']=E74
  mesh['E84']=E84
  
  FeBioFile(mesh)
  
  #return(mesh)
