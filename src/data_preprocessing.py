import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import logging

def load_data(file_path):
    logging.info("Loading data from {}".format(file_path))
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    logging.info("Preprocessing data")
    data.dropna(inplace=True)
    data['Label'] = pd.Categorical(data['Label']).codes
    X = data.drop('Label', axis=1)
    y = data['Label']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def scale_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled
