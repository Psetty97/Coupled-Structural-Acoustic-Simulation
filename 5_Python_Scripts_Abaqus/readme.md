# 5_Python_Scripts_Abaqus

This folder contains Python scripts for processing and formatting simulation data for **acoustic analyses using Abaqus and BEMPP**. These scripts bridge the gap between **multi-body simulation (MBS) outputs from Simpack** and downstream **FEM/BEM acoustic solvers**.

## 📄 Script Descriptions

### 1. `1_group_disp_from_simpack_based_on_frequency.py`
Groups Simpack DRF file displacement results based on frequency. This is the preprocessing step before formatting the data for Abaqus.

### 2. `2_process_simpack_drf_disp_for_abaqus_bc.py`
Processes normal displacement or velocity results from Simpack `.drf` text files and converts them into an **Abaqus input file (.inp)** compatible format.  
This allows applying MBS-derived vibration data as **boundary conditions in acoustic FEM analysis using Abaqus**.

> 🔧 Use scripts 1 & 2 together for **Abaqus-based acoustic simulation** using high-fidelity MBS outputs.

---

### 3. `3_process_velocity_from_simpack_for_bempp.py`
Extracts and formats **normal velocity** data from Simpack results for use in the **BEMPP** Python library.  
Ensures the data is structured properly for use as a **Neumann boundary condition** in BEM acoustic models.

---

### 4. `4_convert_por_from_dat_to_numpy_by_frequency.py`
Parses Abaqus `.dat` file output containing sound pressure (POR) results and converts it into **NumPy arrays**, making it easier to:
- Extract frequency-dependent results
- Plot graphs (e.g., SPL vs. frequency)
- Compare with BEMPP results

---

## 🔗 Applications

These scripts are essential for:
- Coupling **multi-body dynamics** with **acoustic FEM/BEM simulation**
- Leveraging Simpack + Abaqus/BEMPP in hybrid workflows
- Automating data preparation for high-frequency sound radiation analysis

## 🛠️ Requirements

- Python 3.x  
- `numpy`, `scipy`, `matplotlib`, `pandas`
- File I/O familiarity with `.drf`, `.inp`, `.dat` formats

---

For more context on the simulation setup and theory, refer to the [7_Master_Thesis_Report.pdf](../7_Master_Thesis_Report.pdf) in main repository.
