# 4_Cube_BEMPP_X_Normal_Vel

This directory contains the setup and implementation of an **acoustic simulation using the Boundary Element Method (BEM)** with the open-source Python library **BEMPP**. The model uses the same cube structure as in the [Sequentially coupled FEM simulation}(../3_Cube_Sequentially_Coupled_Abaqus) but omits the acoustic cavity mesh. Instead, it uses only the outer surface layer of the cavity, significantly reducing computational requirements.

## 📦 Folder Structure

- `MODEL/`  
  Contains the Abaqus model input files defining the vibrating cube and its external boundary mesh (`outer_infinite`) used for acoustic radiation.

- `RUN/`  
  Includes **Jupyter Notebooks** that implement BEM-based simulation using **BEMPP**. These scripts load surface velocity boundary conditions (e.g., from MBS in Simpack) and compute the resulting far-field acoustic pressure.

## 🎯 Simulation Objective

To evaluate the effectiveness of BEM-based methods in modeling exterior acoustics and validate them against Abaqus FEM simulations for sound pressure radiation.

## 🔍 Technical Highlights

- **Velocity Loading**: Surface-normal velocities were applied to only those cube faces perpendicular to the **X-axis**. Results were **comparable to Abaqus** for a wide range of frequencies in this setup.
- When extending velocity application to multiple faces (e.g., **X, Y**, and **Z**), simulation accuracy **degraded at higher frequencies**.
  - This is likely due to:
    - **Mesh resolution vs. frequency**: For higher wave numbers (frequency ↑), the mesh must be finer to satisfy the **hk ≈ constant** condition.
    - **Geometry effects**: The sharp, non-smooth cube boundaries introduced numerical errors in high-frequency cases.

## ⚙️ Tools Used

- **Python Libraries**: `bempp`, `numpy`, `scipy`, `meshio`
- **Preprocessing**: Mesh from Abaqus is exported and read using `meshio` for use in BEMPP.

## 🧠 Why BEM?

- **No need to mesh the acoustic volume**, only boundary mesh is used.
- Ideal for far-field radiation problems where computational efficiency matters.
- Flexible integration with FEM/MBS-based structural simulations.

---
🔗 For more context on the simulation setup and theory, refer to the [7_Master_Thesis_Report.pdf](../7_Master_Thesis_Report.pdf) in main repository.
