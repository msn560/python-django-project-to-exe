# python-django-project-to-exe

### how to convert python django projects to exe
  
  
 #################################################  
# Formwork systems are examples, appearances #  
# think cmd enable venv #  
# edit app.py downloaded folder names port layout #  
# install pyinstaller and central #  
 #################################################  
  
  
1 - open a new cmd  
# win+x > run > "cmd" >[ENTER]  
cmd >> cd C:\\Users\[user name\]\\Desktop\\toEXE  
# or type cmd in the folder path and press enter  

2 - activate venv  
cmd >> cd venv # venv folder  
cmd >> cd Scripts  
cmd >> activate.bat  
cmd >> cd ../  
cmd >> cd ../  
# cmd should look like this >>> (env) C:\\Users\[user name\]\\Desktop\\toExe>  

3 - install pyinstaller  
cmd >> pip install pyinstaller  
# !you may have installed it globally before, it should be installed in venv. To check cmd >> pip list  

4 - Edit the app.py file according to you (port setting etc here)  

5 - Start the compiler  
cmd >> pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py  
# descriptions  
# --onefile = to get exe file only  
# --add-data "venv;venv" = we print the venv dir into our exe application  
# --add-data "djangoProject;djangoProject" = we print the djangoProject dir into our exe application  
# our app.py prelauncher file  

you app -> dist/app.exe
