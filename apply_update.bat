@echo off
cd /d "%~dp0"
py -3 update_index.py
if errorlevel 1 python update_index.py
pause
