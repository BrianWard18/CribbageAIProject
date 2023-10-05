import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your dataset
dataset = pd.read_csv('C:/Users/bward/Documents/WorkoutTracker/data/muscle_data.csv')


# Preprocess the data
exercise_encoder = CountVectorizer()
exercise_features = exercise_encoder.fit_transform(dataset['Exercise']).toarray()

muscle_encoder = LabelEncoder()
target_muscles = muscle_encoder.fit_transform(dataset['Targeted_Muscle_Group'])

# Train a basic machine learning model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(exercise_features, target_muscles)

# Save the model and encoders
with open('muscle_prediction_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('exercise_encoder.pkl', 'wb') as encoder_file:
    pickle.dump(exercise_encoder, encoder_file)

with open('muscle_encoder.pkl', 'wb') as muscle_encoder_file:
    pickle.dump(muscle_encoder, muscle_encoder_file)

print("Training completed. Model and encoders saved.")