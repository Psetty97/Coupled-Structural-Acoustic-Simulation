import pandas as pd
import numpy as np

# Load the data
file_path = r'C:\Work\CavityModeling\gearbox\MODEL_5_STEEL_ALL_FREQ\RUN\por_90.dat'
df = pd.read_fwf(file_path)
df.rename(columns={'Unnamed: 1': 'FOOT'}, inplace=True)

# Ensure all entries in 'FOOT' are treated as strings
df['FOOT'] = df['FOOT'].astype(str)

# Using query to separate real and imaginary parts
real_parts = df.query("FOOT != 'SSD'")['POR'].tolist()
imag_parts = df.query("FOOT == 'SSD'")['POR'].tolist()

# Convert lists to NumPy arrays
real_array = np.array(real_parts)
imag_array = np.array(imag_parts)

# Ensure both arrays are of the same length
if len(real_array) != len(imag_array):
    raise ValueError("Mismatch in the number of real and imaginary parts.")

# Combine into a complex array
complex_array_por = real_array + 1j * imag_array

# Print or process the complex array as needed
print(complex_array_por[50])

# Define the path where you want to save the array
output_path = r'C:\Work\CavityModeling\gearbox\MODEL_5_STEEL_ALL_FREQ\RUN\SCRIPTS/complex_abaqus_array_por_90.npy'

# Save the array
np.save(output_path, complex_array_por)

