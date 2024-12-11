# Data Folder

This folder contains the dataset used for the Network Security Attack Classification project.

## Dataset Overview

The dataset used in this project is the "CICIDS2017" dataset, which contains network traffic data collected from various attacks and benign traffic. The dataset includes features that describe the network packets and a label indicating whether the traffic is benign or represents a specific type of attack.

## Source

- [CICIDS2017 Dataset on Kaggle](https://www.kaggle.com/datasets/kk0105/cicids2017)

## Data Format

The main dataset file is `week_filtered_cicids.csv`, which contains the following columns:

- **Source IP**: The IP address of the source.
- **Destination IP**: The IP address of the destination.
- **Protocol**: The protocol used (e.g., TCP, UDP).
- **Duration**: The duration of the connection.
- **Bytes Sent**: The number of bytes sent from the source to the destination.
- **Bytes Received**: The number of bytes received from the destination to the source.
- **Label**: The classification label indicating whether the traffic is benign or an attack (e.g., DoS, DDoS, etc.).

## Preprocessing Steps

Before using the dataset, the following preprocessing steps should be applied:

1. **Handling Missing Values**: Remove or impute any missing values in the dataset.
2. **Encoding Categorical Variables**: Convert categorical variables (e.g., protocol) into numerical format using techniques like one-hot encoding or label encoding.
3. **Feature Scaling**: Scale numerical features to ensure they are on a similar scale, which can improve model performance.

## Usage

To load the dataset in your scripts, use the following code snippet:

```python
import pandas as pd

data = pd.read_csv('data/week_filtered_cicids.csv')
