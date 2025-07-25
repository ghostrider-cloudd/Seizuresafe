from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend JS can call API

# Load your model (make sure EE_model.pkl is here)
model = pickle.load(open('EE_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = data.get('input_data', None)

    if input_data is None:
        return jsonify({'error': 'No input data provided'}), 400

    try:
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        if prediction == 0:
            message = 'A seizure is likely to occur. Take precautions!'
        else:
            message = 'No seizure predicted. Stay calm!'

        return jsonify({'prediction': int(prediction), 'message': message})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
