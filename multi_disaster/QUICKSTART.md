# 🚀 Quick Start Guide

## Multi-Disaster Prediction and Alert System

### ⚡ Fast Setup (3 Steps)

#### Option 1: Automated Setup

```powershell
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the complete setup script
python setup.py
```

This will automatically:
- Install all required packages
- Train all 4 ML models
- Generate report.docx
- Generate presentation.pptx

#### Option 2: Manual Setup

```powershell
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Train the models
python train_models.py

# Step 3: Generate documentation (optional)
python generate_report.py
python generate_presentation.py
```

### 🎯 Run the Application

```powershell
streamlit run app.py
```

The app will open in your browser at: `http://localhost:8501`

### 📝 What You'll Get

✅ 4 Trained ML Models (.pkl files)  
✅ Working Streamlit Web App  
✅ Complete Documentation (report.docx)  
✅ Presentation Slides (presentation.pptx)  
✅ All Datasets (CSV files)  

### 🎮 Using the App

1. **Select Disaster Type** - Choose from Flood, Cyclone, Forest Fire, or Earthquake
2. **Adjust Parameters** - Use sliders to set environmental conditions
3. **Click Predict** - Get instant risk assessment
4. **View Results** - See risk gauge, alerts, and charts

### 🔧 Troubleshooting

**Issue**: Module not found  
**Solution**: `pip install -r requirements.txt`

**Issue**: Models not found  
**Solution**: `python train_models.py`

**Issue**: Port already in use  
**Solution**: `streamlit run app.py --server.port 8502`

### 📊 Expected Model Accuracy

- Flood: ~98%
- Cyclone: ~97.5%
- Forest Fire: ~96.5%
- Earthquake: ~99%

### 💡 Tips

- Use realistic parameter ranges (check README.md)
- Green alert = Safe conditions
- Red alert = High risk, take action
- All models are pre-trained and ready to use

---

**Need help?** Check README.md for detailed documentation.
