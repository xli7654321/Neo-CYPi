"""
@Time : 2023/08/23 14:28
@Author : xli_0b101010
@File : load_models.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import pandas as pd
from joblib import load

cyp_isoforms = ("All", "CYP1A2", "CYP2B6", "CYP2C8", "CYP2C9", "CYP2C19", "CYP2D6", "CYP3A4")

models = {
    '2b6': load('models/2b6_maccs_svm.pkl'),
    '2c8': load('models/2c8_mol2vec_svm.pkl')
}

x_train = {
    '2b6': load('models/2b6_maccs_x_train.pkl'),
    '2c8': load('models/2c8_mol2vec_x_train.pkl')
}

x_train_scaled = {
    '2b6': load('models/2b6_maccs_x_train_scaled_smo.pkl'),
    '2c8': load('models/2c8_mol2vec_x_train_scaled.pkl')
}

train_data = {
    '2b6': pd.read_csv('models/2b6_CanonicalTrainData.csv'),
    '2c8': pd.read_csv('models/2c8_CanonicalTrainData.csv')
}

# Applicability domain thresholds - based on euclidean distance
thresholds = {
    '2b6': 19.599,
    '2c8': 15.738
}
