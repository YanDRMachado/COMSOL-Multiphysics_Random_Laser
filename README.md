# Random Laser Simulations using COMSOL-Multiphysics 
### + OriginLab and MATLAB for data analysis / equation solving

The simulation is divided into three parts:
1. fluorescence
2. scattering
3. reincidence of scattered photons into the sample (incoherent and coherent feedback, depending on dimensions)

## 1 Fluorescence

In the first part I present a 3D model based on the Finite Element Method (FEM) to study the fluorescence phenomena through the numerical solution of Helmholtz Equations for the excitation light propagation and fluorescence emission fluence rate using COMSOL Multiphysics platform together with OriginLab (for interpolation and function fitting). 

This first problem is divided in two steps: the excitation of an arbitrary fluorescent material by the absorption of the energy from incident photons and the spontaneous emission of the material when it is returning to the ground state.
For our tests we chose to model Rhodamine 6G, a fluroescent dye derivative of xanthene. Its fluorescence has been vastly studied and I personally characterized its optical properties experimentally, making us able to compare our theoretical results to our real experiments.

To see the parameters, equations, geometry, boundary conditions, mesh and results of the fluorescence simulation **[click here](Fluorescence_Simulation_Summary.pdf)**.
