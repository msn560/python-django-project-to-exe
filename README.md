# python-django-project-to-exe \n
how to convert python django projects to exe\n


1 - yeni bir cmd açın \n
    # win+x > çalıştır > "cmd" >[ENTER] \n
    cmd >> cd C:\Users\[user name]\Desktop\toEXE \n\n
    # yada klasör yoluna cmd yazın enter basın  \n
  
2 - venv aktif edin \n
    cmd >> cd venv  # venv klasörü \n
    cmd >> cd Scripts\n
    cmd >> activate.bat\n
    # cmd bu şekilde gözükmeli : (env) C:\Users\[user name]\Desktop\toExe\venv\Scripts>\n
    cmd >> cd ../\n
    cmd >> cd ../\n
    # cmd bu şekilde gözükmeli (env) C:\Users\[user name]\Desktop\toExe>\n
    
3 - pyinstaller kurun \n
    cmd >> pip install pyinstaller\n
    # !daha önce global olarak kurmuş olabilirsiniz venv içinde kurulu olmalı. Kontrol etmek için cmd >> pip list \n

4 - app.py dosyasını kendinize göre düzenleyin (port ayarı vs burada)\n

5 - Derleyiciyi başlatın\n
    cmd >> pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py \n
    # açıklamalar\n
    # --onefile = sadece exe dosyası elde etmek için\n
    # --add-data "venv;venv" = venv dosyalarını exe uygulamamızın içine yazdırıyoruz\n
    # app.py ön başlatıcı dosyamız\n
