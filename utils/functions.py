"""
@Time : 2023/08/23 15:13
@Author : xli_0b101010
@File : functions.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import heapq

import numpy as np
from rdkit.Chem import DataStructs
from scipy.spatial import distance
from sklearn.preprocessing import StandardScaler


def rdkit_numpy_convert(fp):
    """
    Convert rdkit fingerprint to numpy array
    """
    output = []
    arr = np.zeros([1, ])
    DataStructs.ConvertToNumpyArray(fp, arr)
    output.append(arr)
    return np.asarray(output)


def is_in_training_set(cano_smiles, inhib_proba, train_data):
    """
    Check if the input SMILES string is in the training set, if molecule is in the training set,
    true_value will cover the inhib_proba, and add a '*' after the true_value
    """
    for i in range(len(train_data)):
        if cano_smiles == train_data['SMILES'][i]:
            true_value = str(train_data['CLASS'][i])
            return ''.join(true_value, '*')
    return inhib_proba


def is_in_applicability_domain(x_scaled, x_train_scaled, threshold):
    """
    Check if the input SMILES string is in the applicability domain

    Parameters
    ----------
    x_scaled : numpy.ndarray
        x_scaled is a 2-D array, we need a 1-D array, so usually is x_scaled[0]
    x_train_scaled : numpy.ndarray
        Scaled training set
    threshold : float
        Threshold for applicability domain

    Examples
    --------
    ad_2b6 = is_in_applicability_domain(x_2b6_scaled[0], x_train_2b6_scaled_smo, threshold=19.599)
    """
    i = 0
    dis = []
    while i < x_train_scaled.shape[0]:
        dis.append(distance.euclidean(x_scaled, x_train_scaled[i]))
        i += 1
    knn_dis = heapq.nsmallest(3, dis)
    max_dis = np.max(knn_dis)
    if max_dis > threshold:
        return 'OD'
    else:
        return 'ID'


def predict_inhib_proba(x, x_train, model):
    """
    Predict inhibition probability, x_train and model are from pkl files, 
    only need to get features(x) from SMILES string

    Parameters
    ----------
    x : numpy.ndarray
        Featurized SMILES string
    x_train : numpy.ndarray
        Training set
    model : 
        Prediction model
        
    Returns
    -------
    inhib_proba : str
        Inhibition probability
    x_scaled : numpy.ndarray
        Scaled features
    
    Examples
    --------
    inhib_proba_2b6, x_2b6_scaled = predict_inhib_proba(x_2b6, x_train_2b6, model_2b6)
    """
    
    # Scale features
    scaler = StandardScaler().fit(x_train)
    x_scaled = scaler.transform(x)
    # Model prediction
    inhib_proba = np.round(model.predict_proba(x_scaled)[:, 1], 3)
    # Convert to string
    inhib_proba = ''.join(str(i) for i in inhib_proba)
    
    return inhib_proba, x_scaled
