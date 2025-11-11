@echo off
REM Multi-Disaster Prediction System - Windows Setup Script
REM This batch file automates the complete setup process

echo ========================================================================
echo    MULTI-DISASTER PREDICTION SYSTEM - AUTOMATED SETUP
echo ========================================================================
echo.
echo This script will:
echo   1. Install required Python packages
echo   2. Train all ML models
echo   3. Generate documentation
echo   4. Launch the Streamlit application
echo.
echo ========================================================================
pause

echo.
echo ========================================================================
echo    STEP 1: Installing Dependencies
echo ========================================================================
"..\\.venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Please check if Python is installed and added to PATH.
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo    STEP 2: Training ML Models
echo ========================================================================
"..\\.venv\Scripts\python.exe" train_models.py
if errorlevel 1 (
    echo.
    echo ERROR: Model training failed!
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo    STEP 3: Generating Documentation
echo ========================================================================
"..\\.venv\Scripts\python.exe" generate_report.py
"..\\.venv\Scripts\python.exe" generate_presentation.py

echo.
echo ========================================================================
echo    SETUP COMPLETE!
echo ========================================================================
echo.
echo All files have been generated successfully:
echo   - Models trained and saved in models/ folder
echo   - report.docx created
echo   - presentation.pptx created
echo.
echo ========================================================================
echo    Launching Streamlit Application...
echo ========================================================================
echo.
echo The app will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.

"..\\.venv\Scripts\streamlit.exe" run app.py

pause
