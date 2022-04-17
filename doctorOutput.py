import pickle
import pandas as pd
from sklearn.svm import SVC
# from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
# import seaborn as sns
global df1, symptomList, dict
def getformat(arr):
  predictmod=[]
  for s in arr:
    s = s.lower()
    s = s.replace(' ', '_')
    if s not in symptomList:
      continue
    x=df1[df1['Symptom']==s].index.values
    # symp=df1.iloc[x][0]
    weight=df1.iloc[x[0]][1]
    # print(symp,weight)
    predictmod.append(weight)
  for x in range(17-len(predictmod)):
    predictmod.append(0)
  return predictmod
def outputDisease(symptomString):
  global dict, symptomList, df1
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
  symptomList = {'itching', 'skin_rash', 'nodal_skin_eruptions',
        'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
        'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
        'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue',
        'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings',
        'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat',
        'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes',
        'breathlessness', 'sweating', 'dehydration', 'indigestion',
        'headache', 'yellowish_skin', 'dark_urine', 'nausea',
        'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
        'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
        'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
        'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes',
        'malaise', 'blurred_and_distorted_vision', 'phlegm',
        'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
        'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
        'fast_heart_rate', 'pain_during_bowel_movements',
        'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
        'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
        'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
        'excessive_hunger', 'extra_marital_contacts',
        'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
        'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
        'swelling_joints', 'movement_stiffness', 'spinning_movements',
        'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
        'loss_of_smell', 'bladder_discomfort', 'foul_smell_ofurine',
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
        'altered_sensorium', 'red_spots_over_body', 'belly_pain',
        'abnormal_menstruation', 'dischromic_patches',
        'watering_from_eyes', 'increased_appetite', 'polyuria',
        'family_history', 'mucoid_sputum', 'rusty_sputum',
        'lack_of_concentration', 'visual_disturbances',
        'receiving_blood_transfusion', 'receiving_unsterile_injections',
        'coma', 'stomach_bleeding', 'distention_of_abdomen',
        'history_of_alcohol_consumption', 'blood_in_sputum',
        'prominent_veins_on_calf', 'palpitations', 'painful_walking',
        'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
        'silver_like_dusting', 'small_dents_in_nails',
        'inflammatory_nails', 'blister', 'red_sore_around_nose',
        'yellow_crust_ooze', 'prognosis'}

  df = pd.read_csv('dataset.csv')
  cols = df.columns
  data = df[cols].values.flatten()

  s = pd.Series(data)
  s = s.str.strip()
  s = s.values.reshape(df.shape)

  df = pd.DataFrame(s, columns=df.columns)
  df = df.fillna(0)
  df1 = pd.read_csv('Symptom-severity.csv')
  arr = symptomString.split(', ')
  inp=getformat(arr)

  # # load the model from disk
  filename = 'finalized_model.sav'
  loaded_model = pickle.load(open(filename, 'rb'))
  illness = loaded_model.predict(([inp]))[0]
  # print(illness)
  return (illness,dict.get(illness))
