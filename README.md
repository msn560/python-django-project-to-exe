 
# python-django-project-to-exe  
How to convert a Django project to an EXE file

## Steps

### 1 - Open a new CMD
```cmd
win+x > Run > "cmd" > [ENTER]
```
```cmd
cd C:\Users\[user name]\Desktop\toEXE
```
*Or type `cmd` in the folder path address bar and press Enter*

### 2 - Activate venv
```cmd
cd venv
cd Scripts
activate.bat
```
*(Expected prompt)*  
`(env) C:\Users\[user name]\Desktop\toExe\venv\Scripts>`

```cmd
cd ../
cd ../
```
*(Expected prompt)*  
`(env) C:\Users\[user name]\Desktop\toExe>`

### 3 - Install PyInstaller
```cmd
pip install pyinstaller
```
*Note: Even if installed globally, ensure it's installed in venv (check with `pip list`)*

### 4 - Edit app.py file
- Configure port settings and project configuration in this file

### 5 - Start the compiler
```cmd
pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py
```

#### Parameter explanations:
- `--onefile`: Creates a single EXE file
- `--add-data "venv;venv"`: Includes venv files in EXE
- `--add-data "djangoProject;djangoProject"`: Includes Django project files

---

## 📌 Important Notes
``` 
# Template files show directory structure                                  
# 1. Open CMD and activate venv                                            
# 2. Download app.py and modify folder names/port                         
# 3. Install and run PyInstaller                                           
```

*Note: Windows uses `;` as path separator in PyInstaller commands*
```

Key changes made:
1. Translated all Turkish text to English
2. Maintained original code blocks and structure
3. Kept Windows-specific commands intact
4. Preserved markdown formatting
5. Added proper technical terminology for Django/PyInstaller context

The English version maintains the exact same technical instructions while making it accessible to international developers.
