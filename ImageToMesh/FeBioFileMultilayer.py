# -*- coding: utf-8 -*-
"""
FeBio format
Writes the mesh info in a FeBio file for a multilayer model
Created on Thu Feb 13 06:19:59 2020

@author: Juandiosa
"""
def FeBioFile(MeshInfo):
###################################################################################
#Creates a Febio file for a single part base on the nodes and element information
###################################################################################
#Base on
#https://www.guru99.com/reading-and-writing-files-in-python.html
    f=open("7080Sq3000Ad10ad2.feb","w+")
    f.write("<?xml version=\"1.0\" enconding=\"ISO-8859-1\"?>\n")
    f.write("<febio_spec version=\"2.5\">\n")
    f.write("	<Globals>\n")
    f.write("		<Constants>\n")   
    f.write("			<T>0</T>\n")
    f.write("			<R>0</R>\n")
    f.write("			<Fc>0</Fc>\n")
    f.write("		</Constants>\n")
    f.write("	</Globals>\n")
    f.write("	<Geometry>\n")
    f.write("		<Nodes name=\"Skin\">\n")
    #https://stackoverflow.com/questions/47825291/error-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index?rq=1
    N=MeshInfo['Nc'];Nx=MeshInfo['Nx'];Ny=MeshInfo['Ny'];Nz=MeshInfo['Nz']
    for i in range (0,len(MeshInfo['Nc'])):
        f.write("			<node id=\"%s\">" %N[i]+" %s," %Nx[i]+\
                " %s," %Ny[i]+" %s</node>\n" %Nz[i])
    f.write("		</Nodes>\n")
    #-------------------------------------------------------------------------#
    #Stratum corneum
    f.write("		<Elements type=\"hex8\" elset=\"StratumCorneum\">\n")
    E=MeshInfo['Ec'];E1=MeshInfo['E1'];E2=MeshInfo['E2'];E3=MeshInfo['E3'];
    E4=MeshInfo['E4'];E5=MeshInfo['E5'];E6=MeshInfo['E6'];E7=MeshInfo['E7'];
    E8=MeshInfo['E8'];
    for i in range (0,len(E)):
        f.write("			<elem id=\"%s\">" %E[i]+" %s," %E1[i]+\
                " %s," %E2[i]+" %s," %E3[i]+" %s," %E4[i]+" %s," %E5[i]+\
                " %s," %E6[i]+" %s," %E7[i]+" %s</elem>\n" %E8[i]) 
    f.write("		</Elements>\n")
    #-------------------------------------------------------------------------#
    #Viable Epidermis
    f.write("		<Elements type=\"hex8\" elset=\"ViableEpidermis\">\n")
    E2=MeshInfo['Ec2'];E12=MeshInfo['E12'];E22=MeshInfo['E22'];E32=MeshInfo['E32'];
    E42=MeshInfo['E42'];E52=MeshInfo['E52'];E62=MeshInfo['E62'];E72=MeshInfo['E72'];
    E82=MeshInfo['E82'];
    for i in range (0,len(E2)):
        f.write("			<elem id=\"%s\">" %E2[i]+" %s," %E12[i]+\
                " %s," %E22[i]+" %s," %E32[i]+" %s," %E42[i]+" %s," %E52[i]+\
                " %s," %E62[i]+" %s," %E72[i]+" %s</elem>\n" %E82[i]) 
    f.write("		</Elements>\n")
    #-------------------------------------------------------------------------#
    #Dermis
    f.write("		<Elements type=\"hex8\" elset=\"Dermis\">\n")
    E3=MeshInfo['Ec3'];E13=MeshInfo['E13'];E23=MeshInfo['E23'];E33=MeshInfo['E33'];
    E43=MeshInfo['E43'];E53=MeshInfo['E53'];E63=MeshInfo['E63'];E73=MeshInfo['E73'];
    E83=MeshInfo['E83'];
    for i in range (0,len(E3)):
        f.write("			<elem id=\"%s\">" %E3[i]+" %s," %E13[i]+\
                " %s," %E23[i]+" %s," %E33[i]+" %s," %E43[i]+" %s," %E53[i]+\
                " %s," %E63[i]+" %s," %E73[i]+" %s</elem>\n" %E83[i]) 
    f.write("		</Elements>\n")
    #-------------------------------------------------------------------------#
    #Hypodermis
    f.write("		<Elements type=\"hex8\" elset=\"Hypodermis\">\n")
    E4=MeshInfo['Ec4'];E14=MeshInfo['E14'];E24=MeshInfo['E24'];E34=MeshInfo['E34'];
    E44=MeshInfo['E44'];E54=MeshInfo['E54'];E64=MeshInfo['E64'];E74=MeshInfo['E74'];
    E84=MeshInfo['E84'];
    for i in range (0,len(E4)):
        f.write("			<elem id=\"%s\">" %E4[i]+" %s," %E14[i]+\
                " %s," %E24[i]+" %s," %E34[i]+" %s," %E44[i]+" %s," %E54[i]+\
                " %s," %E64[i]+" %s," %E74[i]+" %s</elem>\n" %E84[i])                 
    f.write("		</Elements>\n")
    f.write("	</Geometry>\n")
    f.write("	<Output>\n")
    f.write("		<plotfile type=\"febio\"/>\n")
    f.write("	</Output>\n")
    f.write("</febio_spec>")
    f.close()
###################################################################################
#Reference values
###################################################################################
