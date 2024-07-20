# Crop Forecasting Using Machine Learning Random Forest Classifier

## Overview

This project is a web application designed to forecast optimal crop types based on soil nutrient levels, temperature, humidity, pH, and rainfall. The application uses Flask for API creation, HTML and CSS for the frontend, and a RandomForestClassifier from sklearn for the machine learning model. The model achieves an accuracy of 98% and aims to assist farmers in making informed agricultural decisions.

## Features

- Forecast optimal crop types based on environmental factors
- Easy-to-use web interface
- High accuracy with RandomForestClassifier

## Technologies Used

- Flask (for backend API)
- HTML/CSS (for frontend)
- JavaScript
- scikit-learn (for machine learning model)

## Dataset

The dataset used for training the model is available on Kaggle: [Crop Recommendation Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)

## Installation

### Step 1: Clone the Repository

git clone https://github.com/yourusername/crop-forecasting.git
cd crop-forecasting

### Step 2: Create a Virtual Environment
Using virtualenv
pip install virtualenv
virtualenv venv

### Step 3: Activate the Virtual Environment
On Windows:
venv\Scripts\activate
On MacOS/Linux:
source venv/bin/activate

### Step 4: Install the Required Packages
pip install -r requirements.txt

### Step 5: Run the Model Script to Create model.pkl
python model.py

### Step 6: Start the Flask Server
python app.py

### Usage
Ensure the Flask server is running.
Open your web browser and navigate to http://127.0.0.1:5000.
Enter the required environmental parameters (soil nutrient levels, temperature, humidity, pH, rainfall) to get the optimal crop forecast.

### File Structure
crop-forecasting/
├── app.py             # Flask application
├── model.py           # Script to train and save the machine learning model
├── templates/
│   └── index.html     # HTML file for the frontend
├── static/
│   └── styles.css     # CSS file for styling
├── model.pkl          # Trained machine learning model
├── requirements.txt   # Python package dependencies
└── README.md          # Project documentation

# Output:
![Screenshot (1499)](https://user-images.githubusercontent.com/66699500/126384009-d4f43584-7066-4377-912b-2ce16e1bce92.png)
![Screenshot (1504)](https://user-images.githubusercontent.com/66699500/126384063-977c5ac9-583b-4adb-84f0-9bc6c9cc7cec.png)
![Screenshot (1502)](https://user-images.githubusercontent.com/66699500/126384077-3edcacf2-5287-4b1a-b553-e62ff6a08ee4.png)
![Screenshot (1503)](https://user-images.githubusercontent.com/66699500/126384082-3af9d244-fbad-43f0-a9fd-332961a618b8.png)
