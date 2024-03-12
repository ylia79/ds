import numpy as np 

import pandas as pd 

from sklearn.model_selection import train_test_split 

from sklearn.tree import DecisionTreeClassifier, export_text 

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix 

from sklearn.datasets import load_iris 

iris = load_iris() 

X = iris.data 

y = (iris.target == 2).astype(int) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

model = DecisionTreeClassifier() 

model.fit(X_train, y_train) 

y_pred = model.predict(X_test) 

accuracy = accuracy_score(y_test, y_pred) 

conf_matrix = confusion_matrix(y_test, y_pred) 

classification_rep = classification_report(y_test, y_pred) 

print(f"Accuracy: {accuracy}") 

print(f"Confusion Matrix:\n{conf_matrix}") 

print(f"Classification Report:\n{classification_rep}") 

tree_rules = export_text(model, feature_names=iris.feature_names) 

print(f"Decision Rules:\n{tree_rules}") 

 
