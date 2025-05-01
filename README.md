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
- ├── 📄 thesis.pdf               # Final thesis report
- ├── 📄 presentation.pdf         # Thesis defense slide
- ├── 📄 README.md                # Project description
- ├── 📂 scripts/                 # Python scripts (BEMPP, post-processing)
- │   └── 🐍 bempp_acoustic_simulation.py
- ├── 📂 abaqus_input_files/      # Example Abaqus input (.inp) files
- ├── 📂 results/                 # Plots and simulation results (SPL comparisons, etc.)
- │   └── 🖼️ spl_comparison.png
- ├── 📂 images/                  # Diagrams, model setups, and simulation visualizations
- ├── 📄 LICENSE                  # MIT Licenses


## 👩‍💻 Author
**Prashanth Setty**  
If you have any questions or suggestions, feel free to reach out to me on [LinkedIn Profile](https://www.linkedin.com/in/prashanth-setty)  

## 📎 Citation
If you use this work, please cite:
> [Comparative Numerical Analysis of Free Field Acoustics using Finite and Boundary Element Methods, Friedrich-Alexander-University Erlangen-Nuremberg, 2025]

## 🏷️ License
This project is licensed under the MIT License. See `LICENSE` for details.

> _“Acoustic analysis bridges the gap between structural vibrations and sound perception — enabling better designs for quieter, safer, and compliant products.”_
