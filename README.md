# 🚚 PredictPlate

> **ML-Powered Food Delivery Time & Delivery Status Prediction**

PredictPlate is an end-to-end Machine Learning web application that predicts:

- ⏱️ Estimated Food Delivery Time
- 🚦 Delivery Status (On-Time / Late)

The application is built using **Python, Scikit-Learn, Streamlit**, and deployed on **Streamlit Community Cloud**.

---

## 🌐 Live Demo

👉 **https://predictplate.streamlit.app**

---

## ✨ Features

- 📦 Predict delivery time using Machine Learning
- 🚦 Predict whether the order will be On-Time or Late
- 🎨 Modern and responsive UI built with Streamlit
- 📊 Confidence score for predictions
- 🔍 View encoded model inputs
- ⚡ Fast and lightweight deployment

---

## 🧠 Machine Learning Models

### Regression Model
- Random Forest Regressor
- Predicts estimated delivery time

### Classification Model
- Random Forest Classifier
- Predicts delivery status (On-Time / Late)

---

## 📊 Input Features

The prediction is based on:

- Distance (km)
- Preparation Time (minutes)
- Courier Experience
- Weather
- Traffic Level
- Time of Day
- Vehicle Type

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| ML Library | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Streamlit |
| Model Serialization | Joblib |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```
PredictPlate/
│
├── app.py
├── model.pkl
├── classifier.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── Food_Delivery_Delay_Prediction_ML.ipynb
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/darshanpkumar/PredictPlate.git
```

Move into the project directory

```bash
cd PredictPlate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- 📍 Live GPS route integration
- 🗺️ Interactive maps
- 🤖 Deep Learning models
- 📈 Prediction analytics dashboard
- ☁️ Cloud database integration
- 📱 Mobile-friendly responsive UI

---

## 👨‍💻 Developer

**Darshan P Kumar**

- GitHub: https://github.com/darshanpkumar
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📄 License

This project is licensed under the MIT License.
