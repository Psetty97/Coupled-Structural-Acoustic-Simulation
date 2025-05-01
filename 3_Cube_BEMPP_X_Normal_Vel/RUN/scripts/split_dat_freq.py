import os

def parse_and_save(input_filepath):
    # Open the original .dat file
    with open(input_filepath, 'r') as file:
        content = file.readlines()
    
    data_collecting = False
    data_blocks = {}
    frequency = None
    
    for line in content:
        if "INCREMENT NUMBER" in line:
            if frequency:
                # Save the previous block if it exists
                data_blocks[frequency] = current_data
            # Start a new data block
            frequency = line.split('=')[-1].strip()
            current_data = []
            data_collecting = False
        elif "NODE FOOT-" in line:
            # Start collecting data after this line
            data_collecting = True
        elif "MAXIMUM" in line or "MINIMUM" in line:
            # Stop collecting data at MAXIMUM or MINIMUM summary
            data_collecting = False
            continue
        elif data_collecting:
            # Collect the data
            current_data.append(line)
    
    # Don't forget to save the last frequency block
    if frequency and current_data:
        data_blocks[frequency] = current_data

    # Output directory for new .dat files
    output_dir = os.path.join(os.path.dirname(input_filepath), "Output_Frequencies")
    os.makedirs(output_dir, exist_ok=True)
    
    # Write each frequency's data to a new .dat file
    for freq, data in data_blocks.items():
        output_path = os.path.join(output_dir, f"{freq}.dat")
        with open(output_path, 'w') as output_file:
            #output_file.write(f"Frequency = {freq} Hz\n")
            output_file.write("      NODE            V1             V2             V3             VR1            VR2            VR3\n")
            output_file.writelines(data)
            print(f"Data for Frequency {freq} Hz written to {output_path}")
        with open(output_path, 'r') as output_file:
            lines = output_file.readlines()
        del lines[1:3]
        with open(output_path, 'w') as output_file:
            output_file.writelines(lines)

# Path to your .dat file
input_file_path = 'C:\Work\BEMPP_Cube\Sequentially_Coupled_6\RUN\Global_4.dat'
parse_and_save(input_file_path)