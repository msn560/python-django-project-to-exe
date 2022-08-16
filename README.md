# python-django-project-to-exe
<h3>how to convert python django projects to exe</h3></br> 

1 - open a new cmd</br>
    # win+x > run > "cmd" >[ENTER]</br>
    cmd >> cd C:\Users\[user name]\Desktop\toEXE</br>
    # or type cmd in the folder path and press enter</br>
  
2 - activate venv</br>
    cmd >> cd venv # venv folder</br>
    cmd >> cd Scripts</br>
    cmd >> activate.bat</br> 
    cmd >> cd ../</br>
    cmd >> cd ../</br>
    # cmd should look like this (env) C:\Users\[user name]\Desktop\toExe></br>
    
3 - install pyinstaller</br>
    cmd >> pip install pyinstaller</br>
    # !you may have installed it globally before, it should be installed in venv. To check cmd >> pip list</br>

4 - Edit the app.py file according to you (port setting etc here)</br>

5 - Start the compiler</br>
    cmd >> pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py</br>
    # descriptions</br>
    # --onefile = to get exe file only</br>
    # --add-data "venv;venv" = we print the venv dir into our exe application</br>
    # --add-data "djangoProject;djangoProject" = we print the djangoProject dir into our exe application</br>
    # our app.py prelauncher file</br>
	
you app -> dist/app.exe
