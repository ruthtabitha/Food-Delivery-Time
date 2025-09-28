# 🍔🚴 Food Delivery Time Prediction with Machine Learning

Food delivery services are expanding rapidly, and **accurate estimation of delivery time (ETA)** is essential for customer satisfaction and efficient logistics.  
This project uses **machine learning** to analyze delivery, courier, and environmental factors, predict delivery times, and provide insights to support **operational optimization**.

---

## 📌 Business Understanding
The main objectives are:
- Identify the key factors contributing to delivery time  
- Build a predictive model to estimate food delivery duration  
- Compare model performance against baseline predictions  
- Generate actionable insights to support decision-making in logistics  

---

## ❓ Key Questions
- Which factors contribute the most to delivery delays?  
- Can a machine learning model accurately predict food delivery times?  
- How well can the model perform compared to baseline predictions?  
- What insights can be drawn to improve delivery efficiency?  

---

## 📊 Data Understanding

**Source:** Synthetic food delivery dataset *(curated and balanced for modeling purposes)*  

| Column                       | Description |
|-------------------------------|-------------|
| `Distance_km`                 | Distance between restaurant and customer (in km) |
| `Preparation_Time_min`        | Food preparation time at restaurant (in minutes) |
| `Traffic_Level`               | Low, Medium, High |
| `Weather`                     | Clear, Rainy, Storm, Fog |
| `Vehicle_Type`                | Motorbike, Car, Scooter |
| `Courier_Experience_yrs`      | Courier’s experience in years |
| `Courier_Experience_Category` | Novice, Intermediate, Expert |
| `Distance_Category`           | Short, Medium, Long |
| `Time_of_Day`                 | Morning, Afternoon, Evening, Night |
| `Delivery_Time` (target)      | Actual delivery time in minutes |

---

## ⚙️ Data Preprocessing
- Handle missing values if any  
- Encode categorical variables  
- Normalize continuous features (`Distance_km`, `Preparation_Time_min`, `Courier_Experience_yrs`)  
- Split dataset into **train (80%)** and **test (20%)**

---

## 🤖 Models
- Ridge Regression (baseline)  
- Decision Tree  
- Random Forest  
- XGBoost  

---

## 📈 Results
- **Dataset Size:** ~560 deliveries  
- **Best Model Performance:** Ridge Regression with MAE ≈ 5 minutes  
- **Relative Error:** ~15–20% of average delivery time  
- **Strongest Predictors:** Distance, Preparation Time, Traffic Level  

---

## 💻 Dummy App
A **Streamlit app** was developed where users can input order details (distance, preparation time, traffic, weather, vehicle type, etc.) and instantly get a predicted delivery time (ETA).  

🔗 [Try the App](#) *(https://food-delivery-prediction-ruth.streamlit.app/)*  

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/food-delivery-time-prediction.git
cd food-delivery-time-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
