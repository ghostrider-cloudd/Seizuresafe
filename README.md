# SeizureSafe

**EEG-Based Epileptic Seizure Prediction System Using Ensemble Machine Learning**



## Overview

SeizureSafe is an AI-powered system designed to predict epileptic seizures from EEG signals with high accuracy. It integrates multiple machine learning models to provide early warnings and assist healthcare providers in epilepsy management.

This project was built under the mentorship of 
    **T Mangayarkarasi** as part of the **IEEE EMBS Pune Chapter Internship Program**.



## Features

- Uses **ensemble learning** combining CNN, LSTM, SVM, Random Forest, and XGBoost.
- Processes raw EEG data for reliable seizure prediction.
- Includes a simple web interface for input and prediction visualization.
- Original work includes database connectivity with user and patient data.
- Specialized dashboard and user authentication implemented using secure Firestore database.



## Technology Stack

- **Python** — core programming language
- **Machine Learning Libraries:** TensorFlow / Keras, Scikit-learn, XGBoost
- **Web:** Flask (via `api.py`) for serving predictions
- **Frontend:** HTML/CSS for user interface
- **Database:** Firestore for secure user and patient data management



## Important Note

> This repository contains only a part of the frontend and backend code, shown here due to API security and privacy restrictions.  
> The full original work, including complete API implementations and secure database integrations, is not publicly published here.



## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages listed in `requirements.txt` (create this file if not present)
- A compatible EEG dataset (preprocessed for model input)

### Installation

```bash
git clone https://github.com/ghostrider-cloudd/Seizuresafe.git
cd Seizuresafe
pip install -r requirements.txt
Running the Application
Start the Flask API server:


python api.py
Open index.html in your browser to access the web interface and test seizure predictions.

Usage
Provide EEG data input through the web interface.

The system runs the ensemble ML models to predict seizure likelihood.

Results are displayed dynamically on the prediction page.

Model Details
CNN & LSTM extract temporal and spatial EEG features.

SVM, Random Forest, and XGBoost classifiers combine outputs for final prediction.

Ensemble approach improves accuracy and reduces false positives.

License
This project is licensed under the Apache License 2.0 — see the LICENSE file for details.

Acknowledgements
IEEE EMBS Pune Chapter Internship Program
Mentor: T Mangayarkarasi
Intern: Arjun M

Contact
For questions or collaboration, reach out at:
For questions or collaboration, reach out at:  
[Email me](mailto:arjun.tech@gmail.com) | [LinkedIn](https://www.linkedin.com/in/techarjun/)

