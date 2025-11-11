"""
🌍 AI-Based Multi-Disaster Prediction and Alert System
A Streamlit web application for predicting natural disasters using Machine Learning

Supported Disasters:
- 🌧️ Flood
- 🌪️ Cyclone
- 🔥 Forest Fire
- 🌍 Earthquake

Author: AI-Based Disaster Management System
Date: 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Multi-Disaster Prediction System",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .alert-safe {
        padding: 20px;
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        border-radius: 5px;
        margin: 20px 0;
    }
    .alert-danger {
        padding: 20px;
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        border-radius: 5px;
        margin: 20px 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Load models function
@st.cache_resource
def load_model(disaster_type):
    """Load the trained model for specified disaster type"""
    model_paths = {
        'Flood': 'models/flood_model.pkl',
        'Cyclone': 'models/cyclone_model.pkl',
        'Forest Fire': 'models/fire_model.pkl',
        'Earthquake': 'models/earthquake_model.pkl'
    }
    
    model_path = model_paths.get(disaster_type)
    if model_path and os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        return None

def create_gauge_chart(probability):
    """Create a gauge chart for risk probability"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = probability * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Risk Level (%)", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#d4edda'},
                {'range': [30, 70], 'color': '#fff3cd'},
                {'range': [70, 100], 'color': '#f8d7da'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def create_feature_chart(features, values, disaster_type):
    """Create a bar chart showing input feature values"""
    fig = go.Figure(data=[
        go.Bar(
            x=features,
            y=values,
            marker_color=['#1E88E5', '#43A047', '#FB8C00'],
            text=values,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=f"{disaster_type} - Input Parameters",
        xaxis_title="Parameters",
        yaxis_title="Values",
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig

def predict_flood():
    """Flood prediction interface"""
    st.subheader("🌧️ Flood Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        rainfall = st.slider(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=250.0,
            value=50.0,
            step=5.0,
            help="Amount of rainfall in millimeters"
        )
    
    with col2:
        river_level = st.slider(
            "River Level (m)",
            min_value=0.0,
            max_value=15.0,
            value=3.0,
            step=0.5,
            help="Current river water level in meters"
        )
    
    with col3:
        humidity = st.slider(
            "Humidity (%)",
            min_value=0,
            max_value=100,
            value=70,
            step=5,
            help="Current humidity percentage"
        )
    
    if st.button("🔍 Predict Flood Risk", key="flood_predict"):
        model = load_model('Flood')
        
        if model:
            # Prepare input
            input_data = np.array([[rainfall, river_level, humidity]])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            # Display results
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if prediction == 1:
                    st.markdown("""
                    <div class="alert-danger">
                        <h2>🚨 FLOOD ALERT!</h2>
                        <p><strong>High Risk Detected</strong></p>
                        <p>Immediate action recommended. Please move to higher ground and follow evacuation procedures.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="alert-safe">
                        <h2>✅ SAFE ZONE</h2>
                        <p><strong>Low Flood Risk</strong></p>
                        <p>Current conditions are within safe parameters. Continue monitoring weather updates.</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.plotly_chart(create_gauge_chart(probability[1]), use_container_width=True)
            
            # Feature chart
            st.plotly_chart(
                create_feature_chart(
                    ['Rainfall (mm)', 'River Level (m)', f'Humidity (%)'],
                    [rainfall, river_level, humidity],
                    'Flood'
                ),
                use_container_width=True
            )
            
        else:
            st.error("❌ Model not found. Please run train_models.py first!")

def predict_cyclone():
    """Cyclone prediction interface"""
    st.subheader("🌪️ Cyclone Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        wind_speed = st.slider(
            "Wind Speed (km/h)",
            min_value=0.0,
            max_value=200.0,
            value=50.0,
            step=5.0,
            help="Current wind speed in kilometers per hour"
        )
    
    with col2:
        pressure = st.slider(
            "Atmospheric Pressure (hPa)",
            min_value=940,
            max_value=1030,
            value=1010,
            step=5,
            help="Current atmospheric pressure in hectopascals"
        )
    
    if st.button("🔍 Predict Cyclone Risk", key="cyclone_predict"):
        model = load_model('Cyclone')
        
        if model:
            # Prepare input
            input_data = np.array([[wind_speed, pressure]])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            # Display results
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if prediction == 1:
                    st.markdown("""
                    <div class="alert-danger">
                        <h2>🚨 CYCLONE ALERT!</h2>
                        <p><strong>High Risk Detected</strong></p>
                        <p>Severe weather conditions detected. Seek shelter immediately and secure all outdoor items.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="alert-safe">
                        <h2>✅ SAFE ZONE</h2>
                        <p><strong>Low Cyclone Risk</strong></p>
                        <p>Weather conditions are stable. Continue normal activities with caution.</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.plotly_chart(create_gauge_chart(probability[1]), use_container_width=True)
            
            # Feature chart
            st.plotly_chart(
                create_feature_chart(
                    ['Wind Speed (km/h)', 'Pressure (hPa)'],
                    [wind_speed, pressure],
                    'Cyclone'
                ),
                use_container_width=True
            )
            
        else:
            st.error("❌ Model not found. Please run train_models.py first!")

def predict_forest_fire():
    """Forest Fire prediction interface"""
    st.subheader("🔥 Forest Fire Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        temperature = st.slider(
            "Temperature (°C)",
            min_value=0.0,
            max_value=50.0,
            value=25.0,
            step=1.0,
            help="Current temperature in Celsius"
        )
    
    with col2:
        humidity = st.slider(
            "Humidity (%)",
            min_value=0,
            max_value=100,
            value=50,
            step=5,
            help="Current humidity percentage"
        )
    
    with col3:
        vegetation_index = st.slider(
            "Vegetation Index",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help="Normalized Difference Vegetation Index (0-1)"
        )
    
    if st.button("🔍 Predict Fire Risk", key="fire_predict"):
        model = load_model('Forest Fire')
        
        if model:
            # Prepare input
            input_data = np.array([[temperature, humidity, vegetation_index]])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            # Display results
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if prediction == 1:
                    st.markdown("""
                    <div class="alert-danger">
                        <h2>🚨 FIRE ALERT!</h2>
                        <p><strong>High Fire Risk Detected</strong></p>
                        <p>Critical fire danger conditions. Avoid open flames and report any smoke immediately.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="alert-safe">
                        <h2>✅ SAFE ZONE</h2>
                        <p><strong>Low Fire Risk</strong></p>
                        <p>Fire danger is minimal. Remain vigilant and follow fire safety guidelines.</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.plotly_chart(create_gauge_chart(probability[1]), use_container_width=True)
            
            # Feature chart
            st.plotly_chart(
                create_feature_chart(
                    ['Temperature (°C)', 'Humidity (%)', 'Vegetation Index'],
                    [temperature, humidity, vegetation_index],
                    'Forest Fire'
                ),
                use_container_width=True
            )
            
        else:
            st.error("❌ Model not found. Please run train_models.py first!")

def predict_earthquake():
    """Earthquake prediction interface"""
    st.subheader("🌍 Earthquake Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        magnitude = st.slider(
            "Magnitude",
            min_value=0.0,
            max_value=10.0,
            value=3.0,
            step=0.1,
            help="Earthquake magnitude on Richter scale"
        )
    
    with col2:
        depth = st.slider(
            "Depth (km)",
            min_value=0,
            max_value=100,
            value=20,
            step=5,
            help="Earthquake depth in kilometers"
        )
    
    with col3:
        seismic_activity = st.slider(
            "Seismic Activity",
            min_value=0,
            max_value=300,
            value=50,
            step=10,
            help="Recent seismic activity level"
        )
    
    if st.button("🔍 Predict Earthquake Risk", key="earthquake_predict"):
        model = load_model('Earthquake')
        
        if model:
            # Prepare input
            input_data = np.array([[magnitude, depth, seismic_activity]])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            # Display results
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if prediction == 1:
                    st.markdown("""
                    <div class="alert-danger">
                        <h2>🚨 EARTHQUAKE ALERT!</h2>
                        <p><strong>High Seismic Risk Detected</strong></p>
                        <p>Significant earthquake activity detected. Take cover under sturdy furniture and stay away from windows.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="alert-safe">
                        <h2>✅ SAFE ZONE</h2>
                        <p><strong>Low Earthquake Risk</strong></p>
                        <p>Seismic activity is within normal range. Continue normal activities.</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.plotly_chart(create_gauge_chart(probability[1]), use_container_width=True)
            
            # Feature chart
            st.plotly_chart(
                create_feature_chart(
                    ['Magnitude', 'Depth (km)', 'Seismic Activity'],
                    [magnitude, depth, seismic_activity],
                    'Earthquake'
                ),
                use_container_width=True
            )
            
        else:
            st.error("❌ Model not found. Please run train_models.py first!")

def main():
    """Main application function"""
    
    # Header
    st.markdown('<h1 class="main-header">🌍 AI-Based Multi-Disaster Prediction and Alert System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Predicting Natural Disasters using Machine Learning | Powered by Random Forest Classifier</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/natural-disaster.png", width=100)
        st.title("🎯 Select Disaster Type")
        
        disaster_type = st.selectbox(
            "Choose a disaster to predict:",
            ['Flood', 'Cyclone', 'Forest Fire', 'Earthquake'],
            help="Select the type of natural disaster you want to predict"
        )
        
        st.markdown("---")
        st.markdown("### 📊 About")
        st.info("""
        This AI-powered system uses **Random Forest Classifier** to predict the likelihood of natural disasters based on environmental parameters.
        
        **Features:**
        - Real-time predictions
        - Visual risk indicators
        - Alert notifications
        - Interactive charts
        """)
        
        st.markdown("---")
        st.markdown("### 🛠️ Tech Stack")
        st.markdown("""
        - Python 3.x
        - Scikit-learn
        - Streamlit
        - Plotly
        - Pandas
        """)
        
        st.markdown("---")
        st.markdown(f"**📅 Date:** {datetime.now().strftime('%Y-%m-%d')}")
        st.markdown(f"**⏰ Time:** {datetime.now().strftime('%H:%M:%S')}")
    
    # Main content
    st.markdown("---")
    
    # Route to appropriate prediction function
    if disaster_type == 'Flood':
        predict_flood()
    elif disaster_type == 'Cyclone':
        predict_cyclone()
    elif disaster_type == 'Forest Fire':
        predict_forest_fire()
    elif disaster_type == 'Earthquake':
        predict_earthquake()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>🌍 Multi-Disaster Prediction System | Developed with ❤️ using AI & Machine Learning</p>
        <p>⚠️ <strong>Disclaimer:</strong> This system is for educational and demonstration purposes. 
        Always follow official disaster management guidelines and alerts from authorized agencies.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
