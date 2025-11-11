# 🚀 How to Run the Multi-Disaster Prediction System

## Quick Start Commands

### ✅ **OPTION 1: Use the Batch File (Easiest)**

Just double-click this file:
```
run_app.bat
```

Or from PowerShell:
```powershell
.\run_app.bat
```

---

### ✅ **OPTION 2: Manual Commands**

#### **Step 1: Open PowerShell**
- Press `Win + X` → Select "Windows PowerShell"
- Or search for "PowerShell" in Start menu

#### **Step 2: Navigate to Project Folder**
```powershell
cd "C:\Users\ECHO\OneDrive\Desktop\disaster management\multi_disaster"
```

#### **Step 3: Run the App**
```powershell
.\.venv\Scripts\streamlit.exe run app_location.py
```

#### **Step 4: Open Your Browser**
- The app will automatically open at: **http://localhost:8502**
- If it doesn't open automatically, copy the URL from the terminal

---

## 🔧 **If You Need to Retrain Models First**

### Only run this if you have NEW datasets or want to retrain:

```powershell
cd "C:\Users\ECHO\OneDrive\Desktop\disaster management\multi_disaster"
.\.venv\Scripts\python.exe train_models_advanced.py
```

**⏱️ This takes 2-5 minutes** and will show accuracy results.

---

## 📋 **Complete Workflow**

```powershell
# 1. Go to project folder
cd "C:\Users\ECHO\OneDrive\Desktop\disaster management\multi_disaster"

# 2. (Optional) Retrain models if you have new data
.\.venv\Scripts\python.exe train_models_advanced.py

# 3. Run the web app
.\.venv\Scripts\streamlit.exe run app_location.py

# 4. Wait for message: "You can now view your Streamlit app in your browser."

# 5. Open browser and go to: http://localhost:8502
```

---

## 🛑 **How to Stop the App**

### In PowerShell Terminal:
- Press `Ctrl + C`

### Or kill all Streamlit processes:
```powershell
taskkill /F /IM streamlit.exe
```

---

## 🌍 **How to Use the App**

1. **Select a City** from dropdown (Delhi, Mumbai, Tokyo, etc.)
   - OR enter custom GPS coordinates

2. **Click** the green button: **"PREDICT ALL DISASTERS FOR THIS LOCATION"**

3. **View Results:**
   - Risk percentages for all 4 disasters
   - Color-coded alerts (Red = High, Yellow = Medium, Green = Low)
   - 7-day forecast with timeline chart
   - Detailed risk breakdown

---

## ⚡ **One-Line Quick Start**

```powershell
cd "C:\Users\ECHO\OneDrive\Desktop\disaster management\multi_disaster" ; .\.venv\Scripts\streamlit.exe run app_location.py
```

Copy and paste this into PowerShell to run instantly!

---

## 🔍 **Troubleshooting**

### **Error: "streamlit.exe not found"**
```powershell
# Reinstall Streamlit
.\.venv\Scripts\pip.exe install streamlit
```

### **Error: "No module named 'pandas'"**
```powershell
# Install all dependencies
.\.venv\Scripts\pip.exe install -r requirements.txt
```

### **Error: "Model file not found"**
```powershell
# Train the models first
.\.venv\Scripts\python.exe train_models_advanced.py
```

### **Port 8502 Already in Use**
```powershell
# Kill existing Streamlit processes
taskkill /F /IM streamlit.exe

# Or run on different port
.\.venv\Scripts\streamlit.exe run app_location.py --server.port 8503
```

---

## 📱 **Access from Other Devices on Same Network**

1. Find your computer's IP address:
```powershell
ipconfig
```
Look for "IPv4 Address" (e.g., 192.168.1.100)

2. Run app with network access:
```powershell
.\.venv\Scripts\streamlit.exe run app_location.py --server.address 0.0.0.0
```

3. On other device, open browser to:
```
http://192.168.1.100:8502
```

---

## 🎯 **What You Should See**

When app starts successfully, you'll see:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://192.168.1.100:8502
```

---

## 📊 **Expected Performance**

- **Startup Time:** 5-10 seconds (loading models)
- **Prediction Time:** 1-2 seconds per location
- **Memory Usage:** ~500MB RAM
- **Models Loaded:** 4 RandomForest classifiers

---

## ✅ **Verification Checklist**

Before running, ensure you have:
- ✅ Python virtual environment at `.venv/`
- ✅ Trained models in `models/` folder (8 .pkl files)
- ✅ Datasets in `datasets/` folder (4 CSV files)
- ✅ All packages installed (pandas, streamlit, scikit-learn, etc.)

If anything is missing:
```powershell
# Setup everything from scratch
.\.venv\Scripts\pip.exe install -r requirements.txt
.\.venv\Scripts\python.exe train_models_advanced.py
```

---

## 🎉 **You're Ready!**

**Fastest way to start:**
```powershell
.\run_app.bat
```

**Then test with:**
- Delhi → Should show low earthquake risk
- Kathmandu → Should show HIGH earthquake risk (70-95%)
- Tokyo → Should show high cyclone + earthquake risk
- Miami → Should show high cyclone risk

---

**Happy Disaster Predicting! 🌍⚡🔥🌊**
