# Python-Project

🍷 **Wine Quality Prediction App**
This project is a simple and interactive web application built with Streamlit that predicts the quality of wine based on its physicochemical properties using a pre-trained machine learning model.

🔍 # *Overview*
The goal of this project is to provide an intuitive interface for users to input features of a wine sample and receive an estimated quality prediction (e.g., low, medium, or high). The model has been trained on the Wine Quality Dataset, commonly used for classification tasks.

📁 # Project Files
main.ipynb: Contains the Jupyter Notebook used for exploratory data analysis, data preprocessing, model training, and evaluation.

app.py: Streamlit-based application that allows users to interact with the model through a web interface.

wine_quality_model.pkl: Trained ML model saved using joblib (must be in the same directory when running the app).

🚀 # How to Run
Install dependencies:

bash
Copy
Edit
pip install streamlit pandas numpy scikit-learn joblib
Run the app:

bash
Copy
Edit
streamlit run app.py
Interact with the app:

Enter wine features like acidity, sugar, alcohol, and wine type.

Click Predict Quality to see the prediction.

🧠 # Model Features
The model considers the following input features:

Fixed Acidity

Volatile Acidity

Citric Acid

Residual Sugar

Chlorides

Free Sulfur Dioxide

Total Sulfur Dioxide

Density

pH

Sulphates

Alcohol

Wine Type (Red or White)

📊 # Model Training
The training notebook (main.ipynb) includes:

Data loading and cleaning

Exploratory data visualization

Feature engineering

Train-test split

Model selection and training

Model evaluation and saving

📦 # Dependencies
streamlit

pandas

numpy

scikit-learn

joblib

📌 # Notes
Ensure wine_quality_model.pkl is present in the working directory when running the app.

This project is for educational/demo purposes. For production use, consider adding model versioning, validation, and exception handling.
