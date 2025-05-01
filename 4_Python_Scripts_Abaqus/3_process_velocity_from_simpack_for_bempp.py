# -----------------------------------------------------------------------------
# Author: Prashanth Setty
# Date: November 29, 2024
# Purpose:
# This script processes velocity data from the output of the script 
# 'group_disp_from_simpack_based_on_frequency.py'. It filters nodes based on a 
# cleaned nodes file, computes surface normal velocities in a complex format, 
# and saves the data as NumPy `.npy` files. The output is prepared specifically 
# for use in BEMPP simulations.
# -----------------------------------------------------------------------------
import pandas as pd
import numpy as np
import os

def read_and_process_data(input_directory, nodes_file_path,output_directory):
    """
    Processes velocity data grouped by frequency, filters valid nodes,
    computes complex surface normal velocities, and saves them as NumPy arrays.

    Parameters:
    - input_directory (str): Path to the directory containing velocity data grouped 
                             by frequency (output of the grouping script).
    - nodes_file_path (str): Path to the file containing filtered nodes.
    - output_directory (str): Path to the directory where the output files will be saved.
    """

    # Read the list of nodes to be processed
    nodes_data = pd.read_fwf(nodes_file_path)

    valid_nodes = set(nodes_data['ERP_NODE'])  # Set for fast lookup
    nodes_output_path = os.path.join(output_directory, 'valid_vel_nodes.txt')
    
    for filename in os.listdir(input_directory):
        if filename.endswith('Hz.inp'):
            filepath = os.path.join(input_directory, filename)

            # Read velocity data directly into DataFrame
            vel_data = pd.read_csv(filepath)
            
            # Filter the data for nodes in the new text file
            vel_data = vel_data[vel_data['node'].isin(valid_nodes)]

            # Task 2: Save nodes and complex surface normal velocity
            vel_data[['node']].to_csv(nodes_output_path, index=False, header=True)
            
            # Convert amplitude from m/s to mm/s and phase to complex numbers
            vel_data['Surface normal velocity'] = vel_data['Surface normal velocity Amplitude'] * 1000 * np.exp(1j * vel_data['Surface normal velocity Phase'])

            # Task 3: Convert Surface normal velocity to a NumPy array and store it
            surface_normal_velocity_array = vel_data['Surface normal velocity'].to_numpy()

            # Save the NumPy array to a .npy file
            np.save(fr'C:\Work\BEMPP_Gearbox\MODEL_5_STEEL_ALL_FREQ\MODEL\normal_velocity\nodal_normal_velocity_{filename}.npy', surface_normal_velocity_array)

# Adjust the path to your file
input_directory = r'C:\Work\CavityModeling\gearbox\velocity_from_simpack\vel_grouped_based_on_freq'
nodes_file_path = r'C:\Work\BEMPP_Gearbox\MODEL_5_STEEL_ALL_FREQ\MODEL\hm\gbx_erp_asi_cleaned_nodes.inp'  # Change this to the path of cleaned nodes file
output_directory = r'C:\Work\CavityModeling\gearbox\SCRIPTS\temp'
read_and_process_data(input_directory, nodes_file_path,output_directory)
