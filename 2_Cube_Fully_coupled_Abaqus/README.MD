# 📁 Fully Coupled Structural-Acoustic Simulation – Abaqus

This folder contains files for a fully coupled structural-acoustic simulation of a cube prototype using **Abaqus**. The setup demonstrates the use of acoustic-structural coupling through direct steady-state dynamics (SSD) analysis.

---

## 📂 Folder Structure

### `MODEL/`
- Contains Abaqus `.inp` files:
  - Structural model of a prototype cube
  - Acoustic cavity around the structure
  - Includes mesh, material definitions, and coupling interfaces

### `RUN/`
- Contains:
  - Input file to run the **direct SSD simulation**
  - Output files: 
    - `.dat` – text summary of analysis results  
    - `.odb` – binary file for visualization in Abaqus/CAE
---

## 📌 Key Notes
- This simulation uses *fully coupled acoustic-structural interaction*.
- Run files are structured for direct use in **Abaqus/Standard**.
- Suitable for analyzing sound pressure levels in vibro-acoustic studies.

---

For more context on the simulation setup and theory, refer to the [7_Master_Thesis_Report.pdf](../7_Master_Thesis_Report.pdf) in main repository.
