# DATA-SCIENCE-PROJECT

COMPANY: CODTECH IT SOLUTIONS  
NAME: ADITYA KANWAR  
INTERN ID: CT06DF952  
DOMAIN: DATA SCIENCE
DURATION: 6 WEEKS  
MENTOR: NEELA SANTOSH  

Project Overview

This project is a complete end-to-end machine learning-based web application designed to predict whether an individual is diabetic or not based on key medical attributes. The application uses a Logistic Regression model trained on the Pima Indians Diabetes dataset and is deployed through a Flask web framework. The user interacts with the system via a clean and responsive HTML interface, and predictions can also be accessed through a REST API.
The application represents a practical implementation of a typical machine learning workflow: from data preprocessing, model training, and evaluation, to saving the model and building a user-friendly interface for real-time predictions.

Objective

The primary goal of this project is to assist in the early diagnosis of diabetes using a lightweight machine learning model that takes in eight basic health parameters. These include number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, body mass index (BMI), diabetes pedigree function, and age. Based on these inputs, the model determines whether the person is likely to be diabetic or not. This kind of solution can be useful in clinics, rural health centers, or educational projects that aim to demonstrate ML deployment in a healthcare scenario.

Dataset Description

The model is trained using the Pima Indians Diabetes dataset, which is publicly available and widely used for diabetes prediction research. It contains 768 rows and 9 columns, where the features are:
• Pregnancies
• Glucose (mg/dL)
• Blood Pressure (mm Hg)
• Skin Thickness (mm)
• Insulin (µU/mL)
• BMI (kg/m²)
• Diabetes Pedigree Function (a measure of genetic influence)
• Age (in years)
The ninth column is the target variable ‘Outcome’, which is binary: 0 indicates not diabetic, and 1 indicates diabetic.

Model Development

The model chosen for this application is Logistic Regression due to its simplicity and strong baseline performance for binary classification problems. The steps followed during model development include:
• Exploratory Data Analysis (EDA) to understand feature distributions and correlations.
• Data preprocessing including handling of zero or missing values and standardization using StandardScaler.
• Splitting data into training and test sets to evaluate the model’s performance.
• Training the logistic regression model and evaluating metrics like accuracy, precision, recall, and F1-score.
• Final model was serialized using Joblib along with the scaler to ensure consistency during inference.
The final model achieved approximately 78% accuracy on the test set and showed balanced performance in terms of predicting both classes.

Application Structure

The application has the following components:
• app.py: This is the Flask backend script which loads the model and scaler, handles HTTP requests, performs prediction, and renders the HTML template.
• diabetes_model.pkl: The saved machine learning model.
• scaler.pkl: The saved StandardScaler object used to preprocess input data before prediction.
• index.html: The frontend form located inside the templates directory, where users input their health parameters.
• Task3_Project_Diabetes_Predictor.ipynb: The Jupyter notebook where all the preprocessing, model training, and evaluation was done.
• requirements.txt: The list of required Python packages including Flask, Scikit-learn, Pandas, NumPy, and Joblib.

Web Interface

The web page is clean, minimal, and user-friendly. Users are required to enter values for each health parameter. Upon submission, the values are sent via a POST request to the /predict route in the Flask app, which processes the input, makes a prediction using the trained model, and displays the result as either “Diabetic” or “Not Diabetic”.
The interface uses basic HTML and CSS for styling, with dropdowns and number input fields to ensure data consistency and user guidance.
Outputs:
![Image](https://github.com/user-attachments/assets/ad2ce9a7-441d-4779-af2f-e4de1586fdef)
![Image](https://github.com/user-attachments/assets/c80d8c1b-127a-46be-8245-427cc257b8f6)
![Image](https://github.com/user-attachments/assets/f20891bd-44a0-4124-b74c-b0753020cfa0)
![Image](https://github.com/user-attachments/assets/4a3da6a4-30f7-4254-bc71-e0bce5e60310)

API Access

The application also supports API-based prediction through a separate route. A POST request to /api/predict with JSON input returns a JSON response indicating the prediction result. This makes the model accessible programmatically via tools like Postman or external applications.
Input format for API: "data": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
Output format: "prediction": "Diabetic" or "Not Diabetic"

How to Run the Project

To run the project locally, follow these steps:
• Clone the repository or download the project files.
• Ensure Python 3.x is installed.
• Install required dependencies using pip. If requirements.txt is available, run pip install -r requirements.txt.
• Launch the Flask app by running python app.py from the terminal.
• Open a browser and go to http://127.0.0.1:5000 to view the interface.
• Enter input values and receive real-time predictions.
Future Improvements
Some potential future enhancements for this project include:
• Hosting the app on a cloud platform like Heroku, Render, or Railway for public access.
• Integrating a database to store user inputs and results for future reference.
• Expanding the model to use ensemble methods like Random Forest or XGBoost for potentially better accuracy.
• Enhancing the frontend with JavaScript for real-time validation and interactive charts.

Conclusion

This diabetes prediction project showcases how machine learning can be deployed in a real-world healthcare application. It demonstrates the entire workflow, from preprocessing and training to deployment and user interaction. The combination of a lightweight model and an intuitive interface makes it ideal for demonstration, learning, or even use in small-scale health applications. Through both web form and API interaction, the model is accessible to users and developers alike, promoting practical use of AI in healthcare diagnostics.
