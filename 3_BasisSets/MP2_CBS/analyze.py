import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# dictionary for organizing important data from the Psi4 outputs
info = {'name':[],'basis set':[],'wall time':[],'MP2 energy':[], 'SCF energy':[]}

# make a list of output files
outputs = [x for x in os.listdir('./inp_files/') if x.endswith('.out')]

# loop through all files and populate 'info' dictionary
mol = 'benzene'
basissets = ['DZ', 'TZ', 'QZ', '5Z']

for basisset in basissets:
    info['name'].append(mol)
    info['basis set'].append(basisset)
    with open('./inp_files/'+mol+'_'+basisset+'.out', 'r') as outfile:
        lines = outfile.readlines()
        for line in lines:
            if '"SCF TOTAL ENERGY"' in line:
                info['SCF energy'].append(float(line.split()[-1]))
            elif '"MP2 TOTAL ENERGY"' in line:
                info['MP2 energy'].append(float(line.split()[-1]))
            elif '    Psi4 wall time' in line:
                info['wall time'].append(line.split()[-1])

# convert dictionary to a dataframe/table
df = pd.DataFrame(info)
df = df.set_index('basis set')

# compute correlation energy
df['Corr. energy'] = df['MP2 energy'] - df['SCF energy']

# convert digital time format to seconds
x_secs = []
for x in df['wall time']:
    hrs = int(x.split(':')[0])
    mins = int(x.split(':')[1])
    secs = float(x.split(':')[2])
    x_sec = (hrs*3600)+(mins*60)+secs
    x_secs.append(float(x_sec))

df['seconds'] = x_secs
print(df)

# graph correlation energy as basis set size increases
#to_graph = pd.DataFrame({'Basis Set':df['basis set'].tolist(), 'Corr. Energy':df['Corr. energy'].tolist()})
#to_graph = to_graph.set_index('Basis Set')
#ax = to_graph.plot.line()
##ax.plot(x=df['basis fxns'].tolist()[::4], y=x**3)
#plt.xlabel('Basis Set')
#plt.ylabel('Correlation Energy')
#plt.savefig('fig.pdf')

# compute extrapolated correlation energy according to 
# eqn 7 in Halkier et al. (1998) DOI: 10.1016/S0009-2614(99)00179-7
DT_CBS_corr_e =
TQ_CBS_corr_e = 
print('[DT]Z:  ', DT_CBS_corr_e)
print('[TQ]Z:  ', TQ_CBS_corr_e)

