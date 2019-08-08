import random
import pickle
import tkinter as tk
from tkinter import messagebox
import os
from Crypt import Crypt

ver = 1.1


class Lokr:
    
    def __init__(self):
        self.lokr_file = ''
        self.window = tk.Tk()
        self.window.wm_iconbitmap(self.window, default ='closedlock.ico')
        self.window.title('LOKR LOGIN')
        self.window.mainloop()


    def setUserLokrFile(self, username):
        # TODO: make this more efficient
        for file in os.listdir(os.getcwd()):
            #finds all lokr files in cwd
            if file.endswith(".lokr"):
                results.append(file)
        for file in results:
            #sets f the current users' filename
            if file.startswith(crypt.encrypt(username, 11)):
                self.lokr_file = file


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
            newdict[crypt.decrypt(k, 7)] = crypt.decrypt(v, 7)
        return newdict

    def saveUser(self, usr, pwd):
        #appends usrname and pwd to USR file
        f = open('usrs.ulokr','rb')
        usrfile = pickle.load(f)
        f.close()
        usrfile[crypt.encrypt(user, 7)] = crypt.encrypt(pwd, 7)
        f = open('usrs.ulokr','wb')
        pickle.dump(usrfile, f)
        f.close()

    def savePassword(self, filename, label, pwd, key):
        #appends encrypted pass, key, lbl to SL file
        enclbl = crypt.encrypt(label, key)
        encpwd = crypt.encrypt(pwd, key)
        f = open(filename + '.lokr', 'rb')
        f.seek(0)
        whatsinside = pickle.load(f)
        f.close()
        whatsinside[enclbl] = {str(key) : encpwd}
        f = open(filename + '.lokr', 'wb')
        pickle.dump(whatsinside, f)
        f.close()

    def deletePassword(index):
        lbls = parseLokrFile(f, 'labels')
        fl = open(f, 'rb')
        fl.seek(0)
        info = pickle.load(fl)
        fl.close()
        del info[lbls[index]]
        fl = open(f, 'wb')
        pickle.dump(info,fl)
        fl.close()

    def decryptLokr(self, filename, info):
        #decrypts SL file, input: file, info('labels' or 'pwds'), returns: info as a list
        keys = parseLokrFile(filename, 'keys')
        labels =  parseLokrFile(filename,"labels")
        pwds = parseLokrFile(filename,"pwds")
        newlabels = [crypt.decrypt(labels[x], keys[x]) for x in range(len(keys))]
        newpwds = [crypt.decrypt(pwds[x], keys[x]) for x in range(len(keys))]
        if info == 'labels':
            return newlabels
        if info == 'pwds':
            return newpwds

    def authenticate(self, usr, pwd):
        #checks if usrname and pwd match, returns True if correct
        for user, password in self.readUsersFile():
            if user == usr and password == pwd:
                return True

    def createLokr(self, name):
        #creates new SL locker file with defaults
        f = open(crypt.encrypt(name, 11) + '.lokr', 'wb')
        pickle.dump({'ExampleLabel':{5:'ExamplePassword'}}, f)
        f.close()
        
    #manager


lokr = Lokr()