import pandas as pd
import subprocess
import time
#import os


df = pd.read_csv('PC.csv', sep=" ", engine = 'python')
Name_PC = df['Name']
gr1 = Name_PC[0:200]
gr2 = Name_PC[200:400]
gr3 = Name_PC[400:600]
gr4 = Name_PC[600:]

print(Name_PC.nunique())

for n in Name_PC:
    #killsap = "TASKKILL /S " + n +" /IM saplogon.exe /IM NWBC.exe /f"
    #os.system(killsap)
    pr = subprocess.Popen('TASKKILL /S {} /IM saplogon.exe /IM NWBC.exe /f'.format(n))
    print(n, "Done")
    time.sleep(3)


#pr = subprocess.Popen('TASKKILL /S {} /IM saplogon.exe /IM NWBC.exe /f'.format('its-lt-2814'), stdout=subprocess.PIPE)
#print(pr.communicate())

