import subprocess

# Activate the virtual environment
subprocess.run(".\\Scripts\\activate", shell=True)

# Export the list of installed packages to requirements.txt
subprocess.run("pip freeze > requirements.txt", shell=True)

# Install packages from requirements.txt
subprocess.run("pip install -r requirements.txt", shell=True)

# Deactivate the virtual environment
subprocess.run("deactivate", shell=True)