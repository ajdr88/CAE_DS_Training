'''
Project: SimJeb 
Feature extraction using voxelized design space
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

#Bounding box for voxels
box = select_files()
mesh_b = pv.read(box[0].name)
voxels = pv.voxelize(mesh_b, density=10)

#open filtered list of meshes and simulation results  
filtered_files = select_file()
sim_files = pd.read_csv(filtered_files.name)

# extract sim results list
sim_results_list = sim_files['sim_csv']

#ranges for bins
r_x = (-4.670e+01, 7.330e+01)
r_y = (-1.800e+02, 2.000e+01)
r_z = (3.563e+00, 6.644e+01)

bin_count=[]
stress_average = []
for i in range(len(sim_results_list)):
    sim_output = pd.read_csv(sim_results_list[i])
    X = sim_output['x']
    Y = sim_output['y']
    Z = sim_output['z']
    h_stress = sim_output['hor_stress']
    #  Weights are normalized to 1 if density is True. If density is False, the values of the returned histogram are equal to the sum of the weights belonging to the samples falling into each bin.
    H, edges = np.histogramdd((X, Y, Z), bins = (20, 12, 7), range=(r_x, r_y, r_z), weights = h_stress, density = False)
    # histogram returns the number of samples per bin / voxel
    H_2, edges_2 = np.histogramdd((X, Y, Z), range=(r_x, r_y, r_z), bins = (20, 12, 7))
    stress_sum = H.flatten()
    node_count = H_2.flatten()
    average_values = np.zeros(len(stress_sum))
    for j in range(len(average_values)):
        if node_count[j] >0:
            average_values[j]=stress_sum[j]/node_count[j]
    bin_count.append([node_count])
    stress_average.append(np.max(average_values))

data = [np.transpose(bin_count), stress_average]
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['NodeCount', 'Stress'])

df.to_csv('TrainingsSet1.csv', index=True)