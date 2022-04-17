import pickle
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
# from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
# import seaborn as sns
dict={
    'Jaundice': 'gastroenterologist',
    'Arthritis': 'rheumatologist',
    'Typhoid': 'infectious-disease',
    'Gastroenteritis': 'gastroenterologist',
    'Tuberculosis': 'pulmonologist-lungs',
    'Alcoholic hepatitis': 'gastroenterologist',
    'Peptic ulcer disease': 'gastroenterologist',
    'Fungal infection': 'dermatologist',
    'Common Cold': 'pediatrician',
    'Heart attack': 'cardiologist',
    'Allergy': 'allergist-immunologist',
    'Migraine': 'neurologist',
    'Hyperthyroidism': 'endocrinologist',
    'GERD': 'gastroenterologist',
    'AIDS': 'infectious-disease',
    'Varicose veins': 'vascular-phlebologist',
    'Hepatitis C': 'gastroenterologist',
    'Hepatitis E': 'gastroenterologist',
    'Pneumonia': 'pulmonologist-lungs',
    'Chicken pox': 'pediatrician',
    'Hepatitis D': 'gastroenterologist',
    '(vertigo) Paroymsal Positional': 'neurologist',
    'Vertigo': 'ear-nose-and-throat-ent',
    'Urinary tract infection': 'urologist',
    'Osteoarthritis': 'rheumatologist',
    'Cervical spondylosis': 'neurologist',
    'Drug Reaction': 'allergist-immunologist',
    'Hypertension': 'cardiologist',
    'Malaria': 'infectious-disease',
    'Psoriasis': 'dermatologist',
    'Hepatitis B': 'gastroenterologist',
    'Chronic cholestasis': 'gastroenterologist',
    'Paralysis (brain hemorrhage)': 'neurologist',
    'Hypothyroidism': 'endocrinologist',
    'hepatitis A': 'gastroenterologist',
    'Acne': 'dermatologist',
    'Impetigo': 'dermatologist',
    'Dengue': 'infectious-disease',
    'Dimorphic hemmorhoids(piles)': 'gastroenterologist',
    'Hypoglycemia': 'endocrinologist',
    'Bronchial Asthma': 'pulmonologist-lungs',
    'Diabetes': 'endocrinologist'
}
def getformat(arr):
  predictmod=[]
  fill=17-len(arr)
  for s in arr:
    x=df1[df1['Symptom']==s].index.values
    # symp=df1.iloc[x][0]
    weight=df1.iloc[x[0]][1]
    print(weight)
    # print(symp,weight)
    predictmod.append(weight)
  for x in range(fill):
    predictmod.append(0)
  print(predictmod)
  return predictmod

df = pd.read_csv('dataset.csv')
print(df.head(n=6))
cols = df.columns
data = df[cols].values.flatten()

s = pd.Series(data)
s = s.str.strip()
s = s.values.reshape(df.shape)

df = pd.DataFrame(s, columns=df.columns)
df = df.fillna(0)
df.head()
df1 = pd.read_csv('Symptom-severity.csv')
arr=[]

####
inp=getformat(arr)
print(inp)
# # load the model from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
illness = loaded_model.predict(([inp]))[0]
print(illness)
print(dict.get(illness))
# result = loaded_model.score(X_test, Y_test)
# print(result)