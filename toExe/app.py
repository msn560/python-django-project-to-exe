from subprocess import Popen, PIPE
import os 

port = 7000

print("python venv activate")
#opening cmd and start venv
p1 = Popen([  os.path.dirname(os.path.abspath(__file__)) + "/env/Scripts/activate.bat"], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
#print(p1.communicate())
#or
p1.wait()

print("server is starting")
print("server port:",port)
new_arg = [ "python",os.path.dirname(os.path.abspath(__file__)) +"/DjangoProject/manage.py","runserver",str(port)] 
#the cmd code run looks like this
#python {this dir}/project/manage.py runserver 7000
p2 = Popen(new_arg, stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True) 
print(p2.communicate())

#active venv -> readme.txt
#pyinstaller --onefile --add-data "venv;venv" --add-data "djangoProject;djangoProject" app.py 
