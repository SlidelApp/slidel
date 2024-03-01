import os
import subprocess
import sys

# Change to the desired directory
os.chdir(sys.argv[1])

# Run the command
try:
    subprocess.run(['poetry', 'run', *sys.argv[2:]], check=True)
except subprocess.CalledProcessError as e:
    sys.exit(e.returncode)
