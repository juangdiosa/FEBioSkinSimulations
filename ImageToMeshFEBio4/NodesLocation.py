# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:54:29 2024

@author: Juan G Diosa 
Nodes Location stores in a dictionary the nodes and elements information
"""

def NodesLocation(dx, dy, dots, Levels, EpidermisLevels, 
                  DermisLevels, HypodermisLevels):
    mesh=dict()
    
    NodesC=[]
    NodesX=[]
    NodesY=[]
    NodesZ=[]

    CountPos = 1
    rows, columns = dots.shape
    
    #stratum corneum layers = 2
    StratumLayers=2
    KLayermax =  StratumLayers-1
    KLayermin = -1
    from NodesLocationInLayer import NodesLocationInLayer
    
    NodesC, NodesX, NodesY, NodesZ, CountPos = NodesLocationInLayer(dx, dy, dots, Levels, 
                             NodesC, NodesX, NodesY, 
                             NodesZ, KLayermax, KLayermin, CountPos)
    
    mesh['Nc'] = NodesC[0::]
    mesh['Nx'] = NodesX[0::]
    mesh['Ny'] = NodesY[0::]
    mesh['Nz'] = NodesZ[0::]
        
    #Viable epidermis   
    KLayermax = EpidermisLevels
    KLayermin = StratumLayers-1
    
    NodesC, NodesX, NodesY, NodesZ, CountPos = NodesLocationInLayer(dx, dy, dots, Levels, 
                             NodesC, NodesX, NodesY, 
                             NodesZ, KLayermax, KLayermin, CountPos)
    
    mesh['Nc2'] = NodesC[len(mesh['Nc'])::]
    mesh['Nx2'] = NodesX[len(mesh['Nc'])::]
    mesh['Ny2'] = NodesY[len(mesh['Nc'])::]
    mesh['Nz2'] = NodesZ[len(mesh['Nc'])::]
    
    #Dermis 
    KLayermax = EpidermisLevels+DermisLevels-1
    KLayermin = EpidermisLevels
    
    NodesC, NodesX, NodesY, NodesZ, CountPos = NodesLocationInLayer(dx, dy, dots, Levels, 
                             NodesC, NodesX, NodesY, 
                             NodesZ, KLayermax, KLayermin, CountPos)
    
    mesh['Nc3'] = NodesC[len(mesh['Nc'])+len(mesh['Nc2'])::]
    mesh['Nx3'] = NodesX[len(mesh['Nc'])+len(mesh['Nc2'])::]
    mesh['Ny3'] = NodesY[len(mesh['Nc'])+len(mesh['Nc2'])::]
    mesh['Nz3'] = NodesZ[len(mesh['Nc'])+len(mesh['Nc2'])::]
       
    #Hypodermis
    KLayermax = EpidermisLevels+DermisLevels+HypodermisLevels-2
    KLayermin = EpidermisLevels+DermisLevels-1
    
    NodesC, NodesX, NodesY, NodesZ, CountPos = NodesLocationInLayer(dx, dy, dots, Levels, 
                             NodesC, NodesX, NodesY, 
                             NodesZ, KLayermax, KLayermin, CountPos)    

    mesh['Nc4'] = NodesC[len(mesh['Nc'])+len(mesh['Nc2'])+len(mesh['Nc3'])::]
    mesh['Nx4'] = NodesX[len(mesh['Nc'])+len(mesh['Nc2'])+len(mesh['Nc3'])::]
    mesh['Ny4'] = NodesY[len(mesh['Nc'])+len(mesh['Nc2'])+len(mesh['Nc3'])::]
    mesh['Nz4'] = NodesZ[len(mesh['Nc'])+len(mesh['Nc2'])+len(mesh['Nc3'])::]
   
    return mesh, NodesC