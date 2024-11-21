'''
Project: SimJeb 
Dataset cleaning using geometrical interfaces
Autor: A. Delgadillo
Created: 11/13/2024 
'''

import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt
import trimesh as tm 
import tkinter as tk
from tkinter import filedialog 
import pandas as pd
import os
import seaborn as sns
import csv

from utils.utilities import select_directory, select_file, select_files



def compute_intersections(interfaces, part_mesh):
    # interfaces: list of paths to interface mesh files
    # part_mesh: pyvista mesh 
    intersect = False
    for interface_mesh in interfaces:
        m = pv.read(interface_mesh.name)
        intersection, s1_split, s2_split = part_mesh.intersection(m)
        if len(intersection.points)>0:
            intersect = True
    
    return intersect

def filter_data(file_list, interfaces):
     #select directory to save plots
    save_dir = select_directory()
    p_1 = pv.Plotter()
    output_list = []

    #Find intersections with the interface meshes
    for i in range(len(file_list['sur_mesh'])):
        filename = file_list['sur_mesh'][i]
        mesh_i = pv.read(filename)
        interface_intersection = compute_intersections(interfaces, mesh_i)
        if interface_intersection == False:
            p_1.add_mesh(mesh_i, opacity=0.10, show_edges=True, color=True)
            row = [i, file_list['sur_mesh'][i], file_list['vol_mesh'][i], file_list['sim_csv'][i]]
            output_list.append(row)

    #save list of files and plot
    csv_file_name = "filtered_files.csv"
    file_path = os.path.join(save_dir, csv_file_name)
    with open('filtered_output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        row = ['id', 'sur_mesh', 'vol_mesh', 'sim_csv']
        writer.writerow(row)
        # Write each row of data to the CSV file
        for row in output_list:
            writer.writerow(row)
    
    file_name = "filtered_meshes.png"
    file_path = os.path.join(save_dir, file_name)
    p_1.save_graphic(file_path)
    return True


file_list = select_file() #load file list : raw_data.csv
sim_files = pd.read_csv(file_list.name)
interface_meshes = select_files()
filter_data(sim_files, interface_meshes)