import numpy as np
import os

# File path setup
input_file = r'C:\Work\BEMPP_Cube\Sequentially_Coupled_6\RUN\submo_4_1.dat'  # Modify this path to your actual data file location
output_folder = r'C:\Work\BEMPP_Cube\Sequentially_Coupled_6\RUN\por_from_abaqus'  # Modify this path to where you want to save the numpy files
os.makedirs(output_folder, exist_ok=True)

# Read the entire file into a list of lines
with open(input_file, 'r') as file:
    lines = file.readlines()

# Helper function to parse blocks of data
def parse_block(block):
    node_data = {}
    for line in block:
        parts = line.split()
        if len(parts) == 3 and 'SSD' in parts:  # Line with SSD (imaginary part)
            node_id, ssd, value = parts
            # Convert value to a complex number with an imaginary part
            if node_id in node_data:
                # If there's already a real part stored, add this imaginary part to it
                node_data[node_id] += 1j * float(value)
            else:
                # Otherwise, just store the imaginary part (real part might come later)
                node_data[node_id] = 1j * float(value)
        elif len(parts) == 2:  # Normal line with node data
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
            frequency_data[current_frequency] = parse_block(current_block)
            current_block = []  # Reset current block for new data
        # Extract new frequency
        current_frequency = "{:.10g}".format(float(line.split('=')[-1].strip()))
    elif "NODE" in line and "POR" in line:
        continue  # Skip header line
    elif "MAXIMUM" in line or "MINIMUM" in line:
        continue  # Skip summary lines
    else:
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
