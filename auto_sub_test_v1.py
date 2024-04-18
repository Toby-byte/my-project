import subprocess
import os

# Path to the Python executable inside the virtual environment
python_executable = "Scripts\\python.exe"  # Use "Scripts\\python.exe" on Windows

# Install packages using the Python executable
subprocess.run([python_executable, "-m", "pip", "install", "requests"])

# Export the list of installed packages to requirements.txt
subprocess.run("pip freeze > requirements.txt", shell=True) # works

# Install packages from requirements.txt
subprocess.run("pip install -r requirements.txt", shell=True) # works

# Create a directory
os.makedirs('I appear if it worked', exist_ok=True)