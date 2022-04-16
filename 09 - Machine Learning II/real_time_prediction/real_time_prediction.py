import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pickle
import os
import time

bucket_dir = "bucket/"
local_dir = "local/"
model_path = "./ariline_passanger_satisfaction_model_ann.pickle"
preprocess_dict_path = "./preprocess.pickle"


def preprocess(X_):

  X = X_.copy()

  ## Load_data
  preprocess_dict = pickle.load(open(preprocess_dict_path,"rb"))
  sc = preprocess_dict["sc"]
  pca1 = preprocess_dict["pca1"]
  pca2 = preprocess_dict["pca2"]
  
  numerical_cols = ['Age',
    'Flight Distance',
    'Inflight wifi service',
    'Departure/Arrival time convenient',
    'Ease of Online booking',
    'Gate location',
    'Food and drink',
    'Online boarding',
    'Seat comfort',
    'Inflight entertainment',
    'On-board service',
    'Leg room service',
    'Baggage handling',
    'Checkin service',
    'Inflight service',
    'Cleanliness',
    'Departure Delay in Minutes',
    'Arrival Delay in Minutes']

  # Drop NaN
  X.dropna(axis=0, inplace=True)

  #Scaling the data
  X[numerical_cols] = sc.transform(X[numerical_cols])

  #Using PCA to reduce the dimensions of highly correlated features
  X['PCA1'] = pca1.transform(X[['Inflight wifi service', 'Ease of Online booking']])
  X['PCA2'] = pca2.transform(X[['Cleanliness', 'Inflight entertainment','Seat comfort','Food and drink']])

  # Drop columns
  X.drop(['Cleanliness','Inflight entertainment','Seat comfort','Food and drink','Inflight wifi service',
                'Ease of Online booking','Gender','Unnamed: 0','id','satisfaction'], axis=1, inplace=True)
                
  #Mapping the Customer Type, Type of Travel and Class Columns in the Testing Data
  X['Customer Type'] = X['Customer Type'].map({'disloyal Customer': 0, 'Loyal Customer' :1})
  X['Type of Travel'] = X['Type of Travel'].map({'Personal Travel': 0, 'Business travel' :1})
  X['Class'] = X['Class'].map({'Eco': 0, 'Eco Plus' :1, 'Business': 2})

  return X
  
def make_predictions(files_name,model):
  for file_name in files_name:
      X_raw = pd.read_csv(local_dir+file_name)
      X_pred = preprocess(X_raw)
      y_pred = (model.predict(X_pred))
      f = open("pred_"+file_name, "w")
      f.write(str(y_pred))
      f.close()
      return y_pred

while True:
    if os.listdir(bucket_dir) : # Check if a Directory is empty

        filenames = next(os.walk(bucket_dir), (None, None, []))[2]  # [] if no file
        filenames_csv = [x for x in filenames if x.endswith('.csv')]

        if len(filenames_csv)>0:
            for file_name in filenames_csv:
                os.system("cp "+bucket_dir+file_name+" "+local_dir)
                os.system("rm "+bucket_dir+file_name)

            model = pickle.load(open(model_path,"rb"))
            make_predictions(filenames_csv,model)
    
    time.sleep(10)