# logyca-azure-storage-blob

Examples of SDK calls to interact with the Azure Storage blob container service using Python

In this examples folder, you'll find console scripts for tasks such as uploading, downloading, modifying properties, deleting, and searching for files by modification date.

```console
pip install -r .\requirements.tx
```
# Azure Storage account access keys

- 🔒 Copy the environment variable template located in the root of the `.env.sample` directory to a file named `.env` in the same directory.
- 🔐⚠️ Obtain the access keys and write them to `.env.`

# Examples of SDK calls to interact with the Azure Storage Account Blob Container Service using Python

The sample scripts are designed to run sequentially. Therefore, the credentials in the .env environment variable file are tested initially, followed by the creation of test containers. Then, the scripts perform actions such as loading, unloading, modifying properties, deleting, and searching for files by modification date.

The sequence is: sample_01..sample_99

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

# Developed with another tool or via console

Configure virtual environment using console commands and run the console scripts with another tool or without a graphical environment.

[Manual: Developed with another tool](docs/virtual-environment-configuration)

# Other documents

[Troubleshooting](docs/troubleshooting.md)
