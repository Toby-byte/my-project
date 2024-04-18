import subprocess

# Activate the virtual environment
subprocess.run(".\\Scripts\\activate", shell=True) # does not work with subprocess

# Export the list of installed packages to requirements.txt
subprocess.run("pip freeze > requirements.txt", shell=True) # works

# Install packages from requirements.txt
subprocess.run("pip install -r requirements.txt", shell=True) # works

# Deactivate the virtual environment
subprocess.run("deactivate", shell=True) # does not work with subprocess