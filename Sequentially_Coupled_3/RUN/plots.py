import pandas as pd
import matplotlib.pyplot as plt

# Load the data from Excel
data = pd.read_excel(r'C:\Work\CavityModeling\Cube\Sequentially_Coupled_4\RUN', sheet_name='ALLQB_to_RADPOW.xlsx')

# Extract columns for plotting
frequencies = data['freq']
spw_allqb = data['SPW_ALLQB_SC * Freq']
#spw_radpow = data['SPW_RADPOW_FC']

# Print the size of each array
print("Number of elements in frequencies:", frequencies.size)
print("Number of elements in SPW(ALLQB_SC * Freq):", spw_allqb.size)
#print("Number of elements in SPW(RADPOW_FC):", spw_radpow.size)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(frequencies, spw_allqb, label='SPW_ALLQB_SC * Freq)', marker='o')
#plt.plot(frequencies, spw_radpow, label='SPW_RADPOW_FC', marker='x')
plt.title('Frequency vs SPW Values')
plt.xlabel('Frequency (Hz)')
plt.ylabel('SPW Values')
plt.legend()
plt.grid(True)
plt.show()
