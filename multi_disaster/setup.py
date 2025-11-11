"""
Setup Script - Complete Project Setup
This script installs dependencies, trains models, and generates documentation.
"""

import subprocess
import sys
import os

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"▶ {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Success!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed!")
        if e.stderr:
            print(e.stderr)
        return False

def main():
    """Main setup function"""
    print_header("🌍 MULTI-DISASTER PREDICTION SYSTEM - SETUP")
    print("This script will:")
    print("  1. Install required Python packages")
    print("  2. Train all ML models")
    print("  3. Generate documentation (report.docx)")
    print("  4. Generate presentation (presentation.pptx)")
    print("\n" + "="*70)
    
    input("\nPress Enter to continue...")
    
    # Step 1: Install dependencies
    print_header("📦 STEP 1: Installing Dependencies")
    if run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing required packages from requirements.txt"
    ):
        print("All packages installed successfully!")
    else:
        print("⚠️  Warning: Some packages may have failed to install.")
        print("Please install them manually: pip install -r requirements.txt")
    
    # Step 2: Train models
    print_header("🤖 STEP 2: Training ML Models")
    if run_command(
        f"{sys.executable} train_models.py",
        "Training all disaster prediction models"
    ):
        print("All models trained and saved successfully!")
    else:
        print("❌ Model training failed. Please run manually: python train_models.py")
        return
    
    # Step 3: Generate report
    print_header("📄 STEP 3: Generating Report (DOCX)")
    if run_command(
        f"{sys.executable} generate_report.py",
        "Generating project report"
    ):
        print("Report created: report.docx")
    else:
        print("⚠️  Report generation failed. Please run manually: python generate_report.py")
    
    # Step 4: Generate presentation
    print_header("📊 STEP 4: Generating Presentation (PPTX)")
    if run_command(
        f"{sys.executable} generate_presentation.py",
        "Generating project presentation"
    ):
        print("Presentation created: presentation.pptx")
    else:
        print("⚠️  Presentation generation failed. Please run manually: python generate_presentation.py")
    
    # Final summary
    print_header("✅ SETUP COMPLETE!")
    print("Your project is ready to use!\n")
    print("📁 Project Structure:")
    print("  ├── datasets/          (4 CSV files)")
    print("  ├── models/            (4 PKL files)")
    print("  ├── app.py             (Streamlit app)")
    print("  ├── train_models.py    (Training script)")
    print("  ├── report.docx        (Project report)")
    print("  └── presentation.pptx  (Presentation slides)")
    print("\n🚀 To run the application:")
    print("   streamlit run app.py")
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
