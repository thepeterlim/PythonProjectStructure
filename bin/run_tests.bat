REM Example If running from PythonProjecStructureFolder
REM Usage: bin\run_tests.bat

@ECHO OFF
setlocal
set PYTHONPATH=%CD%
pytest
endlocal