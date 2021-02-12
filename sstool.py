###################################################################################################
#
#
# SSTool - By HyXFR
# Please contact into discord HyXFR#1231 for add cheats to the list (for md5 hash), only versions and mods !
# Availible on Windows, Linux and Other systems
# Requirements (for start ScreenShare): Python3, hashlib, mediafire, os, tkinter, pathlib, time
# Requirements (of this file) : Python3, tkinter
# It is recommanted to compile to .exe the screenshare (created) file, your MEDIAFIRE EMAIL AND PASSWORD are be writed into the file, ITS LARGELY RECOMMANDED TO CHANGE YOUR MEDIAFIRE PASSWORD AFTER A SCREENSHARE !
#
#
###################################################################################################
def write():
    repertory = repertorye.get()
    mf_email = mf_emaile.get()
    mf_password = mf_passworde.get()
    file_ss = file_sse.get()
    mods_repertory = mods_repertorye.get()
    versions_repertory = version_usede.get()
    
    with open(file_ss, 'w') as f:
        f.write("""
import hashlib

#Def

def getHash(filePath):
    fileObj = open(filePath, 'rb')
    md5 = hashlib.md5()
    while True:
        file = fileObj.read(8096)
        if not file:
            break
        md5.update(file)
    return md5.hexdigest()

#Config
repertory = \'""" + repertory + """\'
mf_email = \'""" + mf_email + """\'
mf_password = \'""" + mf_password + """\'
mods_repertory = \'""" + mods_repertory + """\'
versions_repertory = \'""" + versions_repertory + """\'
cheatlists_mods = [ #This is the "list" of cheats MODS, in the next of this, you can edit this by a md5 file hash, please contact me into discord (HyXFR#1231) if you have some cheats (in .jar file, please precise if it is a version or a mod), I can have the md5 hash of file for add here some clients.
    '587430c043ca3b1e0d366d168c869670' #Serenity Mod
    ]
cheatlists_ver = [ #This is the "list" of cheats VERSIONS, in the next of this, you can edit this by a md5 file hash, please contact me into discord (HyXFR#1231) if you have some cheats (in .jar file, please precise if it is a version or a mod), I can have the md5 hash of file for add here some clients.
        '8c0443868b9e46c77d39db61c755679d', #Aritois 1.12 Version
        'e066242c7ae7e43fdcf037b180bb4913' #Wurst 1.8 Version
        ]

from mediafire.client import (MediaFireClient, File, Folder)
import os
from tkinter import *
from pathlib import Path
import time
window = Tk()
window.title("Verify User")
window.geometry("480x160")
window.resizable(False, False)
def valider():
    def envoy_files():
        info.update()
        import mediafire
        
        try:
            client = MediaFireClient()
            client.login(email= mf_email,
                password= mf_password,
                app_id='42511')
        except mediafire.api.MediaFireApiError:
            window.title("Error : Invalid Connexion")
            return
        except:
            window.title("Connexion error 0")
            return
        
        try: #result file
            client.upload_file("results.txt", "mf:/result.txt")
            os.system('rm results.txt')
            window.title("Result file Sended")
        except KeyError:
            window.title("Result file Sended")
        except FileNotFoundError:
            window.title('Error : result File not found')
            return
        except:
            window.title("Error 0")
            with open("results.txt", "a") as f:
                f.write("Error 0 ")
                f.write(time.asctime())
                f.close()
        
        window.title("Sending mods File...") #Mods
        try:
            os.system('zip -r -q minecraft-mods ' + mods_repertory)
            client.upload_file("minecraft-mods.zip", "mf:/minecraft-mods.zip")
            os.system('rm minecraft-mods.zip')
            window.title("mods File Sended !")
        except KeyError:
            window.title("mods File Sended !")
        except FileNotFoundError:
            window.title('Error : mods File not found')
            return
        except:
            window.title("Error 0")
            with open("results.txt", "a") as f:
                f.write("Error 0 ")
                f.write(time.asctime())
                f.close()
        
        window.title("Sending versions File...") #Versions
        try:
            os.system('zip -r -q minecraft-versions ' + versions_repertory)
            client.upload_file("minecraft-versions.zip", "mf:/minecraft-versions.zip")
            os.system('rm minecraft-versions.zip')
            window.title("versions File Sended !")
        except KeyError:
            window.title("versions File Sended !")
        except FileNotFoundError:
            window.title('Error : Versions File not found')
            return
        except:
            window.title("Error 0")
            with open("results.txt", "a") as f:
                f.write("Error 0 ")
                f.write(time.asctime())
                f.close()
        
        try: #.minecraft file
            os.system('zip -r -q minecraft ' + repertory)
            client.upload_file("minecraft.zip", "mf:/minecraft-client.zip")
            os.system('rm minecraft.zip')
            window.title(".minecraft File Sended !")
        except KeyError:
            window.title(".minecraft File Sended !")
        except FileNotFoundError:
            window.title('Error : minecraft File not found')
            return
        except:
            window.title("Error 0")
            with open("results.txt", "a") as f:
                f.write("Error 0 ")
                f.write(time.asctime())
                f.close()
        
        
        
        
        window.title("All files sended !")
    
    def check_versions():
        hash = getHash(versions_repertory)
        if hash in cheatlists_ver:
            with open("results.txt", 'a') as f:
                f.write('Bad version :' + versions_repertory + '\\n')
                f.close()
    
    def check_mods():

        path = Path(mods_repertory)
        for child in path.iterdir():
            hash = getHash(str(child))
            if hash in cheatlists_mods:
                with open("results.txt", "a") as f:
                    f.write('Bad mod : ' + str(child) + '\\n')
                    f.close()
            else:
                with open("results.txt", "a") as f:
                    f.write('Safe mod : ' + str(child) + '\\n')
                    f.close()
    with open("results.txt", "w") as f:
        f.write("Versions and mods check RESULT ")
        f.write(time.asctime())
        f.write('\\n')
        f.close()
    
    check_versions()
    check_mods()
    envoy_files()
    
    
vide = Label(window, text="    ")
vide.grid(row=0, column=0)
mdpl = Label(window, text="In click on \\"Verify\\", you accept to send your .minecraft file to")
mdpl.grid(row=2, column=0)
mdpl = Label(window, text="a moderator. Also, your .minecraft was been scanned.")
mdpl.grid(row=3, column=0)
valid = Button(window, text="Verify", command=valider)
valid.grid(row=4, column=0)
info = Label(window, text=" ")
info.grid(row=4, column=1)
mainloop()
""")
        window.title("Successfull Created !")

import ppaw

from tkinter import *
window = Tk()
window.title("Create a SS-Tool")
window.geometry("480x240")
window.resizable(True, True)
pb = ppaw.pastebin.Pastebin("bad_api_key")
paste = pb.get_paste("DbTpaniK")
if paste.data == float(1.0):
    vide = Label(window, text="    ")
    vide.grid(row=0, column=0)
    repetoryl = Label(window, text="Repertory of .minecraft file:")
    repetoryl.grid(row=3, column=0)
    repertorye = Entry(window)
    repertorye.grid(row=3,column=1)
    file_ssl = Label(window, text="File for write :")
    file_ssl.grid(row=4, column=0)
    file_sse = Entry(window)
    file_sse.grid(row=4,column=1)

    mods_repertoryl = Label(window, text="Repertory of mods (used actually") 
    mods_repertoryl.grid(row=5, column=0)
    mods_repertorye = Entry(window)
    mods_repertorye.grid(row=5,column=1)
    text = Label(window, text=", e.g. : c:\.minecraft\mods\1.7.10:")
    text.grid(row=6,column=0)
    version_usedl = Label(window, text="Version of user (the .jar in actual version) : ")
    version_usedl.grid(row=7, column=0)
    version_usede = Entry(window)
    version_usede.grid(row=7,column=1)

    mf_emaill = Label(window, text="Email of mediafire account :")
    mf_emaill.grid(row=8, column=0)
    mf_emaile = Entry(window)
    mf_emaile.grid(row=8,column=1)
    mf_passwordl = Label(window, text="Password of mediafire account :")
    mf_passwordl.grid(row=9, column=0)
    mf_passworde = Entry(window, show="●")
    mf_passworde.grid(row=9,column=1)

    valid = Button(window, text="Create", command=write)
    valid.grid(row=10, column=1)
    mainloop()
else:
    vide = Label(window, text="    ")
    vide.grid(row=0, column=0)
    text1 = Label(window, text="New version of this program has released")
    text1.grid(row=1, column=0)
    text2 = Label(window, text="Download at https://github.com/HyXFR/ss-tool")
    text2.grid(row=2, column=0)
    
