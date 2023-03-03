importerror = False
try: import os, webbrowser
except: importerror = True
from tkinter import *
root = Tk()
root.resizable(width=False, height=False)
root.title('')
root.configure(bg='gray5')
try: root.iconbitmap(default='icon.ico')
except: ...

width = 25
root.geometry("+{}+{}".format(int(root.winfo_screenwidth()/2 - 185/2), int(root.winfo_screenheight()/2 - 130/2)))
 
path = {}


def runcult():
    print('--- Running Cultivation launcher ---')
    print(f'[1/2] Moving version.dll file to game path')
    print(f'      version_dll_path: {path["version_dll_path"]}')
    print(f'      game_path: {path["game_path"]}')
    
    with open(path["version_dll_path"], 'rb',) as prefdll:
        with open(path["game_path"]+'\\version.dll' if path["game_path"][:-1] != '\\' else path["game_path"]+'version.dll','wb') as newdll:
            newdll.write(bytes(prefdll.read()))
    
    print(f'\n[2/2] Running launcher')
    print(f'      cultivation_launcher: {path["cultivation_launcher"]}')
    
    root.destroy()
    try: os.system(path["cultivation_launcher"] if " " not in path["cultivation_launcher"] else f'"{path["cultivation_launcher"]}"')
    except: pass
    exit()
    
            

def runorig():
    print('--- Running Genshin Impact launcher ---')
    print(f'[1/2] Removing version.dll file from game path')
    print(f'      game_path: {path["game_path"]}')
    
    
    try: os.remove(path["game_path"]+'\\version.dll' if path["game_path"][:-1] != '\\' else path["game_path"]+'version.dll')
    except: pass
    
    print(f'\n[2/2] running launcher')
    print(f'      original_launcher: {path["original_launcher"]}')
    

    root.destroy()
    try: os.system(path["original_launcher"] if " " not in path["original_launcher"] else f'"{path["original_launcher"]}"')
    except: pass
    exit()
try:
    
    with open('config.cfg', 'r', encoding='utf-8') as file: 
        for line in file.readlines(): path[line.split('=')[0]] = line.split('=')[1].replace('\n','')
        print(path)
    if path['original_launcher'] != '' and path['cultivation_launcher'] != '' and path['game_path'] != '' and path['version_dll_path'] != '': cfgok = True
    else: cfgok = False
except: cfgok = False

def createcfg():
    with open('config.cfg','w',encoding='utf-8') as file: file.write('original_launcher=\ncultivation_launcher=\ngame_path=\nversion_dll_path=')
    root.destroy()
    exit()

def gotogit():
    root.destroy()
    webbrowser.open('https://github.com/ktnk-dev/RefrigeratorLauncher')
    exit()

def gotowebsite():
    root.destroy()
    webbrowser.open('https://frige.sinya.ru')
    exit()


if cfgok:
    Button(
        text="Genshin Impact", width=width, height=2,
        bg="black", fg="white", border='0',
        command=runorig).pack()
    Button(
        text="Cultivation", width=width, height=2,
        bg="black", fg="white", border='0',
        command=runcult).pack()
else: 
     Label(
        text='config.cfg is not configured\nor not exist', width=width,
        bg="black", fg="red").pack()
     
     Button(
        text="Create config.cfg", width=width, height=2,
        bg="black", fg="white", border='0',
        command=createcfg).pack()


creditbuttons = Frame(root)
creditbuttons.config(bg='gray5', width=width)
creditbuttons.pack(side=BOTTOM)
Button(creditbuttons,
    text='Github', width=10, border='0', 
    bg="gray5", fg="white",
    command=gotogit).pack(side=LEFT)
Button(creditbuttons,
    text='Website', width=10, border='0', 
    bg="gray5", fg="white",
    command=gotowebsite).pack(side=RIGHT)

credit = Frame(root)
credit.pack(side=BOTTOM)
Label(credit,
    text='Made with ❤ by Sinya', width=width,
    bg="gray5", fg="white").pack()
root.mainloop()
