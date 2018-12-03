REM Example If running from PythonProjecStructureFolder
REM Usage: bin\run_python.bat helloworld/runner.py

@ECHO OFF
setlocal
set PYTHONPATH=%CD%
python %1 %2
endlocal