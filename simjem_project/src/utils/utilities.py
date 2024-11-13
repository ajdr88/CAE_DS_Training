import numpy as np
import pyvista as pv
import matplotlib as mpl
import trimesh
import tkinter as tk
from tkinter import filedialog 
import pandas as pd
import os
import csv

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    mesh_file = filedialog.askopenfile()
    return mesh_file
def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    mesh_file = filedialog.askopenfiles()
    return mesh_file
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    dir_path = filedialog.askdirectory()  # Open the directory selection dialog
    return dir_path

def plot_all(meshes):
    p = pv.Plotter()
    for i in range(len(meshes)):
    
        filename = meshes[i].name
        mesh_i = pv.read(filename)
        p.add_mesh(mesh_i, opacity=0.10, color=True)
    p.show()

def create_plots(mesh, sim_results, output_dir):
    return True

def view_max_values(file_list):
    ver_stress_max = []
    hor_stress_max = []
    dia_stress_max = []
    tor_stress_max = []
    ver_disp_max = []
    hor_disp_max = []
    dia_disp_max = []
    tor_disp_max = []

    for data_f in file_list:
        sim_data = pd.read_csv(data_f.name)
        ver_stress_max.append(sim_data['ver_stress'].max())
        hor_stress_max.append(sim_data['hor_stress'].max())
        dia_stress_max.append(sim_data['dia_stress'].max())
        tor_stress_max.append(sim_data['tor_stress'].max())
        ver_disp_max.append(sim_data['ver_magdisp'].max())
        hor_disp_max.append(sim_data['hor_magdisp'].max())
        dia_disp_max.append(sim_data['dia_magdisp'].max())
        tor_disp_max.append(sim_data['tor_magdisp'].max())
    
    return True
    

def save_plots(meshes, csvs):
    save_dir = select_directory()
    #view_max_values(csvs)
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
        file_name = str(filename) + ".svg"
        file_path = os.path.join(save_dir, file_name)
        plotter.save_graphic(file_path)

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

def compute_voxel_intersections(surface_mesh, voxel_grid):
    n = voxel_grid.n_cells
    cell_percentage = np.zeros(n) 

    volume_0 = voxel_grid.extract_cells(0).extract_surface().triangulate().volume
    
    for i in range(n):
        intersection = voxel_grid.extract_cells(i).extract_surface().triangulate().boolean_intersection(surface_mesh)
        if len(intersection.points)>0:
            cell_vol = intersection.volume/volume_0
            if cell_vol > 1:
                cell_vol = cell_vol/np.ceil(cell_vol)
            cell_percentage[i] = cell_vol
    
    return cell_percentage

