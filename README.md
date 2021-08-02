# Random Laser Simulations using COMSOL-Multiphysics 
## + OriginLab and MATLAB for data analysis / equation solving
### To see a description of all the files in this repository, **[click here](Fluorescence_Simulation_Summary.pdf)**


The simulation is divided into three parts:
1. fluorescence
2. scattering
3. reincidence of scattered photons into the sample (incoherent / coherent feedback, depending on dimensions)

## 1 Fluorescence

In the first part I present a 3D model based on the Finite Element Method (FEM) to study the fluorescence phenomena through the numerical solution of Helmholtz Equations for the excitation light propagation and fluorescence emission fluence rate using COMSOL Multiphysics platform together with OriginLab (for interpolation and function fitting). 

This first problem is divided in two steps: the excitation of an arbitrary fluorescent material by the absorption of the energy from incident photons and the spontaneous emission of the material when it is returning to the ground state.
For our tests we chose to model Rhodamine 6G, a fluroescent dye derivative of xanthene. Its fluorescence has been vastly studied and I personally characterized its optical properties experimentally, making us able to compare our theoretical results to our real experiments.

To see the parameters, equations, geometry, boundary conditions, mesh and results of the fluorescence simulation **[click here](Fluorescence_Simulation_Summary.pdf)**.

## 2 Scattering

As expected, Maxwell's equations are the basis of our theoretical and computational methods to describe light scattering. We will usually work with spheres for which the analytical solutions are known and calculated in terms of infinite series in COMSOL.
The relative size of the scattering particle is defined by its size parameter x, which is the radio of its characteristic dimension to its wavelength. 

x = 2 * Pi * r / lambda

For particles much smaller than the wavelength of the light (x << 1), COMSOL will solve our Maxwell eqs. according to Rayleigh scattering regimes.

For any spherical particles with any other arbitrary sizes (specially in the same dimension of the wavelength) we will be using Lorentz-Mie solutions. 

More complex shapes such as coated spheres, multispheres, spheroids, and infinite cylinders there are extensions which express the solution in terms of infinite series.
