# python-django-project-to-exe
how to convert python django projects to exe

## Translated from Turkish to English using google translate -- translate.google.com

1 - open a new cmd
    # win+x > run > "cmd" >[ENTER]
    cmd >> cd C:\Users\[user name]\Desktop\toEXE
    # or type cmd in the folder path and press enter
  
2 - activate venv
    cmd >> cd venv # venv folder
    cmd >> cd Scripts
    cmd >> activate.bat
    # cmd should look like this : (env) C:\Users\[user name]\Desktop\toExe\venv\Scripts>
    cmd >> cd ../
    cmd >> cd ../
    # cmd should look like this (env) C:\Users\[user name]\Desktop\toExe>
    
3 - install pyinstaller
    cmd >> pip install pyinstaller
    # !you may have installed it globally before, it should be installed in venv. To check cmd >> pip list

4 - Edit the app.py file according to you (port setting etc here)

5 - Start the compiler
    cmd >> pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py
    # descriptions
    # --onefile = to get exe file only
    # --add-data "venv;venv" = we print the venv files into our exe application
    # our app.py prelauncher file