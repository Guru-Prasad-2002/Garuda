import psutil
import os
import subprocess

def stop_script_by_name(script_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'python.exe' and script_name in process.cmdline():
            try:
                process.terminate()
                print("Script stopped successfully.")
            except psutil.NoSuchProcess:
                print("Failed to stop the script.")

script_name = 'Inference.py'

# Stop the script by name
# stop_script_by_name(script_name)


def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
        print("Script executed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to execute the script.")

# Run a script using its path
# Replace 'script.py' with the path to your script
script_path = 'Inference.py'

# run_script(script_path)