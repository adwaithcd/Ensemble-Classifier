import matplotlib.pyplot as plt
import numpy as np
import math

objects = ('Averaging','Stacking','Best Base Model','  Proposed')
y_pos = np.arange(len(objects))
f1 = [0.9034,0.9384,0.9034,0.9382]
low = min(f1)
high = max(f1)
colors = ['b','g','r','y']
plt.ylim([0.85,0.95])
plt.bar(y_pos, f1, align='center', alpha=0.5, color=colors, width=0.4)
plt.xticks(y_pos,objects)
plt.ylabel('F1')
plt.title('F1 Score Comparison of different Ensemble Methods')
plt.show()

objects = ('Averaging','Stacking','Best Base Model','  Proposed')
y_pos = np.arange(len(objects))
auc = [0.5366,0.5,0.537,0.502]
low = min(auc)
high = max(auc)
colors = ['b','g','r','y']
plt.ylim([0.45,0.55])
plt.bar(y_pos, auc, align='center', alpha=0.5, color=colors, width=0.4)
plt.xticks(y_pos,objects)
plt.ylabel('AUC Score')
plt.title('AUC Score Comparison of different Ensemble Methods')
plt.show()
