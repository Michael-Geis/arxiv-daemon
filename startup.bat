@echo off
cd %ARXIV_DAEMON_PATH%
cmd /c "%ARXIV_DAEMON_PATH%\venv\scripts\pythonw.exe %ARXIV_DAEMON_PATH%\src\daemon.py"