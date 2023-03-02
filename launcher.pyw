importerror = False
try: import os
except: importerror = True
print(0)
from tkinter import *
print(1)
root = Tk()
root.resizable(width=False, height=False)
root.title('')
try: root.iconbitmap(default='icon.ico')
except: ...
root.geometry("+{}+{}".format(int(root.winfo_screenwidth()/2 - 185/2), int(root.winfo_screenheight()/2 - 130/2)))
print(2)
 
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


if cfgok:
    orig = Button(
        text="Genshin Impact", width=25, height=2,
        bg="black", fg="white", border='0',
        command=runorig)
    orig.pack()
    cult = Button(
        text="Cultivation", width=25, height=2,
        bg="black", fg="white", border='0',
        command=runcult)
    cult.pack()
    credit = Label(
        text='Made with ❤ by Sinya', width=25,
        bg="gray5", fg="white")
    credit.pack()
else: 
    importerror = Label(
        text='config.cfg is not configured\nor not exist', width=25,
        bg="black", fg="red")
    importerror.pack()


root.mainloop()
