# -----------------------------------------------------------------------------
# Author: Prashanth Setty
# Date: November 29, 2024
# Purpose:
# This script processes a manually cleaned Abaqus `.dat` file containing POR data
# grouped by frequency. It converts the POR data into complex NumPy arrays
# (real and imaginary parts) and saves them as `.npy` files for each frequency.
# The data is intended for further analysis or visualization.
#
# Note:
# Before running this script, ensure that the `.dat` file is manually cleaned:
# - Remove all unnecessary lines from the top and bottom of the file.
# - Retain only the POR tables and frequency information required for processing.
# -----------------------------------------------------------------------------

import numpy as np
import os

# File path setup
input_file = r'C:\Work\CavityModeling\gearbox\MODEL_5_STEEL_ALL_FREQ\RUN\gbx_all_freq_run_cleaned.dat'  # Modify this path to your actual data file location
output_folder = r'C:\Work\CavityModeling\gearbox\MODEL_5_STEEL_ALL_FREQ\RUN\por_based_on_freq'  # Modify this path to where you want to save the numpy files
os.makedirs(output_folder, exist_ok=True)

# Read the entire file into a list of lines
with open(input_file, 'r') as file:
    lines = file.readlines()

# Helper function to parse blocks of data
def parse_block(block):
    """
    Parses a block of lines containing POR data, converting it into a complex
    NumPy array with real and imaginary parts.

    Parameters:
    - block (list): List of lines corresponding to a single frequency's data.

    Returns:
    - np.ndarray: Complex NumPy array of POR data.
    """

    node_data = {}
    for line in block:
        parts = line.split()
        if len(parts) == 3 and parts[1] == 'SSD':  # Line with SSD (imaginary part)
            node_id, ssd, value = parts
            print(f'node_id = {node_id}')
            # Convert value to a complex number with an imaginary part
            if node_id in node_data:
                # If there's already a real part stored, add this imaginary part to it
                node_data[node_id] += 1j * float(value)
            else:
                # Otherwise, just store the imaginary part (real part might come later)
                node_data[node_id] = 1j * float(value)
        elif len(parts) == 2 and parts[0].isdigit():  # Normal line with node data
            node_id, value = parts
            # Check if node_id already has an imaginary component stored
            if node_id in node_data and isinstance(node_data[node_id], complex):
                # Combine the real part with the existing imaginary part
                node_data[node_id] = float(value) + node_data[node_id]
            else:
                # Store the value as a real number (imaginary part might come later)
                node_data[node_id] = float(value)
    return np.array(list(node_data.values()))


# Main processing loop
frequency_data = {}
current_block = []
current_frequency = None

for line in lines:
    if "INCREMENT NUMBER" in line and "FREQUENCY" in line:
        # Save previous block if exists
        if current_block and current_frequency:
            #print(current_block)
            frequency_data[current_frequency] = parse_block(current_block)
            current_block = []  # Reset current block for new data
        # Extract new frequency
        current_frequency = "{:.10g}".format(float(line.split('=')[-1].strip()))
    elif line.strip() and any(char.isdigit() for char in line):
        current_block.append(line)

# Don't forget to save the last frequency block
if current_block and current_frequency:
    frequency_data[current_frequency] = parse_block(current_block)

# Save each frequency data as a numpy file
for freq, data in frequency_data.items():
    npy_filename = f"{freq}.npy"
    npy_file_path = os.path.join(output_folder, npy_filename)
    np.save(npy_file_path, data)
    print(f"Saved {npy_file_path}")

print("All data processed and saved successfully.")
