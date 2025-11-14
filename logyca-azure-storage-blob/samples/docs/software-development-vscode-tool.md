[← Return to the main README](../README.md "Return to the main project file")

# 🖥️ Developed using Microsoft Visual Studio Code

The automation files, used to prepare the virtual environment and run the scripts, are located in the `.vscode` folder.

## File Descriptions

  📄 File: `tasks.json`. 👉 Documented below:  🧭 Running *Tasks*

      - task: PowerShell Create virtual environment
        
        Once the Python version has been selected and installed, the disk path to python_bin is configured to create the virtual environment. Commands are executed in the samples root folder.

      - task: PowerShell Delete Temporary Files:

        venv/
        tmp/
        logs/

  📄 File: `launch.json`. 👉 Documented below:  🐞 Running *Launch Configurations*

      Once created in a virtual environment, from vscode, by clicking on a file, for example: scripts/python/sample_01_connection_status.py, proceed to use the "Run and Debug (Ctrl+Shift+D)" option, which executes <sample>.py using the virtual environment.

      The script will be executed using the assigned virtual environment binary.
      > .\venv\Scripts\python.exe ... <sample>.py

## ▶️ Execution modes 

### 🧭 Running *Tasks*

#### ⌨️ Keyboard method

1. Press:  
   **Ctrl + Shift + P** (Windows / Linux)  
   **Cmd + Shift + P** (macOS)
2. Type:  
   **Tasks: Run Task**
3. Press **Enter**
4. Select the task you want to run.

---

#### 🖱️ Mouse method

1. Open the menu:  
   **View → Command Palette…**
2. Type **Tasks: Run Task**
3. Click on the option.
4. Select the task from the list.

### 🐞 Running *Launch Configurations* (Run / Debug)

Launch configurations in `.vscode/launch.json` allow running or debugging Python scripts in a controlled way.

#### ⌨️ Keyboard method

- **F5** → Start debugging  
- **Ctrl + F5** → Run without debugging  

To select another configuration:

1. Press **Ctrl + Shift + P**
2. Type: **Debug: Select and Start Debugging**
3. Select the desired launch configuration.

---

#### 🖱️ Mouse method

1. Open the **Run and Debug** view (icon ▶️🐞).
2. At the top, select the launch configuration from the dropdown menu.
3. Click:
   - ▶️ **Run** to execute  
   - ▶️🐞 **Start Debugging** to debug  



[← Return to the main README](../README.md "Return to the main project file")
