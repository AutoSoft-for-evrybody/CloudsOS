import os
import files
from time import sleep
from tkinter import *
import sys
from colorama import Fore, Back, Style, init
 
init(wrap=True)
color = Fore.GREEN
#drives = files.Drives("drives.cvd")
import socket
a = 0
b = 0
c = 0
d = 0
sock = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
print(color + Style.BRIGHT + Back.BLUE + "╔═════════════════════════════════════════════╗")
print(color + Style.BRIGHT + Back.BLUE + "║  Добро пожаловать в CloudsOS!               ║")
print(color + Style.BRIGHT + Back.BLUE + "║  Это русская ОС, с открытым исходным кодом. ║")
print(color + Style.BRIGHT + Back.BLUE + "║                                             ║")
print(color + Style.BRIGHT + Back.BLUE + "║  Для справки введите                        ║")
print(color + Style.BRIGHT + Back.BLUE + "║  HELP                                       ║")
print(color + Style.BRIGHT + Back.BLUE + "║                                             ║")
print(color + Style.BRIGHT + Back.BLUE + "║  Copyright(c)AutoSoft for everybody         ║")
print(color + Style.BRIGHT + Back.BLUE + "║                                             ║")
print(color + Style.BRIGHT + Back.BLUE + "╚═════════════════════════════════════════════╝")
print(color + Style.BRIGHT + Back.BLUE + "Ваш IP:"+ip)



print(Back.BLACK + '')
#drives.chdir('.')
open_dilog = False

def IDEL():
    print('''
╔═══════════════════════════════════════╗
║  Copyright(c)AutoSoft for everybody   ║
║  CM-SCRIPT IDLE                       ║
╚═══════════════════════════════════════╝
╔═══════════════════════════════════════════════════════╗''')
    app_num = int(input(' Количевство строк в коде(Обезательно):'))
    app_commands = list()
    for range_in_app in range(app_num):
        app_cmd = input()
        app_commands.append(app_cmd)
    print('''╚═══════════════════════════════════════════════════════╝''')
    print('ВЫВОД')
    print('═══════════════════════════════════════════════════════')
    inputs = []
    randoms = list()
    for appLine in app_commands:
        if 'say' in appLine:
            if 'inputic_method' in appLine[3:]:
                num_inp = int(appLine[18:])
                print(inputs[num_inp])
            elif 'rand_method' in appLine[3:]:
                num_rand_meth = int(appLine[15:])
                print(randoms[num_rand_meth])
            else:
                print(appLine[3:])
        if 'input' in appLine:
            inputic = input()
            inputs.append(inputic)
                
        if 'random' in appLine:
            import random
            random = random.randint(int(appLine[7:8]), int(appLine[9:]))
            randoms.append(random)


while True:# цикл пока не завершит работу
    cmd = input('CloudsOS v2.5>')
    if open_dilog == True:
            os.chdir('C:\cloudsOS\OS system files\dilogs')
            op = input('введити имя диолога без расширения:')
            bro = open(op+'.cdf', 'r')
            for dioLine in bro:
                cmd = dioLine
            open_dio = False
    if cmd == 'HELP':#Ну ты понял
        print('''
cd .../path/ - перейти в директорию path,
dir - список того что есть в директории,
dir_here - рабочия директория
HELP - помощник,
INFO - INFO об ОС,
list_apps - список предложений,
open_app - открыть предложение,
DEVOLOPER_TYPE - режим разроботчика

        ''')
    elif 'cd' in cmd:
        os.chdir(cmd[3:])
    elif cmd == 'dir':
        for dir in os.listdir(path='.'):
            
            if '.csi' in dir:
                print(dir + '  - installer file')
                print('''
       █
      ███
     █ █ █
       █
       
    ████████
    ████████
    ████████
    ''')
                
            else:
                print(dir)
                print('-----------------------------------')
    elif cmd == 'DEVOLOPER_TYPE':
        DEVOLOPER_TYPE = True
        print("╔════════════╦════════════╗")
        print("║ 1 - IDLE   ║ 2 - DEL    ║")
        print("╠════════════╬════════════╣")
        print("║ 3 - HELPER ║ 4 - QUIT   ║")
        print("╠════════════╩════════════╣")
        print("║ 5 - INSTALL APP         ║")
        print("╠═════════════════════════╣")
        print("║ 6 - IP                  ║")
        print("╚═════════════════════════╝")
        while DEVOLOPER_TYPE:
            DEVOLOPER_CMD =int(input('DEVOLOPER_TYPE>'))
            if DEVOLOPER_CMD == 4:
                DEVOLOPER_TYPE = False
            if DEVOLOPER_CMD == 6:
                print('ip: ' + ip)
            if DEVOLOPER_CMD == 5:
                print('Место положения csi(тип: D:\crazy_girls\i_am_crazy_girl\yes)')
                installer_dir = input()
                print('Название CSI:')
                name_CSI = input()
                os.chdir(installer_dir)
                install = False
                for dir in os.listdir(path='.'):
                    if dir == name_CSI:
                        install = True
                if install == True:
                    print('Установка...')
                    print('''

              ██
            ██████
          ███ ██ ██
              ██
              ██
      ███████ ██ ██████
     █        ██       █
    █                   █
    █████████████████████
    █████████████████████
    █████████████████████
    █████████████████████
    █████████████████████
    █████████████████████
    █████████████████████
                    ''')
                    os.chdir('C:\CloudsOS\APPS')
                    os.mkdir('APP_' + name_CSI[:(len(name_CSI)-4)])
                    os.chdir('APP_' + name_CSI[:(len(name_CSI)-4)])
                    f = open('APP.csf', 'tw')
                    install = open(installer_dir+'/'+name_CSI)
                    for appLine_install in install:
                        f.write(appLine_install)
                    f.close()
                    install.close()
                    print('''
╔════════════════════════════════╗
║ ██████████████████████████████ ║
╚════════════════════════════════╝
             100%
                    ''')
                    print('IP:'+ip+', Установлено из пакета '+name_CSI)

                
            if DEVOLOPER_CMD == 3:
                print('''
Copyright(c) AutoSoft for everybody
-----------------ИНСТРУКЦИЯ К ЯЗЫКУ CM-SCRIPT------------
Язык прогроммирования CM-SCRIPT в данный момент содержит
всего несолько команд, давайте начнём!


code-------------------------------

say Hello, world!

-----------------------------------
 данная программа выводит надпись Hello, world! 
 Вобщем пишем say, делаем пробел, и БЕЗ КЛВЫЧЕК
 И СКОБОК пишем что хотим вывести.

 INPUT

code-------------------------------

input
say inputic_method 0

input
say inputic_method 1

-----------------------------------

И так эта программа считовает строку,
и пичатает её же.
И ещё раз считывает строку и пичатает.
Как работает?  input, считаванье строки,
enter, say inputic_method ИНДЕКС.
где ИНДЕКС там индекс инпута.

 RANDOM

code---------------------------------

random 1 6
say rand_method 0
random 1 5
say rand_method 1

--------------------------------------
 
 Эта программа выводит два рандомных числа
 Первое от 1 до 6
 Второе от 1 до 5
 Смысл понятен.


-----------------------------------------------------
Copyright(c) 2020 AutoSoft for everybody
                ''')
                input('Нажмите ввод для тоблицы действий')
                print("╔════════════╦════════════╗")
                print("║ 1 - IDLE   ║ 2 - DEL    ║")
                print("╠════════════╬════════════╣")
                print("║ 3 - HELPER ║ 4 - QUIT   ║")
                print("╚══╦═════════╩════════╦═══╝")
                print("   ║ 5 - INSTALL_APP  ║    ")
                print("   ╚══════════════════╝    ")
            if DEVOLOPER_CMD == 2:
                print('Какой апплет хотите удалить?')
                APPLET = input('Название без APP_)')
                import shutil
                shutil.rmtree('C:\CloudsOS\APPS\APP_'+APPLET)
                print('''


          █████████
          ███   ███
          █████████



    ███████████████████
     ████████████████
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ██ ██ ██ ██ ██ █
     ████████████████


''')
     
                print('ГОТОВО')
            if DEVOLOPER_CMD == 1:
                IDEL()
                       
    elif cmd == 'INFO':
        print('Продукт от AutoSoft for everybody, cloudOS v2.5')#Здесь понятно
        color = Fore.WHITE
        print(color + '███████████████')
        color = Fore.BLUE
        print(color + '███████████████')
        color = Fore.RED
        print(color + '███████████████')
        color = Fore.GREEN
        print(color + 'Made in Russia')
    elif cmd == 'list_apps':
        os.chdir('C:\cloudsOS\Apps')
        listapps = os.listdir()
        for apps in range(0, len(listapps)):
            print(listapps[apps])
    elif 'open_app' in cmd:# здесь ядро
        print("══════════════════════Запуск приложения══════════════════════")
        cmd_s = input('Название приложения(Без APP_):')
        os.chdir('c:\cloudsOS\APPS\APP_' + cmd_s)
        inputs = list()
        randoms = list()
        tk_TRUE = False
        app_open = open('APP.csf', "r")
        for appLine in app_open:
            if 'say' in appLine:
                if 'inputic_method' in appLine[3:]:
                    num_inp = int(appLine[18:])
                    print(inputs[num_inp])
                elif 'rand_method' in appLine[3:]:
                     num_rand_meth = int(appLine[15:])
                     print(randoms[num_rand_meth])
                else:
                    print(appLine[3:])
            if appLine == 'open FILE':
                open_TR_or_FL = False
                open_file = ''
                drives.chdir('c:\\')
                print('Выберете файл, директория C:\\')
                cmd = input('openFILE_cmd>')
                if cmd == 'HELP':
                    print('''
cd .../path/ - перейти в директорию path,
dir - список того что есть в директории,
open - выбор
                    ''')
                if 'cd' in cmd:
                    os.chdir(cmd[3:])
                if cmd == 'dir':
                    listdirs = os.listdir(path='.')
                    for dirs in range(0, len(listdirs)):
                        print(listdirs[dirs])
                if 'open' in cmd:
                    open_TR_or_FL = True
                    open_file = cmd[3:]
            if 'input' in appLine:
                inputic = input()
                inputs.append(inputic)
                
            if 'random' in appLine:
                import random
                random = random.randint(int(appLine[7:8]), int(appLine[9:]))
                randoms.append(random)
            
#Main code end

#НАШИ ЛЮБИМЫЫЫЫЕ ПОСХАААААААААЛООООЧКИИИИИИИИИИИИИИИИИИИИИ!... Copyright
                
    elif cmd == 'Gimn':
        print('Подпивай!')
        print('''

Радость, пламя неземное,    
Райский дух, слетевший к нам,
Опьяненные тобою,
Мы вошли в твой светлый храм.
Ты сближаешь без усилья
Всех разрозненных враждой,
Там, где ты раскинешь крылья,
Люди — братья меж собой.

Хор
Обнимитесь, миллионы!
Слейтесь в радости одной!
Там, над звёздною страной, -
Бог, в любви пресуществлённый!

Кто сберёг в житейской вьюге
Дружбу друга своего,
Верен был своей подруге, -
Влейся в наше торжество!
Кто презрел в земной юдоли
Теплоту душевных уз,
Тот в слезах, по доброй воле,
Пусть покинет наш союз!

Хор
Всё, что в мире обитает,
Вечной дружбе присягай!
Путь её в надзвездный край,
Где Неведомый витает.

        ''')
        import winsound
        winsound.PlaySound("START.WAV", winsound.SND_ASYNC)
        
    elif cmd == 'interstellar_listen':
        print('''
'Не уходи смиренно, в сумрак вечной тьмы,
Пусть тлеет бесконечность в яростном закате.
Пылает гнев на то, как гаснет смертный мир,
Пусть мудрецы твердят, что прав лишь тьмы покой.
И не разжечь уж тлеющий костёр.
Не уходи смиренно в сумрак вечной тьмы,
Пылает гнев на то, как гаснет смертный мир.'
''')
    elif cmd == 'AMERICA':
        color_star = Fore.BLUE
        color_white = Fore.WHITE
        color_red = Fore.RED
        print((color_star + '████████') + (color_red + '██████████████████████'))
        print((color_star + '████████') + (color_white + '██████████████████████'))
        print(color_red + '██████████████████████████████')
        print(color_white + '██████████████████████████████')
        print(color_red + '██████████████████████████████')
        print(color + '')
        


    else:
        color = Fore.RED
        print(color + '''
███████████████
█████    ██████
█████    ██████
█████    ██████
█████    ██████
█████    ██████
███████████████
█████    ██████
███████████████
''')
        color = Fore.GREEN
        print(color + 'ERROR '+cmd+';')
