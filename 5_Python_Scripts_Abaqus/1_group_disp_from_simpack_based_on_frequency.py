# -----------------------------------------------------------------------------
# Author: Prashanth Setty
# Date: November 29, 2024
# Purpose:
# This script processes displacement data from a Simpack DRF file, groups the 
# data by frequency, and saves each frequency's data into a separate input file 
# in a format suitable for further processing from the script. This output can be used as input 
# to the script that formats boundary conditions for Abaqus (process_simpack_drf_disp_for_abaqus_bc.py).
# -----------------------------------------------------------------------------
import os

def process_frequency_data(input_file_path, output_directory):
    """
    Processes a Simpack DRF file to group data by frequency and save the grouped
    data into separate files.

    Parameters:
    - input_file_path (str): Path to the DRF file containing multiple frequencies 
                             and displacement data.
    - output_directory (str): Path to the directory where output files will be saved.
    """

    # Open the file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    # Initialize variables to track frequency data
    current_freq = None
    data_blocks = {}
    header = None
    collecting = False # Flag to indicate whether to start collecting data
    for line in lines:
        if "frequency=" in line:
            # Extract the frequency value and initialize a block for its data
            current_freq = line.split('=')[1].strip()  # Extract the frequency value
            data_blocks[current_freq] = []  # Initialize a list to store the data for this frequency
            collecting = False  # Reset collecting when new frequency is found
        elif "'node'," in line:
             # Clean and save the header line
            header = line.strip().replace("'", "")  # Clean header line
            data_blocks[current_freq].append(header)  # Store the cleaned header
            collecting = True  # Start collecting data
        elif collecting and line.strip() and line[0].isdigit():
            # Collect data lines that belong to the current frequency
            data_blocks[current_freq].append(line.strip())  # Append data lines to the current frequency block

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Write each frequency's data to a separate file
    for freq, data in data_blocks.items():
        # Generate output filename based on the frequency
        filename = os.path.join(output_directory, f'{freq}Hz.inp')
        with open(filename, 'w') as f:
            for row in data:
                f.write(row + '\n')  # Write each line including the header and data rows

# User-defined paths for the input DRF file and output directory
input_file_path = r'C:\Work\CavityModeling\gearbox\disp_from_simpack\disp_80_200Hz_cleaned.drf'
output_directory = r'C:\Work\CavityModeling\gearbox\disp_from_simpack\disp_grouped_based_on_freq'

process_frequency_data(input_file_path, output_directory)