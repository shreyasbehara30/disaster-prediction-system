"""
Multi-Disaster Prediction System - Model Training Script
This script trains RandomForestClassifier models for predicting:
- Flood
- Cyclone
- Forest Fire
- Earthquake

Author: AI-Based Disaster Management System
Date: 2025
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

def train_flood_model():
    """Train and save Flood prediction model"""
    print("\n" + "="*60)
    print("🌧️  TRAINING FLOOD PREDICTION MODEL")
    print("="*60)
    
    # Load dataset
    df = pd.read_csv('datasets/flood_data.csv')
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Features and target
    X = df[['rainfall', 'river_level', 'humidity']]
    y = df['flood']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Accuracy: {accuracy*100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Safe', 'Flood Risk']))
    
    # Save model
    joblib.dump(model, 'models/flood_model.pkl')
    print("\n💾 Model saved: models/flood_model.pkl")
    
    return accuracy

def train_cyclone_model():
    """Train and save Cyclone prediction model"""
    print("\n" + "="*60)
    print("🌪️  TRAINING CYCLONE PREDICTION MODEL")
    print("="*60)
    
    # Load dataset
    df = pd.read_csv('datasets/cyclone_data.csv')
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Features and target
    X = df[['wind_speed', 'pressure']]
    y = df['cyclone']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Accuracy: {accuracy*100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Safe', 'Cyclone Risk']))
    
    # Save model
    joblib.dump(model, 'models/cyclone_model.pkl')
    print("\n💾 Model saved: models/cyclone_model.pkl")
    
    return accuracy

def train_fire_model():
    """Train and save Forest Fire prediction model"""
    print("\n" + "="*60)
    print("🔥 TRAINING FOREST FIRE PREDICTION MODEL")
    print("="*60)
    
    # Load dataset
    df = pd.read_csv('datasets/fire_data.csv')
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Features and target
    X = df[['temperature', 'humidity', 'vegetation_index']]
    y = df['fire']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Accuracy: {accuracy*100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Safe', 'Fire Risk']))
    
    # Save model
    joblib.dump(model, 'models/fire_model.pkl')
    print("\n💾 Model saved: models/fire_model.pkl")
    
    return accuracy

def train_earthquake_model():
    """Train and save Earthquake prediction model"""
    print("\n" + "="*60)
    print("🌍 TRAINING EARTHQUAKE PREDICTION MODEL")
    print("="*60)
    
    # Load dataset
    df = pd.read_csv('datasets/earthquake_data.csv')
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Features and target
    X = df[['magnitude', 'depth', 'seismic_activity']]
    y = df['quake']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Accuracy: {accuracy*100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Safe', 'Earthquake Risk']))
    
    # Save model
    joblib.dump(model, 'models/earthquake_model.pkl')
    print("\n💾 Model saved: models/earthquake_model.pkl")
    
    return accuracy

def main():
    """Main function to train all models"""
    print("\n" + "="*60)
    print("🚀 MULTI-DISASTER PREDICTION SYSTEM - MODEL TRAINING")
    print("="*60)
    print("Training 4 Machine Learning Models for Disaster Prediction")
    print("Algorithm: Random Forest Classifier")
    print("="*60)
    
    # Train all models
    accuracies = {}
    
    try:
        accuracies['Flood'] = train_flood_model()
        accuracies['Cyclone'] = train_cyclone_model()
        accuracies['Forest Fire'] = train_fire_model()
        accuracies['Earthquake'] = train_earthquake_model()
        
        # Summary
        print("\n" + "="*60)
        print("📈 TRAINING SUMMARY")
        print("="*60)
        for disaster, acc in accuracies.items():
            print(f"{disaster:15} : {acc*100:.2f}% accuracy")
        
        avg_accuracy = np.mean(list(accuracies.values()))
        print(f"\n{'Average':15} : {avg_accuracy*100:.2f}% accuracy")
        print("="*60)
        print("✅ All models trained and saved successfully!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error during training: {str(e)}")
        raise

if __name__ == "__main__":
    main()
