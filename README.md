# Wine Cultivar Origin Prediction System

A machine learning-based web application that predicts the cultivar (origin) of wine based on its chemical properties.

## 🎯 Project Overview

This project uses a **Random Forest Classifier** to predict wine cultivar from 6 chemical features:
- Alcohol
- Malic Acid
- Total Phenols
- Flavanoids
- Color Intensity
- Proline

## 📊 Dataset

- **Source**: UCI Machine Learning Repository / sklearn Wine Dataset
- **Samples**: 178 wine samples
- **Classes**: 3 cultivars (Cultivar 0, 1, 2)
- **Features Used**: 6 out of 13 available features

## 🚀 Features

- ✅ Machine Learning model with high accuracy
- ✅ Interactive web interface using Streamlit
- ✅ Real-time predictions
- ✅ Confidence scores visualization
- ✅ Easy deployment to cloud platforms

## 📁 Project Structure

```
WineCultivar_Project/
│
├── app.py                                  # Streamlit web application
├── requirements.txt                         # Python dependencies
├── WineCultivar_hosted_webGUI_link.txt     # Deployment information
├── README.md                                # This file
│
├── model/
│   ├── model_building.ipynb                # Model training notebook
│   └── wine_cultivar_model.pkl             # Trained model file
│
├── static/
│   └── style.css                           # Optional CSS (if needed)
│
└── templates/
    └── index.html                          # Optional HTML (if using Flask)
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd WineCultivar_Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the model (Optional - if model file not included):
   - Open `model/model_building.ipynb` in Google Colab or Jupyter
   - Run all cells to train and save the model
   - Download `wine_cultivar_model.pkl` to the `model/` folder

4. Run the application:
```bash
streamlit run app.py
```

5. Open your browser and navigate to: `http://localhost:8501`

## 📈 Model Performance

- **Algorithm**: Random Forest Classifier
- **Accuracy**: ~97-99%
- **Validation Method**: Train-Test Split (80-20)
- **Feature Scaling**: StandardScaler
- **Model Persistence**: Joblib

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect repository and deploy

### Render.com
1. Create new Web Service
2. Connect GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### PythonAnywhere
1. Upload files to PythonAnywhere
2. Install dependencies
3. Configure web app for Streamlit

## 🧪 Sample Test Data

**Cultivar 0 Sample:**
- Alcohol: 13.2
- Malic Acid: 2.5
- Total Phenols: 2.8
- Flavanoids: 2.9
- Color Intensity: 5.6
- Proline: 1065

**Cultivar 1 Sample:**
- Alcohol: 12.5
- Malic Acid: 3.4
- Total Phenols: 2.0
- Flavanoids: 1.5
- Color Intensity: 4.8
- Proline: 625

**Cultivar 2 Sample:**
- Alcohol: 13.8
- Malic Acid: 1.8
- Total Phenols: 2.6
- Flavanoids: 2.2
- Color Intensity: 7.5
- Proline: 985

## 📋 Requirements

```
streamlit==1.31.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
joblib==1.3.2
matplotlib==3.7.2
seaborn==0.12.2
```

## 👨‍💻 Development

### Model Training Process
1. Data loading and exploration
2. Feature selection (6 features)
3. Data preprocessing (handling missing values)
4. Feature scaling (StandardScaler)
5. Model training (Random Forest)
6. Model evaluation (accuracy, precision, recall, F1-score)
7. Model persistence (Joblib)

### Web Application Features
- Interactive input form
- Real-time prediction
- Confidence visualization
- Input summary display
- Responsive design

## 🤝 Contributing

This is a class project. For any issues or suggestions:
1. Create an issue
2. Submit a pull request

## 📄 License

This project is created for educational purposes as part of CSC415 coursework.

## 📧 Contact

- **Student**: [Your Name]
- **Matric Number**: [Your Matric Number]
- **Course**: CSC415
- **Institution**: Covenant University

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Wine Dataset
- Scikit-learn for machine learning tools
- Streamlit for the web framework

---

**Note**: Make sure to train the model using `model_building.ipynb` before running the web application. The model file (`wine_cultivar_model.pkl`) must be present in the `model/` folder.
