#Python Reference Layout
####Python project layout to be used as the standard layout
####This project assumes you're using pytest as testing framework
- bin: Contains scripts where you can run using shell/command prompt. 
Take note how current working directory is added to PythonPath.
  - run_tests.bat: runs all pytests in python project when using windows command prompt
  - run_python.bat: main script to run the app.
  - run_hello_world.sh: script to run the app when not using windows
- helloworld
  - package that holds most the main code
  - use runner.py as main entry point
  - see how different packages on broken out.  Not always necessary to break down to subpackages
  - see runner.py imports.  Would prefer absolute paths.
- tests
  - tests are broken down by the packages they are testing
- gitignore
  - list of common files/directories to ignore