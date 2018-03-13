import matplotlib.pyplot as plt
import numpy as np

objects = ('AdaBoost','Logistic','XGBoost','Random Forest')
y_pos = np.arange(len(objects))
auc = [0.512850115938,0.540661626944,0.50137641344,0.502893432018]
colors = ['b','g','r','y']

plt.bar(y_pos, auc, align='center', alpha=0.5, color=colors, width=0.4)
plt.xticks(y_pos,objects)
plt.ylabel('AUC')
plt.title('Comparison of Single Model Best Performance (RBP) using AUC')
plt.show()

objects = ('AdaBoost','Logistic','XGBoost','Random Forest')
y_pos = np.arange(len(objects))
f1 = [0.896631529814,0.903146757945,0.937667742814,0.895386829515]
colors = ['b','g','r','y']

plt.bar(y_pos, f1, align='center', alpha=0.5, color=colors, width=0.4)
plt.xticks(y_pos,objects)
plt.ylabel('F1 Score')
plt.title('Compaarison of Single Model Best Performance (RBP) using F1 Score')
plt.show()
