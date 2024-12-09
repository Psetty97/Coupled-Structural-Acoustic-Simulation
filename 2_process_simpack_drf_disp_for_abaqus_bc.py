# -----------------------------------------------------------------------------
# Author: Prashanth Setty
# Date: November 29, 2024
# Purpose:
# This script processes displacement data (real and imaginary components of 
# Displacement in x, y, and z directions) obtained from the DRF file of Simpack after they are separated based on freq by the script: "group_disp_from_simpack_based_on_frequency.py". 
# The processed data is formatted as required for applying boundary conditions 
# in Abaqus. Nodes are filtered based on a cleaned mesh file provided as input.
# -----------------------------------------------------------------------------

import numpy as np
import os
import pandas as pd

def read_and_process_data(input_directory, nodes_file_path, output_directory):
    """
    Reads displacement data from the input directory, filters it based on valid nodes,
    and formats it for boundary condition input in Abaqus.

    Parameters:
    - input_directory (str): Path to the directory containing displacement data files.
    - nodes_file_path (str): Path to the file containing valid node information.
    - output_directory (str): Path to the directory where the output files will be saved.
    """

    # Read the list of nodes to be processed
    nodes_data = pd.read_fwf(nodes_file_path)

    # Extract valid nodes into a set for fast lookup
    valid_nodes = set(nodes_data['ERP_NODE'])  # Set for fast lookup
    
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.endswith('Hz.inp'):
            filepath = os.path.join(input_directory, filename)

            # Read disp data directly into DataFrame
            data = pd.read_csv(filepath)
            
            # Filter the data for nodes in the new text file
            data = data[data['node'].isin(valid_nodes)]
            
            # Convert amplitude from m/s to mm/s and phase to complex numbers
            data['Displacement X'] = data['Displacement X Amplitude'] * 1000 * np.exp(1j * data['Displacement X Phase'])
            data['Displacement Y'] = data['Displacement Y Amplitude'] * 1000 * np.exp(1j * data['Displacement Y Phase'])
            data['Displacement Z'] = data['Displacement Z Amplitude'] * 1000 * np.exp(1j * data['Displacement Z Phase'])

            # Prepare DataFrame for output
            frames = []
            for direction, label in zip(['X', 'Y', 'Z'], [1, 2, 3]):
                temp_df = pd.DataFrame({
                    'Node': data['node'],
                    'Direction1': label,
                    'Direction2': label,
                    'Real': np.real(data[f'Displacement {direction}']),
                    'Imaginary': np.imag(data[f'Displacement {direction}'])
                })
                frames.append(temp_df)

            output = pd.concat(frames, ignore_index=True)

            # Output filename
            output_filename = os.path.join(output_directory, f'bc_format_{filename}')

            # Write the real and imaginary parts to the file
            with open(output_filename, 'w') as f:
                f.write('*BOUNDARY, REAL, TYPE= Displacement\n')
                output.apply(lambda x: f.write(f"{int(x['Node'])}, {int(x['Direction1'])}, {int(x['Direction2'])}, {x['Real']:.12e}\n"), axis=1)
                
                # Write the imaginary part
                f.write('*BOUNDARY, IMAGINARY, TYPE= Displacement\n')
                output.apply(lambda x: f.write(f"{int(x['Node'])}, {int(x['Direction1'])}, {int(x['Direction2'])}, {x['Imaginary']:.12e}\n"), axis=1)

# Adjust the path to your file
input_directory = r'C:\Work\CavityModeling\gearbox\disp_from_simpack\disp_grouped_based_on_freq'
nodes_file_path = r'C:\Work\CavityModeling\gearbox\MODEL_9_DISP_ALL_FREQ_ASI\MODEL\gbx_asi_nodes.inp'  # Change this to the path of cleaned nodes file
output_directory = r'C:\Work\CavityModeling\gearbox\MODEL_9_DISP_ALL_FREQ_ASI\MODEL\disp_for_bc'
read_and_process_data(input_directory, nodes_file_path, output_directory)
