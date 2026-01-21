"""
Wine Cultivar Origin Prediction System
Web Application using Streamlit

This application predicts the cultivar (origin) of wine based on its chemical properties.
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="Wine Cultivar Predictor",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #8B0000;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f8ff;
        border: 2px solid #8B0000;
        margin-top: 20px;
    }
    .prediction-result {
        font-size: 2rem;
        color: #8B0000;
        font-weight: bold;
        text-align: center;
    }
    .info-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #ffc107;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    """Load the trained model from disk"""
    try:
        model_path = os.path.join('model', 'wine_cultivar_model.pkl')
        model_package = joblib.load(model_path)
        return model_package
    except FileNotFoundError:
        st.error("❌ Model file not found! Please ensure 'wine_cultivar_model.pkl' is in the 'model/' folder.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

# Main application
def main():
    # Header
    st.markdown('<p class="main-header">🍷 Wine Cultivar Origin Prediction System</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Predict wine cultivar based on chemical properties</p>', unsafe_allow_html=True)
    
    # Load model
    model_package = load_model()
    model = model_package['model']
    scaler = model_package['scaler']
    feature_names = model_package['feature_names']
    target_names = model_package['target_names']
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About")
        st.write("""
        This application uses a **Random Forest Classifier** to predict wine cultivar 
        based on 6 chemical properties.
        """)
        
        st.header("📊 Model Info")
        st.write(f"**Algorithm:** Random Forest")
        st.write(f"**Features Used:** {len(feature_names)}")
        st.write(f"**Classes:** {len(target_names)}")
        
        st.header("🎯 Features")
        for i, feature in enumerate(feature_names, 1):
            st.write(f"{i}. {feature.replace('_', ' ').title()}")
        
        st.header("📝 Instructions")
        st.write("""
        1. Enter the wine's chemical properties
        2. Click the **Predict Cultivar** button
        3. View the prediction result
        """)
    
    # Main content area
    st.markdown("---")
    st.subheader("🔬 Enter Wine Chemical Properties")
    
    # Information box
    st.markdown("""
        <div class="info-box">
            <strong>ℹ️ Note:</strong> Enter the values for each chemical property of the wine sample. 
            All fields are required for accurate prediction.
        </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)
    
    # Define typical ranges for each feature (based on wine dataset)
    feature_ranges = {
        'alcohol': (11.0, 15.0, 13.0),
        'malic_acid': (0.5, 6.0, 2.5),
        'total_phenols': (0.5, 4.0, 2.0),
        'flavanoids': (0.0, 6.0, 2.0),
        'color_intensity': (1.0, 13.0, 5.0),
        'proline': (250.0, 1700.0, 750.0)
    }
    
    # Input fields
    user_input = {}
    
    with col1:
        user_input['alcohol'] = st.number_input(
            "Alcohol (%)",
            min_value=feature_ranges['alcohol'][0],
            max_value=feature_ranges['alcohol'][1],
            value=feature_ranges['alcohol'][2],
            step=0.1,
            help="Alcohol content in percentage"
        )
        
        user_input['malic_acid'] = st.number_input(
            "Malic Acid (g/L)",
            min_value=feature_ranges['malic_acid'][0],
            max_value=feature_ranges['malic_acid'][1],
            value=feature_ranges['malic_acid'][2],
            step=0.1,
            help="Malic acid content in grams per liter"
        )
        
        user_input['total_phenols'] = st.number_input(
            "Total Phenols (g/L)",
            min_value=feature_ranges['total_phenols'][0],
            max_value=feature_ranges['total_phenols'][1],
            value=feature_ranges['total_phenols'][2],
            step=0.1,
            help="Total phenolic content in grams per liter"
        )
    
    with col2:
        user_input['flavanoids'] = st.number_input(
            "Flavanoids (g/L)",
            min_value=feature_ranges['flavanoids'][0],
            max_value=feature_ranges['flavanoids'][1],
            value=feature_ranges['flavanoids'][2],
            step=0.1,
            help="Flavanoid content in grams per liter"
        )
        
        user_input['color_intensity'] = st.number_input(
            "Color Intensity",
            min_value=feature_ranges['color_intensity'][0],
            max_value=feature_ranges['color_intensity'][1],
            value=feature_ranges['color_intensity'][2],
            step=0.1,
            help="Intensity of wine color"
        )
        
        user_input['proline'] = st.number_input(
            "Proline (mg/L)",
            min_value=feature_ranges['proline'][0],
            max_value=feature_ranges['proline'][1],
            value=feature_ranges['proline'][2],
            step=10.0,
            help="Proline content in milligrams per liter"
        )
    
    st.markdown("---")
    
    # Predict button (centered)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button("🔮 Predict Cultivar", use_container_width=True, type="primary")
    
    # Make prediction
    if predict_button:
        # Create input array in the correct order
        input_data = np.array([[user_input[feature] for feature in feature_names]])
        
        # Scale the input data
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        # Display results
        st.markdown("---")
        st.subheader("🎯 Prediction Result")
        
        # Prediction box
        st.markdown(f"""
            <div class="prediction-box">
                <p style="text-align: center; font-size: 1.2rem; margin-bottom: 10px;">
                    The wine sample is predicted to be from:
                </p>
                <p class="prediction-result">{target_names[prediction]}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Display confidence scores
        st.markdown("---")
        st.subheader("📊 Confidence Scores")
        
        # Create a DataFrame for confidence scores
        confidence_df = pd.DataFrame({
            'Cultivar': target_names,
            'Confidence': prediction_proba * 100
        })
        
        # Display as bar chart
        st.bar_chart(confidence_df.set_index('Cultivar'))
        
        # Display detailed confidence scores
        st.write("**Detailed Confidence:**")
        for i, (cultivar, confidence) in enumerate(zip(target_names, prediction_proba)):
            st.write(f"- **{cultivar}:** {confidence * 100:.2f}%")
        
        # Display input summary
        st.markdown("---")
        st.subheader("📋 Input Summary")
        input_df = pd.DataFrame({
            'Property': [name.replace('_', ' ').title() for name in feature_names],
            'Value': [user_input[feature] for feature in feature_names]
        })
        st.dataframe(input_df, use_container_width=True, hide_index=True)
        
        # Success message
        st.success("✅ Prediction completed successfully!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #777; padding: 20px;">
            <p>Wine Cultivar Origin Prediction System | CSC415 Project</p>
            <p>Powered by Machine Learning & Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
