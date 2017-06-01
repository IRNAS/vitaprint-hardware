# -*- coding: utf-8 -*-
"""
Created on Dec 8 2016

author: Luka Banovic (banovic@irnas.eu)

============= SCAFFOLD G-CODE GENERATOR ================================

This script generates a .gcode file for bioscaffolds of square shape.
        
    INPUTS:
    - file name 
    
    - filament diameter (d [mm]) 
    
    - feed rate (FR [mm/min])
    
    - extrusion rate (ER [mm] - the displacement of the plunger in the 
      z-direction per one move (size mm))
      
    - size (square shape: size = side length [mm])
    
    - number of layers (N_layers)
    
    - skirt (True or False)
    
    - layer height [mm]
    
    - gap size [mm]

   
    OUTPUT: G-CODE file (filename.gcode) in a working directory.
========================================================================
"""

import numpy as np
import math
import datetime

import os
os.chdir(r'....folder path...')

    
def generate_skirt_5(file,ER,FR,size,skirt):
    """
    This function generates a skirt 5mm away from the bioscaffold to 
    stabilize the extrusion.
    """
    
    if skirt == True:
        
        skirt_start = -5     # skirt starting point is X-5 Y-5      
        skirt_end = size+5
        
        file.write("\nG1 X{0} Y{1} F{2}".format(skirt_start, skirt_start,FR))
        file.write("\nG0 Z0")
        skirt_move_1 = "\nG1 X{0} Y{1} E{2}".format( skirt_end, skirt_start,ER)
        skirt_move_2 = "\nG1 X{0} Y{1} E{2}".format( skirt_end, skirt_end,ER)
        skirt_move_3 = "\nG1 X{0} Y{1} E{2}".format( skirt_start, skirt_end, ER)
        skirt_move_4 = "\nG1 X{0} Y{1} E{2}".format( skirt_start, skirt_start, ER)
        file.write(skirt_move_1)
        file.write(skirt_move_2)
        file.write(skirt_move_3)
        file.write(skirt_move_4)
        file.write("\n")
        
    else:
        pass
    
def generate_skirt_10(file,ER,FR,size,skirt):
    """
    This function generates a skirt 10mm away from the bioscaffold to 
    stabilize the extrusion.
    """
    
    if skirt == True:
        
        skirt_start_B = -10     # skirt starting point is X-5 Y-5      
        skirt_end_B = size+10
        
        file.write("\nG1 X{0} Y{1} F{2}".format(skirt_start_B, skirt_start_B,FR))
        file.write("\nG0 Z0")
        skirt_move_1b = "\nG1 X{0} Y{1} E{2}".format( skirt_end_B, skirt_start_B,ER)
        skirt_move_2b = "\nG1 X{0} Y{1} E{2}".format( skirt_end_B, skirt_end_B,ER)
        skirt_move_3b = "\nG1 X{0} Y{1} E{2}".format( skirt_start_B, skirt_end_B, ER)
        skirt_move_4b = "\nG1 X{0} Y{1} E{2}".format( skirt_start_B, skirt_start_B, ER)
        file.write(skirt_move_1b)
        file.write(skirt_move_2b)
        file.write(skirt_move_3b)
        file.write(skirt_move_4b)
        file.write("\n")
        
    else:
        pass

def generate_skirt_7_5(file,ER,FR,size,skirt):
    """
    This function generates a skirt 7.5mm away from the bioscaffold to 
    stabilize the extruision.
    """
    
    if skirt == True:
        
        skirt_start_C = -7.5     # skirt starting point is X-5 Y-5      
        skirt_end_C = size+7.5
        
        file.write("\nG1 X{0} Y{1} F{2}".format(skirt_start_C, skirt_start_C,FR))
        file.write("\nG0 Z0")
        skirt_move_1c = "\nG1 X{0} Y{1} E{2}".format( skirt_end_C, skirt_start_C,ER)
        skirt_move_2c = "\nG1 X{0} Y{1} E{2}".format( skirt_end_C, skirt_end_C,ER)
        skirt_move_3c = "\nG1 X{0} Y{1} E{2}".format( skirt_start_C, skirt_end_C, ER)
        skirt_move_4c = "\nG1 X{0} Y{1} E{2}".format( skirt_start_C, skirt_start_C, ER)
        file.write(skirt_move_1c)
        file.write(skirt_move_2c)
        file.write(skirt_move_3c)
        file.write(skirt_move_4c)
        file.write("\n")
    
# LAYER A
    
def generate_layer_A(file,gap_size, FR, ER, size):
    """
    This function generates a layer in A - orientation.
    """
   
    Ys = np.linspace(0,size,num = math.ceil((size/gap_size)/2.)*2+1).tolist()
    n_iter = 1
    
    file.write("\n G1 X0 Y0 F{0}".format(FR))
    while n_iter < len(Ys)-1:
        
        file.write("\n G1 X{0} Y{1:.3f} E{2}".format( size, Ys[n_iter-1],ER))
        file.write("\n G3 X{0} Y{1:.3f} I0 J{2:.2f}".format(size, Ys[n_iter], abs((Ys[n_iter]-Ys[n_iter-1])/2)))
        file.write("\n G1 X0 Y{0:.3f} E{1}".format(Ys[n_iter], ER))
        file.write("\n G2 X0 Y{0:.3f} I0 J{1:.2f}".format(Ys[n_iter+1] , abs((Ys[n_iter]-Ys[n_iter-1])/2)))
        n_iter = n_iter + 2
    
    file.write("\n G1 X{0} Y{1} E{2}".format(size, size, ER))


    

#LAYER B
def generate_layer_B(file, gap_size, FR, ER, size):
    """
    This function generates a layer in B - orientation.
    """
    Xs = np.linspace(size,0,num = math.ceil((size/gap_size)/2.)*2+1).tolist()
    n_iter = 1
    
    file.write("\n G1 X{0} Y{1}".format(size, size))
    while n_iter < len(Xs)-1:
        
        file.write("\n G1 X{0:.3f} Y0 E{1}".format( Xs[n_iter-1], ER))
        file.write("\n G2 X{0:.3f} Y0 I-{1:.2f} J0".format(Xs[n_iter], abs((Xs[n_iter]-Xs[n_iter-1])/2)))
        file.write("\n G1 X{0:.3f} Y{1} E{2}".format(Xs[n_iter], size, ER))
        file.write("\n G3 X{0:.3f} Y{1} I-{2:.2f} J0".format(Xs[n_iter+1] , size, abs((Xs[n_iter]-Xs[n_iter-1])/2)))
        n_iter = n_iter + 2
    
    file.write("\n G1 X{0} Y{1} E{2}".format(0, 0, ER))



   
def stack_layers(file, gap_size, FR, ER, size, layer_height, N_layers):
    """
    This function stacks layers A and B according to the number
    of laysers specified in N_layers. 
        
        N_layers has to be an even number.
    """
    
    if N_layers % 2 == 0:
        pass
    else:
        raise ValueError('Number of layers has to be even.')
    
    l_iter = 0
    
    while l_iter <= N_layers:
       Z_value_A = l_iter*layer_height
       Z_value_B = (l_iter+1) * layer_height
       
       file.write("\nG0 Z{0:.2f}".format(Z_value_A))
       generate_layer_A(file,gap_size, FR, ER, size)
       file.write("\nG0 Z{0:.2f}".format(Z_value_B))
       generate_layer_B(file,gap_size, FR, ER, size)
       
       l_iter = l_iter + 2
      
       
    file.write("\nG0 Z{0}".format(Z_value_B+5))
       
def check_size(input_size,gap_size):
    """
    This function rounds the size to nearest feasible size.
    """
    d_size = gap_size*(round(input_size/gap_size))
    return round(d_size,3)
   
   
    
    
#%%
if __name__=="__main__":

    fn = input("FILENAME: ")
    date = datetime.datetime.now()
    filename = "{0}-{1}-{2}-".format(date.year,date.month,date.day) + fn
    substring = ".gcode"
    if substring in filename:
        fullfilename = filename
    else:
        fullfilename = filename + ".gcode"

    file = open(fullfilename,"w")
    file.write("%")
    file.write("\nM83")
    
    
    d = input("FILAMENT DIAMETER [mm]: ")
    d = float(d)
    if d <= 0:
        raise ValueError("d must be bigger than 0!")
        
    gap_size = input("GAP SIZE [mm]: ")
    gap_size = round(float(gap_size),2)
    if gap_size < d:
        raise ValueError("Gap size cannot be smaller than filament diameter.")
    
    FR = input("FEED RATE: ")
    FR = float(FR)
    
    ER = input("EXTRUSION RATE: ")
    ER = float(ER)
    
    input_size = input("SIZE: ")
    input_size = float(input_size)
    size = check_size(input_size, gap_size)
    if size != input_size:
        print("\n WARNING: The input size was rounded to closest feasible size. The print size is now {0} × {0} mm.".format(size))

    N_layers = input("NUMBER OF LAYERS: ")
    N_layers = int(N_layers)
    
    
    skirt = input("SKIRT [y/n]: ")
    if skirt == 'y':
        n_skirts = input("NUMBER OF SKIRTS (between 1 and 3): ")
        n_skirts = float(n_skirts)
        if n_skirts >3 or n_skirts < 1:
            raise ValueError("Number of skirts must be 1, 2 or 3.")
        else:
            pass
         # skirt
        if n_skirts == 1:
            generate_skirt_5(file,ER,FR,size,skirt=True)
        elif n_skirts == 2:
            generate_skirt_7_5(file,ER,FR,size,skirt=True)
            generate_skirt_5(file,ER,FR,size,skirt=True)
            
        elif n_skirts == 3:
            generate_skirt_10(file,ER,FR,size,skirt=True)
            generate_skirt_7_5(file,ER,FR,size,skirt=True)
            generate_skirt_5(file,ER,FR,size,skirt=True)
            
    else:
        pass

    layer_height = input("LAYER HEIGHT [mm]: ")
    layer_height = float(layer_height)
      
    # layer generation
    stack_layers(file, gap_size, FR, ER, size, layer_height, N_layers) 
    # closing the file 
    file.write("\n%")

file.close()

                