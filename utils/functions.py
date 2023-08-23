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

from load_models import x_train_2b6_scaled_smo, x_train_2c8_scaled


def rdkit_numpy_convert(fp):
    """
    Convert rdkit fingerprint to numpy array
    """
    output = []
    arr = np.zeros([1, ])
    DataStructs.ConvertToNumpyArray(fp, arr)
    output.append(arr)
    return np.asarray(output)


def is_in_training_set(smiles, prediction, train_data):
    """
    Check if the input SMILES string is in the training set

    Parameters
    ----------
    smiles : str
        Input SMILES string
    prediction : str
        Prediction result from model
    train_data : DataFrame
        Training set
    
    Returns
    -------
    smiles : str
        If the input SMILES string is in the training set, add a '*' before the SMILES string
    prediction : str
        If the input SMILES string is in the training set, change the prediction result to the true value

    Examples
    --------
    smiles, prediction = is_in_training_set(smiles, prediction, train_data_2b6)
    """
    for i in range(len(train_data)):
        if smiles == train_data['SMILES'][i]:
            smiles = '*' + smiles
            prediction = str(train_data['CLASS'][i])
            return smiles, prediction
    return smiles, prediction


def is_in_applicability_domain(x_scaled, type):
    """
    Check if the input SMILES string is in the applicability domain

    Examples
    --------
    AD_2b6 = is_in_applicability_domain(x_scaled, '2b6')
    """
    datasets = {
        '2b6': {
            'data': x_train_2b6_scaled_smo,
            'threshold': 19.599
        },
        '2c8': {
            'data': x_train_2c8_scaled,
            'threshold': 15.738
        }
    }

    dataset = datasets.get(type)  # 获取与指定键相对应的值
    if dataset is None:
        raise ValueError(f"Invalid type: {type}")

    i = 0
    dis = []
    while i < dataset['data'].shape[0]:
        dis.append(distance.euclidean(x_scaled, dataset['data'][i]))
        i += 1
    knn_dis = heapq.nsmallest(3, dis)
    max_dis = np.max(knn_dis)
    if max_dis > dataset['threshold']:
        return 'OD'
    else:
        return 'ID'
