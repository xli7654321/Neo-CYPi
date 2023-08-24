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


def is_in_training_set(original_smiles, current_smiles, prediction, train_data):
    """
    Check if the input SMILES string is in the training set, if molecule is in the training set,
    new_smiles and true_value will cover the value of the original smiles and prediction

    Parameters
    ----------
    original_smiles : str
        SMILES string from rdkit.Chem.MolToSmiles()
    current_smiles : str
        SMILES string after the first check
    prediction : str
        Prediction inhibition probability from model
    train_data : DataFrame
        Training set, including two columns: SMILES and CLASS
    
    Returns
    -------
    new_smiles or current_smiles : str
        If the input SMILES string is in the training set, add a '*' before the SMILES string
    true_value or prediction : str
        If the input SMILES string is in the training set, change the prediction result to the true value

    Examples
    --------
    smiles, inhibition_proba_str_2b6 = is_in_training_set(mol, inhibition_proba_str_2b6, train_data_2b6)
    """
    for i in range(len(train_data)):
        if original_smiles == train_data['SMILES'][i]:
            new_smiles = '*' + original_smiles
            true_value = str(train_data['CLASS'][i])
            return new_smiles, true_value
    return current_smiles, prediction


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


def predict_inhibition_proba(x, x_train, model):
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
    inhibition_proba_str : str
        Inhibition probability
    x_scaled : numpy.ndarray
        Scaled features
    
    Examples
    --------
    inhibition_proba_str_2b6, x_2b6_scaled = predict_inhibition_proba(x_2b6, x_train_2b6, model_2b6)
    """
    
    # Scale features
    scaler = StandardScaler().fit(x_train)
    x_scaled = scaler.transform(x)
    
    # Model prediction
    inhibition_proba = np.round(model.predict_proba(x_scaled)[:, 1], 3)
    inhibition_proba_str = "".join(str(i) for i in inhibition_proba)
    
    return inhibition_proba_str, x_scaled
