import MDAnalysis as mda
import matplotlib.pyplot as plt
from MDAnalysis.analysis import align
from MDAnalysis.analysis import rms
import pandas as pd
x = mda.Universe('AT3_3UIM_model1.B99990004_filt.pdb')
a = mda.Universe('outII.pdb')
align.AlignTraj(a,x,select='backbone or (resid 8 and name CB and resname ALA)',filename='aligned_AT3.II.pdb',match_atoms=True,dt=16).run()
R = rms.RMSD(a,x,select='backbone or (resid 8 and name CB and resname ALA)')
R.run()
df = pd.DataFrame(R.rmsd,columns=['Frames','Time (ns)','backbone or (resid 8 and name CB and resname ALA)'])
df.to_csv('rmsd_AT3.II.csv', index=False)
fig = df.plot(x='Frames', y=['backbone or (resid 8 and name CB and resname ALA)'],kind='hist', figsize=(20, 16), fontsize=60, color=['#781C6DFF'], edgecolor="white", legend=False)
fig.set_xlabel(r'RMSD ($\AA$)')
for item in ([fig.title, fig.xaxis.label, fig.yaxis.label] +
             fig.get_xticklabels() + fig.get_yticklabels()):
    item.set_fontsize(60)
fig.figure.savefig('rmsd_AT3.II.pdf')
