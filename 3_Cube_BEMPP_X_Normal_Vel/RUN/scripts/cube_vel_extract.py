import pandas as pd
import numpy as np
import os

folder_path = r'C:\Work\BEMPP_Cube\Sequentially_Coupled_6\RUN\Output_Frequencies'
numpy_folder = os.path.join(folder_path, 'numpy_vel')

# Ensure the directory for saving .npy files exists
os.makedirs(numpy_folder, exist_ok=True)

def list_files(directory):
    # List all files and directories in the given directory
    files_and_dirs = os.listdir(directory)
    files = [file for file in files_and_dirs if os.path.isfile(os.path.join(directory, file))]
    return files 

files = list_files(folder_path)
for file in files:
    #print(os.path.join(folder_path, file))
    df = pd.read_fwf(os.path.join(folder_path, file), sep='\t')
    df.rename(columns={'Unnamed: 1': 'FOOT'}, inplace=True)

    node_val = [1,4,7]
    vel_val = ['V1', 'V2', 'V3']
    complex_arr = []

    for i, _ in enumerate(node_val):
        val = node_val[i]
        df_node = df.query("NODE//1000 == @val")

        im = df_node.query("FOOT == 'SSD'")[vel_val[i]].tolist()
        real = df_node.query("FOOT != 'SSD'")[vel_val[i]].tolist()

        for j, _ in enumerate(real):
            complex_arr.append(complex(real[j], im[j]))

    # Convert list to numpy array for saving
    complex_arr_np = np.array(complex_arr)

    # Save to .npy file
    # np.save(os.path.join(path_file, f'{file[:-4]}.npy'), complex_arr_np)

    # Construct the filename for saving the numpy array
    # Assuming the file is named with frequency at the end like 'data_500.00000.dat'
    base_filename = file.split('.')[0]  # This will remove the extension and keep only the first part
    npy_filename = f'{base_filename}.npy'
    npy_file_path = os.path.join(numpy_folder, npy_filename)

    # Save to .npy file
    np.save(npy_file_path, complex_arr_np)
    #print(f'Saved {npy_file_path}')