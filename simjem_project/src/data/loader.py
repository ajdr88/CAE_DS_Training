'''
Project: SimJeb 
Data loader: reads input files from Raw Data directoy
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


def select_files():
    # manually select files with a pop-up window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    files = filedialog.askopenfiles()
    return files

#select surface meshes
mesh_s = select_files()

#select volumetric meshes
mesh_v = select_files()

#select csv simulation results
sim_list = select_files()

#save selected data into a csv file 
with open('raw_data.csv', mode='w', newline='') as file:
    ###Should be stored in the artifacts folder
    writer = csv.writer(file)
    row = ['id', 'sur_mesh', 'vol_mesh', 'sim_csv']
    writer.writerow(row)
    # Write each row of data to the CSV file
    for i in range(len(mesh_s)):
        row = row = [i, mesh_s[i].name, mesh_v[i].name, sim_list[i].name]
        writer.writerow(row)
