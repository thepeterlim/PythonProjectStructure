REM Example If running from top level folder eg python reference layout
REM Usage: bin\run_tests.bat

@ECHO OFF
setlocal
set PYTHONPATH=%CD%
pytest
endlocal