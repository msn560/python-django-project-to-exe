 

 
# python-django-project-to-exe  
Django projesi EXE dosyasına nasıl dönüştürülür

## Adımlar

### 1 - Yeni bir CMD açın
```cmd
win+x > Çalıştır > "cmd" > [ENTER]
```
```cmd
cd C:\Users\[user name]\Desktop\toEXE
```
*Veya klasör yoluna `cmd` yazıp Enter'a basarak direkt açın*

### 2 - venv aktif edin
```cmd
cd venv
cd Scripts
activate.bat
```
*(Görünmesi gereken prompt)*  
`(env) C:\Users\[user name]\Desktop\toExe\venv\Scripts>`

```cmd
cd ../
cd ../
```
*(Görünmesi gereken prompt)*  
`(env) C:\Users\[user name]\Desktop\toExe>`

### 3 - PyInstaller kurun
```cmd
pip install pyinstaller
```
*Not: Globalde kurulu olsa bile venv içinde kurulu olduğundan emin olun (kontrol için `pip list`)*

### 4 - app.py dosyasını düzenleyin
- Port ayarları ve proje konfigürasyonunu bu dosyada yapın

### 5 - Derleyiciyi başlatın
```cmd
pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py
```

#### Parametre açıklamaları:
- `--onefile`: Tek EXE dosyası oluşturur
- `--add-data "venv;venv"`: venv dosyalarını EXE'ye ekler
- `--add-data "djangoProject;djangoProject"`: Django proje dosyalarını ekler

---

## 📌 Önemli Notlar
```
 
# Kalıp dosyaları örnektir, dizin şemasıdır                                 
# 1. CMD açıp venv aktif edin                                              
# 2. app.py dosyasını indirip klasör adlarını ve portu düzenleyin          
# 3. PyInstaller kurup çalıştırın                                         
```

*Windows path ayırıcı olarak `;` kullanıldığına dikkat edin*
 
