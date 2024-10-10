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
    
        filename = mesh_f[i].name
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


mesh_f = select_files()
mesh_h = select_files()
mesh_v = select_files()
csv_list = select_files()
#sim_results = select_files()
mesh_holes = pv.read(mesh_h[0].name)
m2 = pv.read(mesh_h[1].name)
#m3 = pv.read(mesh_h[2].name)
#m4 = pv.read(mesh_h[3].name)
output_list = []
#filter and plot
p_1 = pv.Plotter()

for i in range(len(mesh_f)):
    filename = mesh_f[i].name
    print(filename)
    mesh_i = pv.read(filename)
    interface_intersection = compute_intersections(mesh_h, mesh_i)
    if interface_intersection == False:
        p_1.add_mesh(mesh_i, opacity=0.10, show_edges=True, color=True)
        row = [i, mesh_f[i].name, mesh_v[i].name, csv_list[i].name]
        output_list.append(row)
#p_1.add_mesh(mesh_holes)
#p_1.add_mesh(m2)
#p_1.add_mesh(m3)
#p_1.add_mesh(m4)
with open('filtered_output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    row = ['id', 'sur_mesh', 'vol_mesh', 'sim_csv']
    writer.writerow(row)
    # Write each row of data to the CSV file
    for row in output_list:
        writer.writerow(row)
p_1.show()

#save_plots()

''''
p_1 = pv.Plotter()
for i in range(50):
    filename = mesh_f[i].name
    mesh_i = pv.read(filename)
    p_1.add_mesh(mesh_i, opacity=0.10, show_edges=True, color=True)
p_1.show()



# Specify the directory and file name
dir_path = './my_folder'
file_name = 'my_file.txt'
file_content = 'Hello, World!'

# Ensure the directory exists
os.makedirs(dir_path, exist_ok=True)

# Save the file in the directory
with open(os.path.join(dir_path, file_name), 'w') as file:
    file.write(file_content)

    '''