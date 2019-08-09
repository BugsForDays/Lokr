"""
██╗      ██████╗ ██╗  ██╗██████╗
██║     ██╔═══██╗██║ ██╔╝██╔══██╗
██║     ██║   ██║█████╔╝ ██████╔╝
██║     ██║   ██║██╔═██╗ ██╔══██╗
███████╗╚██████╔╝██║  ██╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

****************************************************************************
|                   LOKR PASSWORD ENCRYTION MANAGER                        |
|   Created by petabite aka Philip Z(https://github.com/petabite)          |
****************************************************************************
"""

import pickle
import tkinter as tk
import os
from Crypt import Crypt
from LoginFrame import LoginFrame

# TODO: organize in folders
class Lokr(tk.Tk):
    ver = 1.1
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.lokr_file = ''
        self.user = ''
        self.wm_iconbitmap(self, default='closedlock.ico')
        self.logo = tk.PhotoImage(file='lock.png')
        self.title('LOKR LOGIN')
        self.minsize(350,200)
        plain_text_file = open('cset.dlokr', 'rb')
        cipher_text_file = open('cpcset.dlokr', 'rb')
        plain_text = pickle.load(plain_text_file)
        cipher_text = pickle.load(cipher_text_file)
        plain_text_file.close()
        cipher_text_file.close()
        self.crypt = Crypt(cipher_text, plain_text)
        LoginFrame(self)
        self.mainloop()


    def setUserLokrFile(self, username):
        self.user = username
        for file in os.listdir(os.getcwd()):
            #finds all lokr files in cwd
            if file == (self.crypt.encrypt(username, 11) + '.lokr'):
                self.lokr_file = file
        # for file in results:
        #     #sets f the current users' filename
        #     if file.startswith(self.crypt.encrypt(username, 11)):


    def parseLokrFile(self, filename, call): #helper
        #reads .lokr, input: file, call('keys', 'labels, or 'pwds'), returns: info in file as a list
        if filename.endswith('.lokr'):
            pcfn = filename
        else:
            pcfn = filename + '.lokr'
        f = open(pcfn, 'rb')
        f.seek(0)
        info = pickle.load(f)
        labels = list(info.keys())
        keys = []
        pwds = []
        for k, i in enumerate(list(info.keys())):
            keys.append((list(list(info.values())[k].keys())[0]))
        for k, i in enumerate(list(info.keys())):
            pwds.append((list(list(info.values())[k].values())[0]))
        if call == 'keys':
            return keys
        if call == 'labels':
            return labels
        if call == 'pwds':
            return pwds
        f.close()

    def readUsersFile(self):
        #reads USR file, returns: decrypted usr info as a dict in format: usr:pwd
        f = open('usrs.ulokr', 'rb')
        usrinfo = pickle.load(f)
        f.close()
        newdict = {}
        for k , v in usrinfo.items():
            newdict[self.crypt.decrypt(k, 7)] = self.crypt.decrypt(v, 7)
        return newdict

    def saveUser(self, usr, pwd):
        #appends usrname and pwd to USR file
        f = open('usrs.ulokr','rb')
        usrfile = pickle.load(f)
        f.close()
        usrfile[self.crypt.encrypt(usr, 7)] = self.crypt.encrypt(pwd, 7)
        f = open('usrs.ulokr','wb')
        pickle.dump(usrfile, f)
        f.close()

    def savePassword(self, filename, label, pwd, key):
        #appends encrypted pass, key, lbl to SL file
        enclbl = self.crypt.encrypt(label, key)
        encpwd = self.crypt.encrypt(pwd, key)
        # TODO: stream line lokr file, not extension guessing etc
        f = open(filename, 'rb')
        f.seek(0)
        whatsinside = pickle.load(f)
        f.close()
        whatsinside[enclbl] = {str(key) : encpwd}
        f = open(filename, 'wb')
        pickle.dump(whatsinside, f)
        f.close()

    def deletePassword(self, index):
        lbls = self.parseLokrFile(self.lokr_file, 'labels')
        fl = open(self.lokr_file, 'rb')
        fl.seek(0)
        info = pickle.load(fl)
        fl.close()
        del info[lbls[index]]
        fl = open(self.lokr_file, 'wb')
        pickle.dump(info,fl)
        fl.close()

    def decryptLokr(self, filename, info):
        #decrypts SL file, input: file, info('labels' or 'pwds'), returns: info as a list
        keys = self.parseLokrFile(filename, 'keys')
        labels =  self.parseLokrFile(filename,"labels")
        pwds = self.parseLokrFile(filename,"pwds")
        newlabels = [self.crypt.decrypt(labels[x], keys[x]) for x in range(len(keys))]
        newpwds = [self.crypt.decrypt(pwds[x], keys[x]) for x in range(len(keys))]
        if info == 'labels':
            return newlabels
        if info == 'pwds':
            return newpwds

    def authenticate(self, usr, pwd):
        #checks if usrname and pwd match, returns True if correct
        for user, password in self.readUsersFile().items():
            if user == usr and password == pwd:
                return True

    def createLokr(self, name):
        #creates new SL locker file with defaults
        f = open(self.crypt.encrypt(name, 11) + '.lokr', 'wb')
        pickle.dump({'ExampleLabel':{5:'ExamplePassword'}}, f)
        f.close()


lokr = Lokr()