import numpy as np
import math
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier

def train_meta(classifiers_map,train_features,train_re_labels,base_classifiers,test_features,test_labels):

    ls = []
    for i in range(len(base_classifiers)):
        ls.append((classifiers_map[base_classifiers[i]].predict_proba(train_features))[:,1])
    new_train_features = np.array(ls).transpose()
    clf_meta_model = LogisticRegression()
    clf_meta_model.fit(new_train_features,train_re_labels)
    ls = []
    for i in range(len(base_classifiers)):
        ls.append((classifiers_map[base_classifiers[i]].predict_proba(test_features))[:,1])
    new_test_features = np.array(ls).transpose()

    final_list = list(clf_meta_model.predict(new_test_features))
    return final_list
