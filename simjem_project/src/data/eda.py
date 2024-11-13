'''
Project: SimJeb 
Exploratory Data Analisys
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
from utils import select_directory


#load file list



#create and save plots
def save_plots(meshes, csvs):
    #select directory to save plots
    save_dir = select_directory()
    
    for i in range(len(meshes)):
        #create_plots()   
        sim_data = pd.read_csv(csvs[i].name)
        filename = meshes[i].name
        mesh_i = pv.read(filename)

        plotter = pv.Plotter()
        _ = plotter.add_mesh(mesh_i, opacity=0.35)
        mesh_i['Stress GPa'] = sim_data['ver_stress']
        plotter.view_xy()
        filename = os.path.splitext(os.path.basename(filename))[0]
        file_name = str(filename) + "_lc1" ".png"
        file_path = os.path.join(save_dir, file_name)
        plotter.save_graphic(file_path)

    return True


