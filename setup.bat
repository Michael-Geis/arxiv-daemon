@echo off
setx ARXIV_DAEMON_PATH %~dp0
cmd /c "%~dp0\venv\scripts\python.exe %~dp0\src\setup.py"
