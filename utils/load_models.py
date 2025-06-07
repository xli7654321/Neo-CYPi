import pandas as pd
from joblib import load

cyp_isoforms = ('All', 'CYP1A2', 'CYP2B6', 'CYP2C8', 
                'CYP2C9', 'CYP2C19', 'CYP2D6', 'CYP3A4')

models = {
    '1a2': load('models/1a2/1a2_ecfp_xgb.pkl'),
    '2b6': load('models/2b6/2b6_maccs_svm.pkl'),
    '2c8': load('models/2c8/2c8_mol2vec_svm.pkl'),
    '2c9': load('models/2c9/2c9_mol2vec_xgb.pkl'),
    '2c19': load('models/2c19/2c19_mol2vec_xgb.pkl'),
    '2d6': load('models/2d6/2d6_ecfp_xgb.pkl'),
    '3a4': load('models/3a4/3a4_mol2vec_xgb.pkl')
}

x_train = {
    '2b6': load('models/2b6/2b6_maccs_x_train.pkl'),
    '2c8': load('models/2c8/2c8_mol2vec_x_train.pkl')
}

x_train_scaled = {
    '2b6': load('models/2b6/2b6_maccs_x_train_scaled_smo.pkl'),
    '2c8': load('models/2c8/2c8_mol2vec_x_train_scaled.pkl')
}

train_data = {
    '1a2': pd.read_csv('models/1a2/1a2_training.csv'),
    '2b6': pd.read_csv('models/2b6/2b6_training.csv'),
    '2c8': pd.read_csv('models/2c8/2c8_training.csv'),
    '2c9': pd.read_csv('models/2c9/2c9_training.csv'),
    '2c19': pd.read_csv('models/2c19/2c19_training.csv'),
    '2d6': pd.read_csv('models/2d6/2d6_training.csv'),
    '3a4': pd.read_csv('models/3a4/3a4_training.csv')
}

# Applicability domain thresholds - based on euclidean distance
thresholds = {
    '1a2': 0.4,
    '2b6': 19.599,
    '2c8': 15.738,
    '2c9': 0.26,
    '2c19': 0.24,
    '2d6': 0.33,
    '3a4': 0.28
}
