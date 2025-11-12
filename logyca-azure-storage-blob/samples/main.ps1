<#
    #############################
    🔍📁 Navigate to the root of the samples directory and open a PowerShell console.
    cd ../samples/
    #############################
    ⚙️ Define the version of Python to use
    Note: PYTHON_BIN is the full disk path to the python.exe binary
    #############################
#>
    
$Env:PYTHON_BIN = "C:\python\python311\python.exe"

Write-Output "==============================================" ; `
    Write-Output "- Preparing the virtual environment in the operating system" `
    Write-Output "  * create_virtual_environment" ; `
    .\scripts\powershell\create_virtual_environment.ps1

Write-Output "==============================================" ; `
    Write-Output "- Activating virtual environment" ; `
    Write-Output "  *** Install the library dependencies within the active virtual environment." ; `
    .\venv\Scripts\activate ; `
    python -m pip install --upgrade pip ; `
    pip install -r .\requirements.txt ; `

Write-Output "==============================================" ; `
    Write-Output "- Running script app scripts/sample_01_conection_status.py" ; `
    python .\scripts\python\sample_01_conection_status.py ; `
    Write-Output "Connection test completed"

