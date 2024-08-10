import pandas as pd
import numpy as np
from keras.models import load_model
model = load_model("model2.h5")

def make_prediction(model,data):
  df = pd.read_csv(data,header=None)
  df = pd.DataFrame(df)
  class_1 = df[df[187]==1.0]
  class_2 = df[df[187]==2.0]
  class_3 = df[df[187]==3.0]
  class_4 = df[df[187]==4.0]
  class_0 = df[df[187]==0.0].sample(n = 2000)
  df = pd.concat([class_1, class_2, class_3, class_4, class_0]).sample(frac=1)
  x_test = df.drop([187], axis=1) 
  y_test = df[187]
  x_test = np.array(x_test).reshape(x_test.shape[0],x_test.shape[1],1)
  user_input = int(input("Enter a record number "))
  x_test_user = np.array(x_test[user_input]).reshape(-1,x_test[user_input].shape[0],1)  
  prediction = model.predict(x_test_user)
  classes = ['Normal', 'Supraventricular Ectopic Beat', 'Ventricular Ectopic Beat', 'Fusion Beats', 'Unkown Beats']
  classes_predictions = np.argmax(prediction)
  predicted_label = classes[classes_predictions]
  return predicted_label