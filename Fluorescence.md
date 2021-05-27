## Fluorescence Simulation

### 1 Diffusion equation in Helmholtz form (COMSOL pre-set physics setting)

The problem is divided in two steps: the excitation of the fluorescent material by the absorption of the energy of the incident photons (Equation (1)), and the spontaneous emission when it is returning to the ground state (Equation (2)). 
The diffusion equation is used to model propagating light in a medium and find its fluence value.

Equation (1):

φ<sub>x</sub>(r) - ∇ D<sub>x</sub>(r)  ∇ φ<sub>x</sub>(r) + μ<sub>ax</sub>(r)  φ<sub>x</sub>(r) = S<sub>x</sub>(r)		

φ<sub>x</sub> (r)  is the fluence rate of the propagating light in a medium, S<sub>x</sub> (r) is the source term, D<sub>x</sub> (r) is the diffusion coefficient and μ<sub>ax</sub> (r) is the absorption coefficient.

The calculated result of φ<sub>x</sub>(r) in the first step is used as initial condition (excitation light, source term) to the following step that describes the spontaneous emission defined by Equation (2)
	
Equation (2):

φ<sub>m</sub>(r) - ∇D<sub>m</sub>(r) ∇φ<sub>m</sub>(r) + μ<sub>am</sub>(r)  φ<sub>m</sub>(r) = μ<sub>af</sub> γ<sub>m</sub> φ<sub>x</sub>(r) 

where φ<sub>m</sub> (r) is the fluence rate of the emission light in a medium, μ<sub>af</sub> is the absorption coefficient at the excitation wavelength, φ<sub>x</sub> (r)  is the excitation light fluence rate obtained after solving the equation (1) and γ<sub>m</sub> is the fluorescence yield fraction. In the Equation (2) the diffusion and absorption coefficients are defined according to the material chosen to be the active medium and its source term is the fluence rate for the fluorescence emission (which will be later used as a parameter of the electromagnetic field that will be scattered by the nanoparticles to achieve the non-coherent feedback already studied experimentally)

In COMSOL Multiphysics there is a pre-set physics setting for Helmholtz equations. To make things easier we use this preset and determine the Diffusion equations (1 and 2) in their Helmholtz forms:  

∇(-c∇u)+au=f 	 

Where u = φ<sub>x</sub> , c = D, a = μ<sub>ax</sub> and f = S.

Equations 1 and 2 can be written in their Helmholtz form as

∇(-D ∇φ<sub>ex</sub>)+μ<sub>a</sub> φ<sub>ex</sub>=S 	

and

∇(-D<sup>i</sup> ∇φ<sup>i</sup><sub>em</sub>)+μ<sup>i</sup><sub>a</sub> φ<sup>i</sup><sub>em</sub>= μ<sub>a</sub><sup>ex</sup> Y<sup>i</sup>  φ<sub>ex</sub> 		
respectively.

The subscript i represents the emission wavelength, em and ex are related to the emission and excitation light sources.


### 2 Definitions / Parameters summary
 

