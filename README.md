# Coupled Structural–Acoustic Analysis of Exterior Noise Radiation using FEM and BEM

## 📌 Overview
This repository contains the simulation workflows, scripts, and documentation for my Master's thesis on coupled structural–acoustic analysis under free-field boundary conditions. The study compares fully coupled and sequentially coupled FEM approaches in Abaqus, and validates the Boundary Element Method (BEM) calculations in BEMPP by comparing them with Abaqus.

## 🎯 Objectives
- Compare fully coupled and sequentially coupled structural–acoustic analyses in Abaqus.
- Develop a simulation workflow for wind turbine gearbox acoustic analysis by integrating displacement data from a multibody simulation in Simpack into Abaqus for 
  sequentially coupled acoustic calculations.
- Validate BEMPP-based acoustic calculations against Abaqus results.
- Document methodological insights and challenges for future research in computational acoustics.

## 🛠️ Tools & Technologies
- **Abaqus Standard** (FEM simulation)
- **BEMPP Library** (Boundary Element Method in Python)
- **Python and MATLAB Scripting** (for post-processing and automation)
- **Simpack** (for multibody simulation)
- **Hyperworks** (for FEM modeling)

## 📖 Summary of Findings
- The sequentially coupled analysis achieves comparable accuracy while reducing computational cost by approximately 50% compared to the fully coupled approach.
- Successfully demonstrated the integration of Simpack-generated displacement data into Abaqus for gearbox acoustic analysis, enabling better representation of 
  complex dynamics like gear meshing and bearing interactions.
- Mesh refinement based on wave number and smooth geometry affects BEM accuracy at higher frequencies.
-  *Full results and plots available in the [`results/`](./results/) folder.*
  
➡️ Simulation videos are available at:  [View Simulation Videos](https://psetty97.github.io/Coupled-Structural-Acoustic-Simulation/)

## 📂 Repository Structure

- 📁 project-root/
  ├── 📁 2_Cube_Fully_coupled_Abaqus/         # Fully coupled structural-acoustic FEM model in Abaqus
  ├── 📁 3_Cube_Sequentially_Coupled_Abaqus/  # Sequential coupling setup using Abaqus
  ├── 📁 4_Cube_BEMPP_X_Normal_Vel/           # BEMPP-based acoustic solver using normal velocity from Abaqus
  ├── 📁 5_Python_Scripts_Abaqus/             # Python scripts for automation and post-processing (BEMPP, Simpack to Abaqus)
  ├── 📁 6_results/                           # SPL plots, comparison results, and validation data
  ├── 📄 1_Thesis_Presentation.pptx           # Thesis defense presentation slides
  ├── 📄 7_Master_Thesis_Report.pdf           # Final master's thesis report
  ├── 📄 LICENSE                              # License information (MIT)
  ├── 📄 README.md                            # Project overview and setup instructions
  ├── 📄 index.html                           # Web-based index for repository navigation (GitHub Pages or similar)


## 👩‍💻 Author
**Prashanth Setty**  
If you have any questions or suggestions, feel free to reach out to me on [LinkedIn Profile](https://www.linkedin.com/in/prashanth-setty)  

## 📎 Citation
If you use this work, please cite:
> [Comparative Numerical Analysis of Free Field Acoustics using Finite and Boundary Element Methods, Friedrich-Alexander-University Erlangen-Nuremberg, 2025]

## 🏷️ License
This project is licensed under the MIT License. See `LICENSE` for details.

> _“Acoustic analysis bridges the gap between structural vibrations and sound perception — enabling better designs for quieter, safer, and compliant products.”_
