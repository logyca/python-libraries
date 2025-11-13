[← Return to the main README](../README.md "Return to the main project file")

# Developed with another tool or via console

## Creation of the virtual environment

🧰 Install Python on your operating system and locate the binary.
🔍📁 For this documentation, Python 3.11 has been downloaded and installed, and the binary is located in this path
    
        C:\python\python311\python.exe

## Automatic procedure

ℹ️ Navigate to the root of the samples directory and open a PowerShell console.
Edit the main.ps1 file and define the variable: $Env:PYTHON_BIN

Run the file

```powershgell
.\main.ps1
```

## Manual procedure

## Python Virtual environment

🧰 Open a console to run the following commands for the first time.
🔍📁 Navigate to the root of the samples directory and open a PowerShell console.

```Powershell
$python_bin="C:\python\python311\python.exe"
& $python_bin --version
& $python_bin -m pip install --upgrade pip
& $python_bin -m pip install virtualenv --upgrade
& $python_bin -m virtualenv venv
.\venv\Scripts\activate
python --version
python -m pip install --upgrade pip
```

## Execution of development commands
🔍📁 Navigate to the root of the samples directory and open a PowerShell console.

```Powershell
# When needed
pip install -r .\requirements.txt
```

```Powershell
# Connection test
python .\scripts\python\sample_01_conection_status.py
```

[← Return to the main README](../README.md "Return to the main project file")