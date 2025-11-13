[← Return to the main README](../README.md "Return to the main project file")

# Developed using Microsoft Visual Studio Code

The automation files, used to prepare the virtual environment and run the scripts, are located in the `.vscode` folder.

tasks.json

    - task: PowerShell Create virtual environment
      
      Once the Python version has been selected and installed, the disk path to python_bin is configured to create the virtual environment. Commands are executed in the samples root folder.

    - task: PowerShell Delete Temporary Files:

      venv/
      tmp/
      logs/

launch.json

    Once created in a virtual environment, from vscode, by clicking on a file, for example: scripts/python/sample_01_connection_status.py, proceed to use the "Run and Debug (Ctrl+Shift+D)" option, which executes <sample>.py using the virtual environment.

```console
.\venv\Scripts\python.exe <sample>.py
```

[← Return to the main README](../README.md "Return to the main project file")
