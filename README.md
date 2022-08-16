# python-django-project-to-exe
how to convert python django projects to exe


1- yeni bir cmd açın 
  win+x > çalıştır > "cmd" >[ENTER] 
  cd C:\Users\SDD\Desktop\toEXE 
  yada klasör yoluna cmd yazın enter basın  
  
2- venv aktif edin 
    cmd >> cd venv  # venv klasörü 
    cmd >> cd Scripts
    cmd >> activate.bat
    # cmd bu şekilde gözükmeli : (env) C:\Users\my-pc\Desktop\toExe\venv\Scripts>
    cmd >> cd ../
    cmd >> cd ../
    # cmd bu şekilde gözükmeli (env) C:\Users\my-pc\Desktop\toExe>
3- pyinstaller kurun 
  !daha önce global olarak kurmuş olabilirsiniz venv içinde kurulu olmalı. Kontrol etmek için cmd >> pip list 
  pip install pyinstaller

4- app.py dosyasını kendinize göre düzenleyin (port ayarı vs burada)
