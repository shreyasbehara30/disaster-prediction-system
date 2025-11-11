@echo off
REM Quick launch script for the Location-Based Disaster Prediction App

echo ========================================================================
echo    MULTI-DISASTER PREDICTION SYSTEM (Location-Based)
echo ========================================================================
echo.
echo Starting Streamlit application...
echo The app will open in your default browser at http://localhost:8502
echo.
echo Features:
echo  - 32+ City Dropdown Selection
echo  - GPS Coordinate Input
echo  - Geological Calibration (Accurate Predictions!)
echo  - 7-Day Future Forecast
echo.
echo Press Ctrl+C to stop the server.
echo ========================================================================
echo.

"..\.venv\Scripts\streamlit.exe" run app_location.py

pause
