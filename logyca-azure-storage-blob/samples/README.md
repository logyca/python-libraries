# 🧱 Project Description

📝 Nombre: logyca-azure-storage-blob

🧰 Examples of SDK calls to interact with the Azure Storage blob container service using Python

In this examples folder, you'll find console scripts for tasks such as uploading, downloading, modifying properties, deleting, and searching for files by modification date.

```console
pip install -r .\requirements.tx
```

# Project Structure

```
.
├── .vscode/                   # VS Code workspace settings folder
├── docs/                      # Documentation files
├── scripts/                   # Folder for supporting scripts
├── venv/                      # Virtual environment folder
├── .env                       # Environment variables that must be created based on .env.sample
├── .env.sample                # Sample environment variables without sensitive data
├── .gitignore                 # Git ignore file to exclude unnecessary files
├── main.ps1                   # PowerShell file that automates the creation of prerequisites and running the first sample script.
├── pdtes.md                   # Markdown file for additional documentation
├── README.md                  # Project overview and setup guide
├── requirements.txt           # List of Python dependencies
```

# ☁️🛢️ Azure Storage account | 🛡️ 🔐 access keys

- Copy the environment variable template located in the root of the `.env.sample` directory to a file named `.env` in the same directory.
- 🗝️ Obtain the access keys and write them to `.env`

# 🧠 Examples of SDK calls to interact with the Azure Storage Account Blob Container Service using Python

The sample scripts are designed to run sequentially.
Therefore, the credentials in the `.env` environment variable file are tested initially, followed by the creation of test containers.
Then, the scripts perform actions such as loading, unloading, modifying properties, deleting, and searching for files by modification date.

The sequence is: sample_01..sample_99

# 📚 Documentation Contents

| **Description**                                                                          | **Location / Link**                                                                        |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Main documentation file. Provides general overview, installation and usage instructions. | [README.md](README.md)                                                                     |
| Development setup using **Visual Studio Code**.                                          | [Developed using Microsoft Visual Studio Code](docs/software-development-vscode-tool.md)   |
| Alternative development setup using other tools or console.                              | [Developed with another tool or via console](docs/software-development-another-tool.md)    |
| Troubleshooting related to logging configuration and errors.                             | [Logging troubleshooting](docs/troubleshooting-logging.md)                                 |
