import matplotlib.pyplot as plt
import numpy as np
import math

objects = ('RMSD','ZOL','Best Performance','    Hierarchical Clustering')
y_pos = np.arange(len(objects))
f1 = [0.9364,0.9361,0.9286,0.9365]
low = min(f1)
high = max(f1)
colors = ['b','g','r','y']
plt.ylim([0.9,1])
plt.bar(y_pos, f1, align='center', alpha=0.5, color=colors, width=0.4)
plt.xticks(y_pos,objects)
plt.ylabel('F1')
plt.title('F1 Scores using different Diversity Measures')
plt.show()

objects = ('RMSD','ZOL','Best Performance','    Hierarchical Clustering')
y_pos = np.arange(len(objects))
auc = [0.5018,0.5010,0.5053,0.5013]
low = min(auc)
high = max(auc)
colors = ['b','g','r','y']
plt.ylim([0.49,0.51])
plt.bar(y_pos, auc, align='center', alpha=0.5, color=colors, width=0.4)
plt.xticks(y_pos,objects)
plt.ylabel('AUC Score')
plt.title('AUC Scores using different diversity measures')
plt.show()
