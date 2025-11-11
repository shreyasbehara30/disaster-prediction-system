# 📊 How to Use Your Own Datasets

## Yes! You Can Use Your Own Datasets! ✅

This guide shows you **exactly how to replace the synthetic data with your own real datasets** for better predictions.

---

## 🎯 Quick Answer

**YES, you can absolutely provide your own datasets!** The system is designed to be flexible and easy to customize with your data.

---

## 📋 Dataset Requirements

For each disaster type, your CSV file must have specific columns:

### 1. Flood Dataset (`flood_data.csv`)
**Required Columns:**
- `rainfall` - Amount of rainfall in mm (0-300 typical range)
- `river_level` - Water level in meters (0-20 typical range)
- `humidity` - Humidity percentage (0-100)
- `flood` - Target label (0 = no flood, 1 = flood)

**Example Format:**
```csv
rainfall,river_level,humidity,flood
45.2,3.5,78,0
120.5,8.2,92,1
150.3,9.5,95,1
30.1,2.1,65,0
```

### 2. Cyclone Dataset (`cyclone_data.csv`)
**Required Columns:**
- `wind_speed` - Wind speed in km/h (0-250 typical range)
- `pressure` - Atmospheric pressure in hPa (900-1030 typical range)
- `cyclone` - Target label (0 = no cyclone, 1 = cyclone)

**Example Format:**
```csv
wind_speed,pressure,cyclone
45.2,1012,0
95.8,985,1
110.3,975,1
30.5,1015,0
```

### 3. Forest Fire Dataset (`fire_data.csv`)
**Required Columns:**
- `temperature` - Temperature in °C (0-60 typical range)
- `humidity` - Humidity percentage (0-100)
- `vegetation_index` - NDVI value (0.0-1.0)
- `fire` - Target label (0 = no fire, 1 = fire)

**Example Format:**
```csv
temperature,humidity,vegetation_index,fire
18.5,65,0.45,0
38.2,22,0.85,1
42.6,18,0.92,1
15.3,70,0.42,0
```

### 4. Earthquake Dataset (`earthquake_data.csv`)
**Required Columns:**
- `magnitude` - Richter scale magnitude (0-10)
- `depth` - Depth in kilometers (0-700)
- `seismic_activity` - Recent seismic activity level (0-500)
- `quake` - Target label (0 = no major quake, 1 = major quake)

**Example Format:**
```csv
magnitude,depth,seismic_activity,quake
2.5,15,45,0
6.8,25,185,1
7.5,35,220,1
1.8,10,32,0
```

---

## 🔄 How to Replace Datasets

### Method 1: Replace Existing Files (Easiest)

1. **Prepare Your Data**
   - Format your data to match the required columns (see above)
   - Save as CSV files with the exact names

2. **Replace the Files**
   ```
   Navigate to: multi_disaster/datasets/
   
   Replace these files with yours:
   - flood_data.csv
   - cyclone_data.csv
   - fire_data.csv
   - earthquake_data.csv
   ```

3. **Retrain the Models**
   ```bash
   # Run this in the multi_disaster folder
   ..\.venv\Scripts\python.exe train_models.py
   ```

4. **Done!** Your models are now trained on your own data!

### Method 2: Add New Files (Keep Both)

If you want to keep the original synthetic data:

1. **Save your data with different names:**
   ```
   my_flood_data.csv
   my_cyclone_data.csv
   my_fire_data.csv
   my_earthquake_data.csv
   ```

2. **Update `train_models.py`:**

   Find this line (around line 23):
   ```python
   df = pd.read_csv('datasets/flood_data.csv')
   ```
   
   Change to:
   ```python
   df = pd.read_csv('datasets/my_flood_data.csv')
   ```
   
   Repeat for all 4 disaster types (lines 23, 57, 91, 125)

3. **Retrain models:**
   ```bash
   ..\.venv\Scripts\python.exe train_models.py
   ```

---

## 📥 Where to Get Real Datasets

### Recommended Sources:

1. **Kaggle Datasets**
   - [Flood Prediction Dataset](https://www.kaggle.com/datasets)
   - [Cyclone Dataset](https://www.kaggle.com/datasets)
   - [Forest Fires Data Set](https://www.kaggle.com/datasets)
   - [Earthquake Dataset](https://www.kaggle.com/datasets)

2. **Government Sources**
   - NOAA (National Oceanic and Atmospheric Administration)
   - USGS (United States Geological Survey)
   - Your country's meteorological department
   - Seismological institutes

3. **Research Repositories**
   - UCI Machine Learning Repository
   - Google Dataset Search
   - AWS Open Data Registry

---

## 🛠️ Data Preparation Tips

### 1. Clean Your Data
```python
import pandas as pd

# Load your data
df = pd.read_csv('your_data.csv')

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Check data types
print(df.dtypes)
print(df.describe())
```

### 2. Create Target Labels

If your data doesn't have binary labels (0/1), you need to create them:

**Example for Flood:**
```python
# If you have 'flood_occurred' column with Yes/No
df['flood'] = df['flood_occurred'].map({'Yes': 1, 'No': 0})

# Or based on threshold
df['flood'] = (df['water_level'] > 5).astype(int)
```

### 3. Feature Engineering

Add or derive features if needed:
```python
# Example: Calculate vegetation index from other columns
df['vegetation_index'] = (df['NIR'] - df['Red']) / (df['NIR'] + df['Red'])

# Example: Normalize temperature
df['temperature'] = (df['temp_kelvin'] - 273.15)
```

### 4. Balance Your Dataset

Make sure you have balanced classes (roughly equal 0s and 1s):
```python
print(df['flood'].value_counts())

# If imbalanced, you can undersample or oversample
from sklearn.utils import resample

# Separate majority and minority classes
df_majority = df[df.flood==0]
df_minority = df[df.flood==1]

# Upsample minority class
df_minority_upsampled = resample(df_minority, 
                                 replace=True,     
                                 n_samples=len(df_majority),    
                                 random_state=42)

# Combine
df_balanced = pd.concat([df_majority, df_minority_upsampled])
```

---

## 📊 Example: Converting Your Own Data

Let's say you have flood data from your local area:

**Your Original Data (my_flood_observations.csv):**
```csv
date,location,rain_mm,water_height_m,humidity_pct,flooding_event
2024-01-15,City A,120,8.5,90,Yes
2024-01-16,City A,30,2.1,65,No
2024-01-17,City B,150,9.2,95,Yes
```

**Convert to Required Format:**
```python
import pandas as pd

# Load your data
df = pd.read_csv('my_flood_observations.csv')

# Rename columns to match required format
df = df.rename(columns={
    'rain_mm': 'rainfall',
    'water_height_m': 'river_level',
    'humidity_pct': 'humidity'
})

# Convert target to binary
df['flood'] = df['flooding_event'].map({'Yes': 1, 'No': 0})

# Keep only required columns
df = df[['rainfall', 'river_level', 'humidity', 'flood']]

# Save in correct format
df.to_csv('datasets/flood_data.csv', index=False)

print("✅ Data converted successfully!")
print(df.head())
```

---

## 🎯 Minimum Dataset Size

**Recommendations:**
- **Minimum:** 50-100 samples per disaster type
- **Good:** 500-1000 samples
- **Excellent:** 5000+ samples

More data = Better accuracy!

---

## ✅ Checklist Before Training

Before training with your own data:

- [ ] CSV files have correct column names (case-sensitive!)
- [ ] Target column is binary (0 or 1)
- [ ] No missing values (NaN, null)
- [ ] Data types are numeric (not text)
- [ ] Files saved in `datasets/` folder
- [ ] File names match: `flood_data.csv`, `cyclone_data.csv`, etc.
- [ ] At least 50+ samples per file
- [ ] Both classes represented (some 0s and some 1s)

---

## 🚀 Training With Your Data

Once your data is ready:

### Step 1: Place Files
```
multi_disaster/
  └── datasets/
      ├── flood_data.csv      ← Your file
      ├── cyclone_data.csv    ← Your file
      ├── fire_data.csv       ← Your file
      └── earthquake_data.csv ← Your file
```

### Step 2: Train Models

**Option A - Windows Batch File:**
```batch
run_setup.bat
```

**Option B - PowerShell:**
```powershell
cd "C:\Users\ECHO\OneDrive\Desktop\disaster management\multi_disaster"
..\.venv\Scripts\python.exe train_models.py
```

**Option C - Direct Python:**
```python
python train_models.py
```

### Step 3: Check Results
The script will show accuracy for each model:
```
🌧️ Flood Model: XX% accuracy
🌪️ Cyclone Model: XX% accuracy
🔥 Forest Fire Model: XX% accuracy
🌍 Earthquake Model: XX% accuracy
```

If accuracy is low (<80%), you may need:
- More data
- Better quality data
- Different features
- Model tuning

---

## 🔧 Advanced: Customize Model Parameters

Edit `train_models.py` to adjust model settings:

Find this section (appears 4 times, once per disaster):
```python
model = RandomForestClassifier(
    n_estimators=100,      # Number of trees (increase for more accuracy)
    max_depth=10,          # Tree depth (increase for complex patterns)
    random_state=42        # For reproducibility
)
```

Try different values:
```python
model = RandomForestClassifier(
    n_estimators=200,      # More trees
    max_depth=15,          # Deeper trees
    min_samples_split=5,   # Minimum samples to split
    min_samples_leaf=2,    # Minimum samples in leaf
    random_state=42
)
```

---

## 📧 Send Me Your Dataset (How To Share)

**Yes, you can share your dataset with me!** Here's how:

### Method 1: Share CSV Files
1. Place your CSV files in the `datasets/` folder
2. Let me know the file names
3. I can help you:
   - Verify the format is correct
   - Train models on your data
   - Optimize model parameters
   - Troubleshoot any issues

### Method 2: Share Sample Data
If your dataset is large, share:
- First 10-20 rows (as CSV or text)
- Column names and descriptions
- Data ranges and units
- Any special considerations

### What I Can Do For You:
✅ Validate your data format
✅ Train models with your data
✅ Adjust model parameters for better accuracy
✅ Add new features or disaster types
✅ Fix any errors or issues
✅ Optimize performance

---

## 💡 Pro Tips

1. **Start Small** - Test with 100 samples first, then scale up
2. **Validate Data** - Always check your CSV opens correctly in Excel
3. **Backup Original** - Keep a copy of synthetic data for testing
4. **Check Accuracy** - If <80%, you need more/better data
5. **Balance Classes** - Equal number of 0s and 1s is ideal
6. **Use Real Units** - Keep units consistent (mm, km/h, °C, etc.)

---

## ❓ Common Questions

**Q: How many samples do I need?**
A: Minimum 50-100, but 500+ is better. More data = higher accuracy.

**Q: Can I have different column names?**
A: Yes! Just rename them in the CSV or update `train_models.py`.

**Q: What if I only have data for one disaster?**
A: That's fine! Keep synthetic data for others, use yours for one.

**Q: Can I add more features?**
A: Yes! Update the model training code to include more columns.

**Q: My accuracy is low, what should I do?**
A: Try: more data, different features, tune model parameters, check data quality.

---

## 🎉 Summary

**YES, you can use your own datasets!**

Just follow these steps:
1. Format your CSV files correctly
2. Place them in `datasets/` folder
3. Run `train_models.py`
4. Your models are trained on YOUR data!

**Need help?** Share your dataset and I'll help you get it working! 🚀

---

*Built to be flexible and customizable for YOUR data needs!*
