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

model_2b6 = load('models/2b6_maccs_svm.pkl')
model_2c8 = load('models/2c8_mol2vec_svm.pkl')
x_train_2b6 = load('models/2b6_maccs_x_train.pkl')
x_train_2c8 = load('models/2c8_mol2vec_x_train.pkl')
x_train_2b6_scaled_smo = load('models/2b6_maccs_x_train_scaled_smo.pkl')
x_train_2c8_scaled = load('models/2c8_mol2vec_x_train_scaled.pkl')
train_data_2b6 = pd.read_csv('models/2b6_CanonicalTrainData.csv')
train_data_2c8 = pd.read_csv('models/2c8_CanonicalTrainData.csv')
