## Electron Correlation and Post-HF Methods

1. Create folder of XYZs with methane, ethane, propane, and butane XYZs. Use Avogadro to create these xyz files.
2. Run methane, ethane, propane, and butane energy calculations with increasing basis set sizes. (Use `make_inps.py` to create these input files)
3. Use `analyze.py` to tabulate and graph results.  
4. Instructor: explain density fitting
5. Run a psi4 calculation with `scf_type df` and take note of basis sets used in the calculation (relative to `scf_type pk`).
