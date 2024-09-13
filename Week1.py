import numpy as np
import pyvista as pv
import matplotlib as mpl
import trimesh
import tkinter as tk
from tkinter import filedialog 

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

mesh_f = select_files()

p = pv.Plotter()

for i in range(len(mesh_f)):
    
    filename = mesh_f[i].name
    mesh_i = pv.read(filename)
    p.add_mesh(mesh_i, opacity=0.10, color=True)
p.show()

p_1 = pv.Plotter()
for i in range(50):
    filename = mesh_f[i].name
    mesh_i = pv.read(filename)
    p_1.add_mesh(mesh_i, opacity=0.10, show_edges=True, color=True)
p_1.show()