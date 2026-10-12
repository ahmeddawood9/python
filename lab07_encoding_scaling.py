"""
Encoding and Scaling Lab
File: lab07_encoding_scaling.py

Codes in this file (in order):
  1. one_hot_encode()  - manual one-hot encoding
  2. min_max()         - Min-Max normalization
  3. z_score()         - Z-score standardization
  4. mean_norm()       - Mean normalization
  5. FULL PIPELINE     - split, encode, scale, LogisticRegression, accuracy
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ---------- ONE-HOT (manual) ----------
cities = ["Islamabad", "Lahore", "Peshawar"]

def one_hot_encode(city):
    vector = [0] * len(cities)
    vector[cities.index(city)] = 1
    return vector

# ---------- ONE-HOT (pandas) ----------
# encoded = pd.get_dummies(df["City"], prefix="City", dtype=int)

# ---------- ONE-HOT (sklearn) ----------
# from sklearn.preprocessing import OneHotEncoder
# enc = OneHotEncoder(handle_unknown="ignore")
# enc.fit(X_train[["City"]])
# train_city = enc.transform(X_train[["City"]]).toarray()
# test_city  = enc.transform(X_test[["City"]]).toarray()

# ---------- THREE SCALERS (train stats only) ----------
def min_max(train, test):
    mn, mx = train.min(), train.max()
    return (train - mn) / (mx - mn), (test - mn) / (mx - mn)

def z_score(train, test):
    mu, sd = train.mean(), train.std(ddof=0)      # ddof=0 matches StandardScaler
    return (train - mu) / sd, (test - mu) / sd

def mean_norm(train, test):
    mu = train.mean()
    rng = train.max() - train.min()
    return (train - mu) / rng, (test - mu) / rng

# sklearn: fit_transform on TRAIN, transform on TEST
# from sklearn.preprocessing import MinMaxScaler, StandardScaler
# sc = StandardScaler()
# train_scaled = sc.fit_transform(X_train[["Age", "Salary"]])
# test_scaled  = sc.transform(X_test[["Age", "Salary"]])

# ---------- FULL PIPELINE ----------
data = {
    "Age": [25, 35, 28, 45, 22, 40, 30, 50, 27, 38],
    "Salary": [30000, 50000, 40000, 80000, 25000,
               70000, 45000, 90000, 35000, 60000],
    "City": ["Peshawar", "Lahore", "Islamabad", "Lahore", "Peshawar",
             "Islamabad", "Peshawar", "Lahore", "Islamabad", "Lahore"],
    "Purchased": ["No", "Yes", "Yes", "Yes", "No",
                  "Yes", "No", "Yes", "No", "Yes"],
}
df = pd.DataFrame(data)

X = df.drop("Purchased", axis=1)
y = df["Purchased"].map({"No": 0, "Yes": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

train_city = np.array([one_hot_encode(c) for c in X_train["City"]])
test_city = np.array([one_hot_encode(c) for c in X_test["City"]])

age_mean, age_std = X_train["Age"].mean(), X_train["Age"].std()
sal_mean, sal_std = X_train["Salary"].mean(), X_train["Salary"].std()

train_age = ((X_train["Age"] - age_mean) / age_std).to_numpy().reshape(-1, 1)
test_age = ((X_test["Age"] - age_mean) / age_std).to_numpy().reshape(-1, 1)
train_sal = ((X_train["Salary"] - sal_mean) / sal_std).to_numpy().reshape(-1, 1)
test_sal = ((X_test["Salary"] - sal_mean) / sal_std).to_numpy().reshape(-1, 1)

X_train_final = np.hstack([train_age, train_sal, train_city])   # (8, 5)
X_test_final = np.hstack([test_age, test_sal, test_city])       # (2, 5)

model = LogisticRegression()
model.fit(X_train_final, y_train)
y_pred = model.predict(X_test_final)
print(accuracy_score(y_test, y_pred))
