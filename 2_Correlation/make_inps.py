# makes input files from xyzs
import os
import numpy as np

# directory of xyzs
ROOT = '/theoryfs2/ds/csargent/psi4education/intro-elec-str/2_postHF/XYZs/'
XYZs = os.listdir(ROOT)

# directory to write input files to
WROOT = '/theoryfs2/ds/csargent/psi4education/intro-elec-str/2_postHF/inp_files/'

# change this depending on preferences
methods = ['hf','mp2','ccsd','ccsd(t)']
basis_set = 'aug-cc-pvdz'
cores = 1

labels = {'hf':'hf', 'mp2':'mp2', 'ccsd':'ccsd','ccsd(t)':'ccsd_t'}

# writing input files
for xyz in XYZs:
    with open(ROOT+xyz, 'r') as xyzfile:
        xyzlines = xyzfile.readlines()[2:]
        for method in methods:
            inp_filename = xyz[:-4]+'_'+f'{labels[method]}'
            with open(WROOT+inp_filename+'.in', 'w') as inpfile:
                inpfile.write("""
memory 10 GB
molecule mol {\n0 1\n
""" + ''.join(xyzlines) +
"""\n""" +
"""units angstrom
symmetry c1
}\n
set {
basis """ + basis_set +'\n'+
"""freeze_core true
scf_type pk
mp2_type conv
cc_type conv
}\n
energy('"""+method+"""')
""")

# make bash script to run all files and name timer.dat to molecule.time

all_filenames = os.listdir(WROOT)

with open(WROOT+'run_all.cmd', 'w') as runscript:
    runscript.write('#!/bin/bash\n\n')
    for dimer in all_filenames:
        dimer_id = dimer[:-3]
        runscript.write(f'psi4 -n{cores} {dimer_id}.in\n')
        runscript.write(f'mv timer.dat {dimer_id}.time\n\n')

