@echo off
setlocal enabledelayedexpansion


set "lambda2=10.0"
set "h=0.001"
set "d2=1.0"
set "nameCase="Simulation of the Accordion Phenomenon""
set "lambda3=5.0"
set "d3=2.0"

if not "%~1"=="" set "lambda2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "d2=%~3"
if not "%~4"=="" set "nameCase=%~4"
if not "%~5"=="" set "lambda3=%~5"
if not "%~6"=="" set "d3=%~6"

python ../../../../PythonFile/Model1W3C_Equilibrium__CV_DV.py %lambda2% %h% %d2% %nameCase% %lambda3% %d3%

::exit /b
pause

