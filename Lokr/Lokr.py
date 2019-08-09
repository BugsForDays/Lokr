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
import sys
from Crypt import Crypt
from LoginFrame import LoginFrame

class Lokr(tk.Tk):
    ver = 1.1

    def __init__(self):
        # init main window
        tk.Tk.__init__(self)
        self.lokr_file = ''
        self.user_file = '.lokrdata/usrs.ulokr'
        self.user = ''
        self.wm_iconbitmap(self, default=self.resource_path('assets\\closedlock.ico'))
        self.logo = tk.PhotoImage(file=self.resource_path('assets\\lock.png'))
        self.title('LOKR LOGIN')
        self.minsize(350, 200)
        plain_text_file = open('.lokrdata/cset.dlokr', 'rb')
        cipher_text_file = open('.lokrdata/cpcset.dlokr', 'rb')
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
        encrypted_label = self.crypt.encrypt(label, key)
        encrypted_password = self.crypt.encrypt(pwd, key)
        file = open(self.lokr_file, 'rb')
        file.seek(0)
        whatsinside = pickle.load(file)
        file.close()
        whatsinside[encrypted_label] = {str(key): encrypted_password}
        file = open(self.lokr_file, 'wb')
        pickle.dump(whatsinside, file)
        file.close()

    def editPassword(self, index, label, pwd):
        # edits password: delete and resaves with new info
        keys = self.parseLokrFile("keys")
        self.deletePassword(index)
        self.savePassword(label, pwd, int(keys[index]))

    def deletePassword(self, index):
        # delete password from user's .lokr
        labels = self.parseLokrFile('labels')
        file = open(self.lokr_file, 'rb')
        file.seek(0)
        contents = pickle.load(file)
        file.close()
        del contents[labels[index]]
        file = open(self.lokr_file, 'wb')
        pickle.dump(contents, file)
        file.close()


    # USER MANAGEMENT METHODS

    def setUserLokrFile(self, username):
        # set user's lokr file
        self.user = username
        for file in os.listdir(os.getcwd() + '\\.lokrdata'):
            if file == (self.crypt.encrypt(username, 11) + '.lokr'):
                self.lokr_file = ".lokrdata/" + file

    def readUsersFile(self):
        # reads USR file, returns: decrypted usr info as a dict in format: usr:pwd
        file = open(self.user_file, 'rb')
        user_data = pickle.load(file)
        file.close()
        decrypted_user_data = {}
        for user, pwd in user_data.items():
            decrypted_user_data[self.crypt.decrypt(user, 7)] = self.crypt.decrypt(pwd, 7)
        return decrypted_user_data

    def saveUser(self, usr, pwd):
        # appends usr and pwd to USR file
        file = open(self.user_file, 'rb')
        user_data = pickle.load(file)
        file.close()
        user_data[self.crypt.encrypt(usr, 7)] = self.crypt.encrypt(pwd, 7)
        file = open(self.user_file, 'wb')
        pickle.dump(user_data, file)
        file.close()

    def authenticate(self, usr, pwd):
        # checks if usr and pwd match USR file, returns True if correct
        for user, password in self.readUsersFile().items():
            if user == usr and password == pwd:
                return True
        return False


    # LOKR FILE METHODS

    def parseLokrFile(self, call):
        #reads .lokr, input: call('keys', 'labels, or 'pwds'), returns: requested info as a list
        file = open(self.lokr_file, 'rb')
        file.seek(0)
        lokr_data = pickle.load(file)
        labels = list(lokr_data.keys())
        keys = []
        pwds = []
        file.close()
        for k, i in enumerate(list(lokr_data.keys())):
            keys.append((list(list(lokr_data.values())[k].keys())[0]))
        for k, i in enumerate(list(lokr_data.keys())):
            pwds.append((list(list(lokr_data.values())[k].values())[0]))
        if call == 'keys':
            return keys
        if call == 'labels':
            return labels
        if call == 'pwds':
            return pwds

    def decryptLokr(self, info):
        # decrypts .lokr file, input: info('labels' or 'pwds'), returns: requested info as a list
        keys = self.parseLokrFile('keys')
        labels = self.parseLokrFile("labels")
        pwds = self.parseLokrFile("pwds")
        newlabels = [self.crypt.decrypt(labels[x], keys[x]) for x in range(len(keys))]
        newpwds = [self.crypt.decrypt(pwds[x], keys[x]) for x in range(len(keys))]
        if info == 'labels':
            return newlabels
        if info == 'pwds':
            return newpwds

    def createLokr(self, name):
        # creates new .lokr file for user with defaults
        file = open('.lokrdata/' + self.crypt.encrypt(name, 11) + '.lokr', 'wb')
        pickle.dump({'ExampleLabel':{5:'ExamplePassword'}}, file)
        file.close()

    # HELPER METHODS

    def resource_path(self, relative_path):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

lokr = Lokr()
