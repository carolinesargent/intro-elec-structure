## Basis Sets

Topic: 2-point extrapolation
`MP2_CBS`:
1. Create input files by running `make_inps.py`. This script will generate input files for different basis sets with MP2 and the benzene XYZ in `/XYZs`.
2. Run `analyze.py` to produce a table of energies, correlation energies, times, etc, in addition to a figure. View the figure.
3. View Halkier1998.pdf equation 7 for two point extrapolation equation. Code the equation in analyze.py and compare results to correlation energies from step 2. 
4. Create an automated Psi4 job for MP2/CBS (using the basis sets used in step 3). Make sure that your results match. 

`CCSD_T_CBS`
1. Create and run a benzene energy calculation with CCSD(T)/cc-pvtz
2. Create and run a benzene energy calculation with CCSD(T)/CBS(a[TQ]Z+d:DZ)
3. Compare results
