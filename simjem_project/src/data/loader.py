'''
Project: SimJeb 
Data loader: reads input files from Raw Data directoy
Autor: A. Delgadillo
Created: 11/13/2024 
'''

import tkinter as tk
from tkinter import filedialog 
import pandas as pd
import os
import seaborn as sns
import csv
from utils.utilities import select_directory, select_files


#select surface meshes
mesh_s = select_files()

#select volumetric meshes
mesh_v = select_files()

#select csv simulation results
sim_list = select_files()

#select where to save the raw_data file
save_dir = select_directory()
output_file = os.path.join(save_dir, 'TrainingsSet1.csv')

#save selected data into a csv file 
with open(output_file, mode='w', newline='') as file:
    ###Should be stored in the artifacts folder
    writer = csv.writer(file)
    row = ['id', 'sur_mesh', 'vol_mesh', 'sim_csv']
    writer.writerow(row)
    # Write each row of data to the CSV file
    for i in range(len(mesh_s)):
        row = row = [i, mesh_s[i].name, mesh_v[i].name, sim_list[i].name]
        writer.writerow(row)
