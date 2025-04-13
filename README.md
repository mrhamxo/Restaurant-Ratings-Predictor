# 🍽️ Restaurant Rating Predictor App
An AI-powered Streamlit web application that predicts a restaurant's **aggregate rating** (on a scale of 0.0 to 5.0) using various features such as pricing, table booking availability, online delivery, number of votes, and cuisine types.

> 📊 Ideal for restaurant owners, data analysts, and food tech startups aiming to estimate and enhance their restaurant’s customer perception and review performance.

## 🚀 Features
- 🔢 Predict restaurant review ratings based on:
  - Average cost for two
  - Table booking availability
  - Online delivery availability
  - Price range (1 to 4)
  - Number of user votes
  - Cuisine types (optional via MultiLabelBinarizer)
- 🎨 Intuitive Streamlit UI with review category display
- 🧠 Machine Learning model trained on real restaurant data
- 💬 Review interpretation (Poor, Average, Good, Very Good, Excellent)
- 📉 MAE and RMSE evaluation metrics tracked during training
- 🧮 StandardScaler for consistent input scaling
- 🌐 Social footer with GitHub and LinkedIn links

## 📷 Screenshot
![Image](https://github.com/user-attachments/assets/f6449209-e721-4bc2-bd5c-cc34f7261109)
![Image](https://github.com/user-attachments/assets/72d7f786-344e-4a0a-8fa1-350a8215efac)

## 🛠️ Tech Stack
- **Frontend**: Streamlit (Python-based web UI)
- **Backend/Modeling**: Scikit-learn (Machine Learning)
- **Preprocessing**: StandardScaler, LabelEncoder, MultiLabelBinarizer
- **Deployment Ready**: Works locally and on platforms like Hugging Face Spaces

## 🧠 Machine Learning Models Used
- Linear Regression (LR)
- K-Nearest Neighbors (KNN)
- Decision Tree Regressor (DTR)
- Random Forest Regressor (RFR) ✅ *(Best Performing)*
- Support Vector Regressor (SVR)

All models were evaluated using:
- `Mean Absolute Error (MAE)`
- `Root Mean Squared Error (RMSE)`

## 📁 Project Structure
```
restaurant-rating-predictor/
│
├── model/
│   ├── rf_grid_model.pkl         # Trained Random Forest model
│   └── scaler.pkl                # StandardScaler fitted on training data
│
├── app.py                        # Main Streamlit app
├── requirements.txt              # All dependencies
└── README.md                     # This file
```

## 📊 Input Features
| Feature              | Type        | Description                                          |
|----------------------|-------------|------------------------------------------------------|
| Average Cost for two | Numeric     | Approximate meal cost for two persons                |
| Has Table booking    | Categorical | Yes/No for reservation capability                    |
| Has Online delivery  | Categorical | Yes/No for online ordering                           |
| Price range          | Numeric     | Price tier (1 = cheap, 4 = expensive)                |
| Votes                | Numeric     | Number of customer reviews or feedback submissions   |
| Cuisines             | MultiLabel  | Cuisine types (e.g., Chinese, Japanese, Italian)     |

## 🧑‍💻 Author
- **Muhammad Hamza**  
🔗 [GitHub](https://www.linkedin.com/in/muhammad-hamza-khattak/)  
🔗 [LinkedIn](https://github.com/mrhamxo)

## 📜 License
This project is licensed under the MIT License.
