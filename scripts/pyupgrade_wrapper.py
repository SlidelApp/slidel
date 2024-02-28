import os
import subprocess
import sys

# Change to the desired directory
os.chdir(sys.argv[1])

# Prepend the directory name to each filename
filenames = [f'../{name}' for name in sys.argv[2:]]

# Run the command
subprocess.run(['poetry', 'run', 'pyupgrade', '--py39-plus', *filenames])
