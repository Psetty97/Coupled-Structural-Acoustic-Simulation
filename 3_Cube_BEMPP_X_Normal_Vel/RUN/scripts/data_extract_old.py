import pandas as pd
import cmath
import numpy as np

# Read the data into a DataFrame
# df = pd.read_csv(r'C:\Work\BEMPP_Cube\Abaqus\RUN\cube_run_1.dat', header=None, names=['data'], sep='\n')

# Split the 'data' column into multiple columns
# df = df['data'].str.split(expand=True)

df = pd.read_fwf('C:/Work/BEMPP_Cube/Sequentially_Coupled_5/RUN/Output_Frequencies/500.00000.dat', sep='\t')
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

complex_array = np.array(complex_arr)

# Define the path where you want to save the array
output_path = 'C:/Work/BEMPP_Cube/Sequentially_Coupled_5/RUN/complex_array.npy'

# Save the array
np.save(output_path, complex_array)

