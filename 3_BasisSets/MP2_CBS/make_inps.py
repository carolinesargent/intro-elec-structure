# makes input files from xyzs
import os
import numpy as np

# directory of xyzs
ROOT = './XYZs/'
XYZs = os.listdir(ROOT)

# directory to write input files to
WROOT = './inp_files/'

# change this depending on preferences
method = 'mp2'
basis_sets = ['cc-pvdz', 'cc-pvtz', 'cc-pvqz','cc-pv5z']
cores = 6

labels = {'hf':'hf', 'mp2':'mp2', 'ccsd':'ccsd','ccsd(t)':'ccsd_t', 'cc-pvdz':'DZ','cc-pvtz':'TZ', 'cc-pvqz':'QZ','cc-pv5z':'5Z','cc-pv6z':'6Z'}

# writing input files
for xyz in XYZs:
    with open(ROOT+xyz, 'r') as xyzfile:
        xyzlines = xyzfile.readlines()[2:]
        for basis_set in basis_sets:
            inp_filename = xyz[:-4]+'_'+f'{labels[basis_set]}'
            with open(WROOT+inp_filename+'.in', 'w') as inpfile:
                inpfile.write("""
memory 60 GB
molecule mol {\n0 1\n
""" + ''.join(xyzlines) +
"""\n""" +
"""units=au
symmetry c1
}\n
set {
basis """ + basis_set +'\n'+
"""freeze_core true
scf_type df
mp2_type df
}\n
energy('"""+method+"""')\n
print_variables()
""")

# make bash script to run all files and name timer.dat to molecule.time

all_filenames = [x for x in os.listdir(WROOT) if '.in' in x]

with open(WROOT+'run_all.cmd', 'w') as runscript:
    runscript.write('#!/bin/bash\n\n')
    for dimer in all_filenames:
        dimer_id = dimer[:-3]
        runscript.write(f'psi4 -n{cores} {dimer_id}.in\n')
        runscript.write(f'mv timer.dat {dimer_id}.time\n\n')

