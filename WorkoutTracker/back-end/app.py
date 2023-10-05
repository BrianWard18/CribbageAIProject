from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model and encoders
with open('muscle_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('exercise_encoder.pkl', 'rb') as encoder_file:
    exercise_encoder = pickle.load(encoder_file)

with open('muscle_encoder.pkl', 'rb') as muscle_encoder_file:
    muscle_encoder = pickle.load(muscle_encoder_file)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract workout data from the request
    workouts = data.get('workouts', [])

    # Convert workout descriptions to features using the saved encoder
    exercise_features = exercise_encoder.transform(workout['exercise'] for workout in workouts).toarray()

    # Make predictions using the trained model
    predictions = model.predict(exercise_features)

    # Decode predictions back to muscle names using the saved encoder
    predicted_muscles = muscle_encoder.inverse_transform(predictions)

    return jsonify({'predictions': predicted_muscles.tolist()})

if __name__ == '__main__':
    app.run(debug=True)