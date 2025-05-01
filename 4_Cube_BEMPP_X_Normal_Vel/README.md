# 4_Cube_BEMPP_X_Normal_Vel

This directory contains the setup and implementation of a **Boundary Element Method (BEM)** based acoustic simulation using **BEMPP** in Python. Unlike the FEM-based fully coupled model, this simulation considers only the **outer infinite boundary** (outer layer of the cavity), significantly reducing the degrees of freedom and computational cost.

## 📦 Folder Structure

- `MODEL/`  
  Contains the Abaqus model input files defining the cube structure and its outer boundary (`outer_infinite`). The cavity volume is not modeled explicitly as the BEM formulation does not require meshing the acoustic domain.

- `RUN/`  
  Contains **Jupyter Notebook files** implementing the acoustic BEM simulation using **BEMPP**. These notebooks import velocity boundary conditions (e.g., from a previous MBS simulation) and solve the Helmholtz problem on the defined outer surface.

## 💡 Objective

To demonstrate the use of open-source BEM tools (BEMPP) as a cost-efficient alternative to commercial FEM-based acoustic solvers. This model uses **normal surface velocity** as boundary input to compute the radiated sound pressure field around the vibrating structure.

## 🧠 Key Concepts

- **BEM over FEM**: Only the boundary is discretized, making it computationally lighter for exterior acoustic problems.
- **Normal Velocity as Input**: The boundary condition is extracted from structural simulation and applied to the BEM model.
- **BEMPP in Python**: Leverages the flexibility and efficiency of Python with boundary element formulations.

## 📝 Notes

- Make sure the Python environment includes `bempp`, `numpy`, `scipy`, and `meshio`.
- This model complements the FEM-based fully coupled model by validating results and highlighting computational efficiency.

---

🔗 For more context on the simulation setup and theory, refer to the [7_Master_Thesis_Report.pdf](../7_Master_Thesis_Report.pdf) in main repository.
