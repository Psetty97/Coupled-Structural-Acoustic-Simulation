import pandas as pd
import numpy as np

# Load the data
file_path = r'C:\Work\BEMPP_Cube\Sequentially_Coupled_6\RUN\submo_4.dat'
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
output_path = 'C:/Work/BEMPP_Cube/Sequentially_Coupled_6/RUN/complex_array_por.npy'

# Save the array
np.save(output_path, complex_array_por)

