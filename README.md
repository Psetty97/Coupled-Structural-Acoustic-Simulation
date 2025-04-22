# Coupled Structural–Acoustic Analysis of Exterior Noise Radiation using FEM and BEM

## 📌 Overview
This repository contains the simulation workflows, scripts, and documentation for my Master's thesis on coupled structural–acoustic analysis under free-field boundary conditions. The study compares fully coupled and sequentially coupled FEM approaches in Abaqus, and validates the Boundary Element Method (BEM) calculations in BEMPP by comparing them with Abaqus.

## 🎯 Objectives
- Compare fully coupled and sequentially coupled structural–acoustic analyses in Abaqus for a prototype cube model.
- Develop a simulation workflow for wind turbine gearbox acoustic analysis by integrating displacement data from a multibody simulation in Simpack into Abaqus for sequentially coupled acoustic calculations.
- Validate BEMPP-based acoustic calculations against Abaqus results.
- Document methodological insights and challenges for future research in computational acoustics.

## 🛠️ Tools & Technologies
- **Abaqus Standard** (FEM simulation)
- **BEMPP Library** (Boundary Element Method in Python)
- **Python Scripting** (for post-processing and automation)
- **Simpack** (for multibody simulation)

## 📂 Repository Structure

## 🖼️ Key Results
- SPL comparison between fully coupled (Abaqus) and sequentially coupled (Abaqus).
- SPL comparison between structural tie elements (Abaqus) and acoustic-structural interface elements (Abaqus).
- SPL comparison between FEM (Abaqus) and BEM (BEMPP).
- Far-field sound pressure visualisations (Abaqus).

## 📖 Summary of Findings
- Sequentially coupled analysis achieves high accuracy with approximately 50% lower computational cost compared to the fully coupled approach.
- Successfully demonstrated the integration of Simpack-generated displacement data into Abaqus for gearbox acoustic analysis, enabling better representation of 
  complex dynamics like gear meshing and bearing interactions.
- Mesh refinement based on wave number and smooth geometry affect BEM accuracy at higher frequencies.


## 👩‍💻 Author
**Prashanth Setty**  
[linkedin.com/in/prashanth-setty]  

## 📎 Citation
If you use this work, please cite:
> [Comparative Numerical Analysis of Free Field Acoustics using Finite and Boundary Element Methods, Friedrich-Alexander-University Erlangen-Nuremberg, 2025]

## 🏷️ License
This project is licensed under the MIT License. See `LICENSE` for details.
