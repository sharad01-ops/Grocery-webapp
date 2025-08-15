#!/usr/bin/env python3
"""
Simple runner script for Grocery Webapp
"""

import os
import sys
import subprocess

def main():
    """Run the grocery webapp"""
    
    # Check if we're in the right directory
    if not os.path.exists("backend"):
        print("Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Check if virtual environment exists
    venv_path = os.path.join("backend", ".venv")
    if not os.path.exists(venv_path):
        print("Virtual environment not found. Creating one...")
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
        
        # Install requirements
        print("Installing dependencies...")
        pip_path = os.path.join(venv_path, "bin", "pip")
        if os.name == "nt":  # Windows
            pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
        
        subprocess.run([pip_path, "install", "-r", "backend/requirements.txt"], check=True)
    
    # Run the application
    print("Starting Grocery Webapp...")
    print("Access the application at: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    
    python_path = os.path.join(venv_path, "bin", "python")
    if os.name == "nt":  # Windows
        python_path = os.path.join(venv_path, "Scripts", "python.exe")
    
    try:
        subprocess.run([python_path, "-m", "backend.app"], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error running the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
