import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

info = {'name':[],'basis fxns':[],'method':[],'wall time':[],'energy':[]}

outputs = [x for x in os.listdir('./inp_files/') if x.endswith('.out')]

mols = ['methane', 'ethane', 'propane', 'butane']
methods = ['hf', 'mp2', 'ccsd', 'ccsd_t']

#Number of basis functions: 100

for mol in mols:
    for method in methods:
        info['name'].append(mol)
        info['method'].append(method)
        with open('./inp_files/'+mol+'_'+method+'.out', 'r') as outfile:
            lines = outfile.readlines()
            for line in lines:
                if 'Number of basis functions:' in line:
                    nbf = line.split()[-1]
                elif '    Psi4 wall time' in line:
                    info['wall time'].append(line.split()[-1])
                elif 'Total Energy =' in line:
                    info['energy'].append(line.split()[-1])
        info['basis fxns'].append(int(nbf))

df = pd.DataFrame(info)

x_secs = []
for x in df['wall time']:
    hrs = int(x.split(':')[0])
    mins = int(x.split(':')[1])
    secs = float(x.split(':')[2])
    x_sec = (hrs*3600)+(mins*60)+secs
    x_secs.append(float(x_sec))

df['seconds'] = x_secs
print(df)

dflines = pd.DataFrame(df['basis fxns'][::4])
#dflines['hf_line'] = dflines['basis fxns'] ** 3
#dflines['mp2_line'] = dflines['basis fxns'] ** 3
#dflines['ccsd_line'] = dflines['basis fxns'] ** 3
#dflines['ccsdt_line'] = dflines['basis fxns'] ** 3
#hf_z = np.polyfit(x = df['basis fxns'][::4], y=df['seconds'][::4], deg=4)
#hf_line = np.poly1d(hf_z)
#dflines['hf_line'] = hf_line(df['basis fxns'][::4])
#mp2_z = np.polyfit(x = df['basis fxns'][::4], y=df['seconds'][1::4], deg=5)
#mp2_line = np.poly1d(mp2_z)
#dflines['mp2_line'] = hf_line(df['basis fxns'][::4])
#ccsd_z = np.polyfit(x = df['basis fxns'][::4], y=df['seconds'][2::4], deg=6)
#ccsd_line = np.poly1d(ccsd_z)
#dflines['ccsd_line'] = hf_line(df['basis fxns'][::4])
#ccsdt_z = np.polyfit(x = df['basis fxns'][::4], y=df['seconds'][3::4], deg=7)
#ccsdt_line = np.poly1d(ccsdt_z)
#dflines['ccsdt_line'] = hf_line(df['basis fxns'][::4])
#
#to_graph = pd.DataFrame({'nbf':df['basis fxns'].tolist()[::4], 'HF':df['seconds'].tolist()[::4], 'MP2':df['seconds'].tolist()[1::4], 'CCSD':df['seconds'].tolist()[2::4], 'CCSD(T)':df['seconds'].tolist()[3::4], 'HFline':dflines['hf_line'].tolist(), 'MP2line':dflines['mp2_line'], 'CCSD line':dflines['ccsd_line'], 'CCSD(T) line':dflines['ccsdt_line']})

to_graph = pd.DataFrame({'nbf':df['basis fxns'].tolist()[::4], 'HF':df['seconds'].tolist()[::4], 'MP2':df['seconds'].tolist()[1::4], 'CCSD':df['seconds'].tolist()[2::4], 'CCSD(T)':df['seconds'].tolist()[3::4]})
to_graph = to_graph.set_index('nbf')
ax = to_graph.plot.line()
#ax.plot(x=df['basis fxns'].tolist()[::4], y=x**3)
plt.xlabel('Number of Basis Functions')
plt.ylabel('Wall Time (seconds)')
plt.savefig('fig.pdf')
