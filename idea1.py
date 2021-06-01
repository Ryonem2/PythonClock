from win10toast import ToastNotifier
from datetime import datetime
import win32com.client
import smtplib
import os
import time
import math


hr = int(input("Hr => "))
mn = int(input("Min => "))
sc = int(input("Sec => "))
to = input(str("EnterEmailYouWannaSend : "))
gmail_user = 'YOUR-EMAIL'
gmail_pwd = input(str("EnterYourPassword : "))
progress = 3
starttime = time.time()
timer = 1
presentime = datetime.now()
hourss = presentime.hour
hrP = hourss*60*60
hrP2 = hr*60*60
minss = presentime.minute
minP = minss*60
minP2 = mn*60
secss = presentime.second
sums1 = hrP + minP + secss
sums2 = hrP2 + minP2 + sc
sums = sums2 - sums1
result = sums/100
result = round(result,2)
trigger = 1


# print("Time was set")
# print("Now Progress = ",progress," %")
while True:
    # print(timer)
    presentime = datetime.now()
    hour = presentime.hour
    mins = presentime.minute
    sec = presentime.second

    if progress != 100:
        progress = progress + 1
    else:
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Time was set")
    print("Now Progress = ",progress," %")
    print("Now Time is => ",hour,".",mins,".",sec)
    if(progress < 5):
        print("|--------------------|")
    elif (progress <= 5):
        print("|▮-------------------|")
    elif (progress <= 10):
        print("|▮▮------------------|")
    elif (progress <= 15):
        print("|▮▮▮-----------------|")
    elif (progress <= 20):
        print("|▮▮▮▮----------------|")
    elif (progress <= 25):
        print("|▮▮▮▮▮---------------|")
    elif (progress <= 30):
        print("|▮▮▮▮▮▮--------------|")
    elif (progress <= 35):
        print("|▮▮▮▮▮▮▮-------------|")
    elif (progress <= 40):
        print("|▮▮▮▮▮▮▮▮------------|")
    elif (progress <= 45):
        print("|▮▮▮▮▮▮▮▮▮-----------|")
    elif (progress <= 50):
        print("|▮▮▮▮▮▮▮▮▮▮----------|")
    elif (progress <= 55):
        print("|▮▮▮▮▮▮▮▮▮▮▮---------|")
    elif (progress <= 60):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮--------|")
    elif (progress <= 65):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮-------|")
    elif (progress <= 70):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮-------|")
    elif (progress <= 75):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮------|")
    elif (progress <= 80):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮-----|")
    elif (progress <= 85):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮----|")
    elif (progress <= 90):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮--|")
    elif (progress <= 99):
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮-|")
    else:                      
        print("|▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮|")

    time.sleep(result)  

   

mailserver = smtplib.SMTP("smtp.gmail.com",587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
#! https://myaccount.google.com/lesssecureapps?pli=1 set that to mini secure!!!!!!
mailserver.login(gmail_user, gmail_pwd)
print("login Secessful!!")
print("Alarm was setted!")
msg = 'Hey Time to work now get back to work'
mailserver.sendmail(gmail_user, to, msg)
print ('Email was sent!!')
mailserver.quit()
