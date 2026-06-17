# 💻 Laptop Price Predictor

A Machine Learning-based web application that predicts laptop prices using hardware specifications such as Brand, Processor, RAM, Storage, and Screen Size.

The project uses **Linear Regression** for prediction and **Streamlit** for creating an interactive dashboard with visual analytics.

---

## 🚀 Features

* Predict Laptop Prices Instantly
* Interactive Streamlit Dashboard
* Brand Distribution Analysis
* Average Price by Brand Visualization
* RAM vs Price Analysis
* Storage vs Price Analysis
* Processor Distribution Analysis
* Dataset Statistics
* Prediction History
* User-Friendly Interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Plotly

---

## 📊 Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values. The model learns the relationship between laptop specifications and their corresponding prices and generates predictions for new laptop configurations.

---

## 📁 Dataset Features

| Feature     | Description           |
| ----------- | --------------------- |
| Brand       | Laptop Manufacturer   |
| Processor   | CPU Type              |
| RAM         | Memory Capacity (GB)  |
| Storage     | Storage Capacity (GB) |
| Screen Size | Display Size (Inches) |

### Target Variable

| Variable | Description  |
| -------- | ------------ |
| Price    | Laptop Price |

---

## 📂 Project Structure

```text
LaptopPricePredictor/
│
├── app.py
├── train_model.py
├── laptop_data.csv
├── model.pkl
├── brand_encoder.pkl
├── cpu_encoder.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Shivamvishwakarma0122/LaptopPricePredictor.git
```

Move into the project folder:

```bash
cd LaptopPricePredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Run:

```bash
python train_model.py
```

This generates:

```text
model.pkl
brand_encoder.pkl
cpu_encoder.pkl
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## 📈 Dashboard Components

### Statistics Cards

* Total Laptops
* Average Price
* Number of Brands
* Model Accuracy

### Price Prediction

Users can select:

* Brand
* Processor
* RAM
* Storage
* Screen Size

and receive an estimated laptop price.

### Visualizations

* Brand Distribution Pie Chart
* Average Price by Brand Bar Chart
* RAM vs Price Scatter Plot
* Storage vs Price Scatter Plot
* Processor Distribution Chart

### Dataset Preview

Displays the dataset used for training.

### Prediction History

Stores and displays previous predictions made during the current session.

---

## 🎯 Project Objective

The objective of this project is to develop a machine learning model capable of estimating laptop prices based on hardware specifications. The system helps users understand how different laptop configurations affect market prices and assists in making informed purchasing decisions.

---

## 📸 Application Features

✔ Interactive Dashboard

✔ Laptop Price Prediction

✔ Data Analytics & Insights

✔ Graphical Visualizations

✔ Prediction History

✔ User-Friendly Interface

---

## 🔮 Future Scope

* Larger Real-World Datasets
* Random Forest Regression
* XGBoost Regression
* Cloud Deployment
* Laptop Recommendation System
* Real-Time Market Price Integration

---

## 👨‍💻 Author

**Shivam Vishwakarma**

Minor Project: **Laptop Price Predictor**

GitHub Profile:

https://github.com/Shivamvishwakarma0122

Project Repository:

https://github.com/Shivamvishwakarma0122/LaptopPricePredictor

---