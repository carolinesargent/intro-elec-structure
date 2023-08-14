import matplotlib.pyplot as plt
import os
import sys

f = open('RHF/RHF.out', 'r')
flines = f.readlines()
rhfdata = flines[-14:-5]

uf = open('UHF/UHF.out', 'r')
uflines = uf.readlines()
uhfdata = uflines[-14:-5]

ccsdf = open('CCSD/CCSD.out', 'r')
ccsdlines = ccsdf.readlines()
ccsddata = ccsdlines[-14:-5]

Rvals = []
rhfe = []
uhfe = []
ccsde = []

for d in rhfdata:
    splitdata = d.split()
    Rvals.append(float(splitdata[0]))
    rhfe.append(float(splitdata[1]))

for d in uhfdata:
    splitdata = d.split()
    uhfe.append(float(splitdata[1]))

for d in ccsddata:
    splitdata = d.split()
    ccsde.append(float(splitdata[1]))

plt.plot(Rvals, rhfe, color='royalblue', label='RHF')
plt.plot(Rvals, uhfe, color='green', label='UHF')
plt.plot(Rvals, ccsde, color='black', label='CCSD')
plt.legend()
plt.xlabel('Bond Length in Angstroms')
plt.ylabel('Energy in Hartrees')
plt.savefig('H2_PES.pdf')

