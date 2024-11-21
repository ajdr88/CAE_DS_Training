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

from utils.utilities import select_directory, select_file


#create and save plots of stress fields
def save_mesh_plots(meshes, csvs):
    #select directory to save plots
    save_dir = select_directory()
    
    p_1 = pv.Plotter()

    for i in range(len(meshes)):
        #create_plots()   
        sim_data = pd.read_csv(csvs[i].name)
        filename = meshes[i].name
        mesh_i = pv.read(filename)

        #load case 1
        plotter = pv.Plotter()
        _ = plotter.add_mesh(mesh_i, opacity=0.35)
        mesh_i['Stress GPa'] = sim_data['ver_stress']
        plotter.view_xy()
        filename = os.path.splitext(os.path.basename(filename))[0]
        file_name = str(filename) + "_lc1" ".png"
        file_path = os.path.join(save_dir, file_name)
        plotter.save_graphic(file_path)

        #load case 2
        plotter = pv.Plotter()
        _ = plotter.add_mesh(mesh_i, opacity=0.35)
        mesh_i['Stress GPa'] = sim_data['hor_stress']
        plotter.view_xy()
        filename = os.path.splitext(os.path.basename(filename))[0]
        file_name = str(filename) + "_lc1" ".png"
        file_path = os.path.join(save_dir, file_name)
        plotter.save_graphic(file_path)

        #load case 3
        plotter = pv.Plotter()
        _ = plotter.add_mesh(mesh_i, opacity=0.35)
        mesh_i['Stress GPa'] = sim_data['dia_stress']
        plotter.view_xy()
        filename = os.path.splitext(os.path.basename(filename))[0]
        file_name = str(filename) + "_lc1" ".png"
        file_path = os.path.join(save_dir, file_name)
        plotter.save_graphic(file_path)

        #load case 4
        plotter = pv.Plotter()
        _ = plotter.add_mesh(mesh_i, opacity=0.35)
        mesh_i['Stress GPa'] = sim_data['tor_stress']
        plotter.view_xy()
        filename = os.path.splitext(os.path.basename(filename))[0]
        file_name = str(filename) + "_lc1" ".png"
        file_path = os.path.join(save_dir, file_name)
        plotter.save_graphic(file_path)
        
        #plot all meshes
        p_1.add_mesh(mesh_i, opacity=0.10, show_edges=True, color=True)
    
    file_name = "all_meshes.png"
    file_path = os.path.join(save_dir, file_name)
    p_1.save_graphic(file_path)


    return True


def save_histograms(sur_mesh, csvs):
    #select directory to save plots
    save_dir = select_directory()

    #all load cases stresses and displacement
    ver_stress_l = np.empty(0)
    hor_stress_l = np.empty(0)
    dia_stress_l = np.empty(0)
    tor_stress_l = np.empty(0)
    ver_disp_l = np.empty(0)
    hor_disp_l = np.empty(0)
    dia_disp_l = np.empty(0)
    tor_disp_l = np.empty(0)

    for data_f in csvs:
        sim_data = pd.read_csv(data_f)
        ver_stress_l = np.append(ver_stress_l, np.array(sim_data['ver_stress']))
        hor_stress_l = np.append(hor_stress_l, np.array(sim_data['hor_stress']))
        tor_stress_l = np.append(tor_stress_l, np.array(sim_data['tor_stress']))
        dia_stress_l = np.append(dia_stress_l, np.array(sim_data['dia_stress']))
        ver_disp_l = np.append(ver_disp_l, np.array(sim_data['ver_magdisp']))
        hor_disp_l = np.append(hor_disp_l, np.array(sim_data['hor_magdisp']))
        dia_disp_l = np.append(dia_disp_l, np.array(sim_data['dia_magdisp']))
        tor_disp_l = np.append(tor_disp_l, np.array(sim_data['tor_magdisp']))
    
    file_name = "all_stresses.png"
    file_path = os.path.join(save_dir, file_name)
    id = np.linspace(0, len(ver_stress_l), len(ver_stress_l))
    plt.title('Stresses')
    plt.scatter(id, ver_stress_l, label= 'Load case 1')
    plt.scatter(id, hor_stress_l,label= 'Load case 2')
    plt.scatter(id, dia_stress_l, label= 'Load case 3')
    plt.scatter(id, tor_stress_l,label= 'Load case 4')
    plt.ylabel('Stress (GPa)')
    plt.xlabel('Part Id')
    plt.legend()
    plt.savefig(file_path)
    plt.close()
    
    file_name = "Stress_LC1.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(ver_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Stress distribution (Load case 1)')
    plt.xlabel('Stress (GPa)')
    plt.show()

    file_name = "Stress_LC2.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(hor_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Stress distribution (Load case 2)')
    plt.xlabel('Stress (GPa)')
    plt.savefig(file_path)
    plt.close()

    file_name = "Stress_LC3.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(dia_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Stress distribution (Load case 3)')
    plt.xlabel('Stress (GPa)')
    plt.savefig(file_path)
    plt.close()

    file_name = "Stress_LC4.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(tor_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Stress distribution (Load case 4)')
    plt.xlabel('Stress (GPa)')
    plt.savefig(file_path)
    plt.close()

    file_name = "Displacement_LC1.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(ver_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Displacement distribution (Load case 1)')
    plt.xlabel('Displacement (mm)')
    plt.savefig(file_path)
    plt.close()

    file_name = "Displacement_LC2.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(hor_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Displacement distribution (Load case 2)')
    plt.xlabel('Displacement (mm)')
    plt.savefig(file_path)
    plt.close()

    file_name = "Displacement_LC3.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(dia_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Displacement distribution (Load case 3)')
    plt.xlabel('Displacement (mm)')
    plt.savefig(file_path)
    plt.close()

    file_name = "Displacement_LC4.png"
    file_path = os.path.join(save_dir, file_name)
    plt.hist(tor_stress_l, log=True) #np.log(k), density=True, log=True
    plt.title('Displacement distribution (Load case 4)')
    plt.xlabel('Displacement (mm)')
    plt.savefig(file_path)
    plt.close()


    #maximum values
    ver_stress_max = []
    hor_stress_max = []
    dia_stress_max = []
    tor_stress_max = []
    ver_disp_max = []
    hor_disp_max = []
    dia_disp_max = []
    tor_disp_max = []

    for data_f in csvs:
        sim_data = pd.read_csv(data_f)
        ver_stress_max.append(sim_data['ver_stress'].max())
        hor_stress_max.append(sim_data['hor_stress'].max())
        dia_stress_max.append(sim_data['dia_stress'].max())
        tor_stress_max.append(sim_data['tor_stress'].max())
        ver_disp_max.append(sim_data['ver_magdisp'].max())
        hor_disp_max.append(sim_data['hor_magdisp'].max())
        dia_disp_max.append(sim_data['dia_magdisp'].max())
        tor_disp_max.append(sim_data['tor_magdisp'].max())

    
    file_name = "Maximum_Stress.png"
    file_path = os.path.join(save_dir, file_name)
    id = np.linspace(0, len(ver_stress_max), len(ver_stress_max))
    plt.title('Maximum stress')
    plt.scatter(id, ver_stress_max, label= 'Load case 1')
    plt.scatter(id, hor_stress_max,label= 'Load case 2')
    plt.scatter(id,dia_stress_max, label= 'Load case 3')
    plt.scatter(id, tor_stress_max,label= 'Load case 4')
    plt.ylabel('Stress (GPa)')
    plt.xlabel('Part Id')
    plt.legend()
    plt.savefig(file_path)
    plt.close()

    file_name = "Maximum_Disp.png"
    file_path = os.path.join(save_dir, file_name)
    plt.title('Maximum displacement')
    plt.scatter(id, ver_disp_max, label= 'Load case 1')
    plt.scatter(id, hor_disp_max,label= 'Load case 2')
    plt.scatter(id,dia_disp_max, label= 'Load case 3')
    plt.scatter(id, tor_disp_max,label= 'Load case 4')
    plt.ylabel('Displacement (mm)')
    plt.xlabel('Part Id')
    plt.legend()
    plt.savefig(file_path)
    plt.close()

    #plot max_stress/volume
    volume_list = []
    for part_mesh in sur_mesh:
        part_i = pv.read(part_mesh)
        part_volume = part_i.volume
        volume_list.append(part_volume)

    file_name = "Stress_Volume.png"
    file_path = os.path.join(save_dir, file_name)
    plt.title('Maximum stress')
    plt.scatter(volume_list, ver_stress_max, label= 'Load case 1')
    plt.scatter(volume_list, hor_stress_max,label= 'Load case 2')
    plt.scatter(volume_list,dia_stress_max, label= 'Load case 3')
    plt.scatter(volume_list, tor_stress_max,label= 'Load case 4')
    plt.ylabel('Stress (GPa)')
    plt.xlabel('Volume')
    plt.savefig(file_path)
    plt.close()

    return True


file_list = select_file() #load file list : raw_data.csv
sim_files = pd.read_csv(file_list.name)
mesh_plots = save_mesh_plots(sim_files['vol_mesh'], sim_files['sim_csv'])
histograms = save_histograms(sim_files['sur_mesh'], sim_files['sim_csv'])
