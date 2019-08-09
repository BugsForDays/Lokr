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
# TODO: rename variables
class Lokr(tk.Tk):
    ver = 1.1
   
    def __init__(self):
        # init main window
        tk.Tk.__init__(self)
        self.lokr_file = ''
        self.user = ''
        self.wm_iconbitmap(self, default='closedlock.ico')
        self.logo = tk.PhotoImage(file='lock.png')
        self.title('LOKR LOGIN')
        self.minsize(350, 200)
        plain_text_file = open('cset.dlokr', 'rb')
        cipher_text_file = open('cpcset.dlokr', 'rb')
        plain_text = pickle.load(plain_text_file)
        cipher_text = pickle.load(cipher_text_file)
        plain_text_file.close()
        cipher_text_file.close()
        self.crypt = Crypt(cipher_text, plain_text)
        LoginFrame(self)
        self.mainloop()
        
    # PASSWORD MANIPULATION METHODS
    
    def savePassword(self, label, pwd, key):
        # appends encrypted pass, key, lbl to user's .lokr file
        enclbl = self.crypt.encrypt(label, key)
        encpwd = self.crypt.encrypt(pwd, key)
        f = open(self.lokr_file, 'rb')
        f.seek(0)
        whatsinside = pickle.load(f)
        f.close()
        whatsinside[enclbl] = {str(key) : encpwd}
        f = open(self.lokr_file, 'wb')
        pickle.dump(whatsinside, f)
        f.close()

    def editPassword(self, index, label, pwd):
        keys = self.parseLokrFile("keys")
        self.deletePassword(index)
        self.savePassword(label, pwd, int(keys[index]))

    def deletePassword(self, index):
        # delete password from user's .lokr
        lbls = self.parseLokrFile('labels')
        fl = open(self.lokr_file, 'rb')
        fl.seek(0)
        info = pickle.load(fl)
        fl.close()
        del info[lbls[index]]
        fl = open(self.lokr_file, 'wb')
        pickle.dump(info, fl)
        fl.close()

        
    # USER MANAGEMENT METHODS
    
    def setUserLokrFile(self, username):
        # set user's lokr file
        self.user = username
        for file in os.listdir(os.getcwd()):
            if file == (self.crypt.encrypt(username, 11) + '.lokr'):
                self.lokr_file = file

    def readUsersFile(self):
        # reads USR file, returns: decrypted usr info as a dict in format: usr:pwd
        f = open('usrs.ulokr', 'rb')
        usrinfo = pickle.load(f)
        f.close()
        newdict = {}
        for k , v in usrinfo.items():
            newdict[self.crypt.decrypt(k, 7)] = self.crypt.decrypt(v, 7)
        return newdict

    def saveUser(self, usr, pwd):
        # appends usr and pwd to USR file
        f = open('usrs.ulokr','rb')
        usrfile = pickle.load(f)
        f.close()
        usrfile[self.crypt.encrypt(usr, 7)] = self.crypt.encrypt(pwd, 7)
        f = open('usrs.ulokr','wb')
        pickle.dump(usrfile, f)
        f.close()

    def authenticate(self, usr, pwd):
        # checks if usr and pwd match USR file, returns True if correct
        for user, password in self.readUsersFile().items():
            if user == usr and password == pwd:
                return True
        return False


    # LOKR FILE METHODS
    
    def parseLokrFile(self, call):
        #reads .lokr, input: call('keys', 'labels, or 'pwds'), returns: requested info as a list
        f = open(self.lokr_file, 'rb')
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
    
    def decryptLokr(self, info):
        # decrypts .lokr file, input: info('labels' or 'pwds'), returns: requested info as a list
        keys = self.parseLokrFile('keys')
        labels =  self.parseLokrFile("labels")
        pwds = self.parseLokrFile("pwds")
        newlabels = [self.crypt.decrypt(labels[x], keys[x]) for x in range(len(keys))]
        newpwds = [self.crypt.decrypt(pwds[x], keys[x]) for x in range(len(keys))]
        if info == 'labels':
            return newlabels
        if info == 'pwds':
            return newpwds

    def createLokr(self, name):
        # creates new .lokr file for user with defaults
        f = open(self.crypt.encrypt(name, 11) + '.lokr', 'wb')
        pickle.dump({'ExampleLabel':{5:'ExamplePassword'}}, f)
        f.close()

lokr = Lokr()