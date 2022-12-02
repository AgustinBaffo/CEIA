import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pickle
import os
import time

bucket_dir = "ml2_bucket_uba_abaffo"
local_dir = "local/"
model_path = "./ariline_passanger_satisfaction_model_rf.pickle"
preprocess_dict_path = "./preprocess.pickle"
file_with_names_path = "./new_data_filenames.txt"


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
  pred_file_names = []
  for file_name in files_name:
      X_raw = pd.read_csv(local_dir+file_name)
      X_pred = preprocess(X_raw)
      y_pred = (model.predict(X_pred))
      f = open("./predictions/pred_"+file_name, "w")
      f.write(str(y_pred))
      print("pred values: "+str(y_pred))
      print("saving predictions in predictions/pred_"+str(file_name))
      f.close()
      pred_file_names.append("predictions/pred_"+str(file_name))

  return pred_file_names


already_processed = []

while True:
    # Create a list with the new csv files
    os.system("rm ./new_data_filenames.txt")
    os.system("rm -r ./local")
    os.system("mkdir local")
    os.system("gsutil ls gs://"+str(bucket_dir)+" >> new_data_filenames.txt")
  
    # Check if there are any new csv file in lint
    file_with_names = open(file_with_names_path, "r")
    filenames = file_with_names.read().split("\n")
    file_with_names.close()

    # Only CSV files
    filenames_csv = [x for x in filenames if x.endswith('.csv')]
    
    # Check if they haven't been processed before
    files_to_process = [] 
    for fc in filenames_csv:
      if(not (fc in already_processed)):
        files_to_process.append(fc)
    already_processed = already_processed + files_to_process

    if len(files_to_process)>0: # If there are something new to process
      for f in files_to_process:
        os.system("gsutil cp "+str(f)+" ./local/")
     
      if os.listdir(local_dir):
        local_filenames_csv = next(os.walk(local_dir), (None, None, []))[2]  # [] if no file

        # Load model
        file = open(model_path, 'rb')
        model = pickle.load(file)
        file.close()

        print("predict: "+str(local_filenames_csv))
        pred_file_names = make_predictions(local_filenames_csv,model)
        if(len(pred_file_names)>0):
          for fname in pred_file_names:
            print("gsutil cp "+str(fname)+" gs://"+str(bucket_dir)+"/output/")
            os.system("gsutil cp "+str(fname)+" gs://"+str(bucket_dir)+"/output/")
    
    else:
      print("\nnothing new to process...")

    time.sleep(5)

