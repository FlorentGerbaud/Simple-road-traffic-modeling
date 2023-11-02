@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=2.0"
set "h=0.0001"

:: Check if the first argument is provided and use it if available
if not "%~1"=="" set "a2=%~1"

:: Check if the second argument is provided and use it if available
if not "%~2"=="" set "h=%~2"

:: Run the Python script with the provided or default arguments
python ../../../../PythonFile/Model1W2C_Equilibrium_CV.py %a2% %h%

:: Exit the batch script
exit /b
