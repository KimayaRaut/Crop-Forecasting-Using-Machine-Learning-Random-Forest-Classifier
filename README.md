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

git clone https:[//github.com/yourusername/crop-forecasting.git
cd crop-forecasting](https://github.com/KimayaRaut/Crop-Forecasting-Using-Machine-Learning-Random-Forest-Classifier.git)

### Step 2: Create a Virtual Environment
Using virtualenv


```plaintext 
pip install virtualenv
```


```plaintext 
virtualenv venv
```

### Step 3: Activate the Virtual Environment
On Windows:


```plaintext 
venv\Scripts\
```


On MacOS/Linux:


```plaintext
source venv/bin/activate
```

### Step 4: Install the Required Packages
```plaintext 
pip install -r requirements.txt
```

### Step 5: Run the Model Script to Create model.pkl
```plaintext 
python model.py
```

### Step 6: Start the Flask Server
```plaintext 
python app.py
```

### Usage
Ensure the Flask server is running.

Open your web browser and navigate to http://127.0.0.1:5000.

Enter the required environmental parameters (soil nutrient levels, temperature, humidity, pH, rainfall) to get the optimal crop forecast.

### File Structure
```plaintext
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
```

# Output:
![screencapture-127-0-0-1-8000-2024-07-21-05_17_22](https://github.com/user-attachments/assets/04798250-24fe-4815-be2c-f2bc8a9c2cba)

