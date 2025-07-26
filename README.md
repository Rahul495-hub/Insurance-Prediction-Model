### Installation & Runnig Locally

```
# Clone the repo
git clone https://github.com/Rahul495-hub/Insurance-Prediction-Model.git
cd Insurance-Prediction-Model

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI app
uvicorn app:app --reload ```


```
🛡️ Insurance Premium Prediction API

A FastAPI-based machine learning solution that predicts insurance premium amounts based on a user's health, lifestyle, and income profile. The project is designed to be modular, scalable, and ready for deployment.
```



 🚀 Overview

This API uses a trained regression model to predict how much premium a user might pay for health insurance. The backend is built with **FastAPI**, enabling fast, interactive, and schema-validated HTTP services.



 📊 Features & Input Parameters

The API accepts the following input features via POST request:

| Feature           | Type   | Description                                                  |
|-------------------|--------|--------------------------------------------------------------|
| `bmi`             | float  | Body Mass Index of the individual                            |
| `age_group`       | str    | Age category (e.g., `18-25`, `26-35`, etc.)                  |
| `lifestyle_risk`  | str    | Risk level (`low`, `medium`, `high`) based on lifestyle      |
| `city_tier`       | int    | City classification based on development (1, 2, 3)           |
| `income_lpa`      | float  | Annual income in lakhs per annum (LPA)                       |
| `occupation`      | str    | Occupation type or category                                  |



🧠 Model Pipeline

1. **Input validation** with `Pydantic` schemas
2. **Prediction logic** encapsulated in `predict_output()`
3. **Model loaded** from `model.pkl`
4. **Versioning** via `MODEL_VERSION`



📁 Project Structure
Insurance-Prediction-Model/
├── app.py # FastAPI application
├── model/
│ ├── model.pkl # Serialized ML model
│ └── predict.py # Prediction pipeline
├── schema/
│ ├── user_input.py # Input data schema (Pydantic)
│ └── prediction_response.py # Output schema
└── README.md # Project documentation
```
