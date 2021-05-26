The problem is divided in two steps: the excitation of the fluorescent material by the absorption of the energy of the incident photons (Equation (1)), and the spontaneous emission when it is returning to the ground state (Equation (2)). 
The diffusion equation is used to model propagating light in a medium and find its fluence value.

Equation (1):

φ_x (r)-∇D_x (r)  ∇φ_x (r)+μ_ax (r)  φ_x (r)=S_x (r)				(1)

φ_x (r)  is the fluence rate of the propagating light in a medium, S_x (r) is the source term, D_x (r) is the diffusion coefficient and μ_ax (r) is the absorption coefficient.
The calculated result of φ_x (r) in the first step is used as initial condition (excitation light, source term) to the following step that describes the spontaneous emission defined by Equation (2)
	
Equation (2):

φ<sub>m</sub>(r) - ∇D<sub>m</sub>(r) ∇φ<sub>m</sub>(r) + μ<sub>am</sub>(r)  φ<sub>m</sub>(r) = μ<sub>af</sub> γ<sub>m</sub> φ<sub>x</sub> (r)		(2)

where φ_m (r) is the fluence rate of the emission light in a medium, μ_af is the absorption coefficient at the excitation wavelength, φ_x (r)  is the excitation light fluence rate obtained after solving the equation (1) and γ_m is the fluorescence yield fraction. In the Equation (2) the diffusion and absorption coefficients are defined according to the material chosen to be the active medium and its source term is the fluence rate for the fluorescence emission (which will be later used as a parameter of the electromagnetic field that will be scattered by the nanoparticles to achieve the non-coherent feedback already studied experimentally)

In COMSOL Multiphysics there is a pre-set physics setting for Helmholtz equations. To make things easier we use this preset and determine the Diffusion equations (1 and 2) in their Helmholtz forms (3-5):  

∇(-c ∇ u)+au=f 	 				(3)
Where u = φ_x , c = D, a = μ_ax and f = S.

Equations 1 and 2 can be written in their Helmholtz form as

∇(-D ∇φ_ex)+μ_a 〖 φ〗_ex=S 					(4)
and
∇(-D^i  ∇φ_em^i )+μ_(a )^i φ_em^i= μ_a^ex  Y^i  φ_ex 			(5)
respectively.
The subscript i represents the emission wavelength, em and ex are related to the emission and excitation light sources.

