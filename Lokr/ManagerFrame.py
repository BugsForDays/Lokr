"""
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗██╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗    ██╔════╝ ██║   ██║██║
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝    ██║  ███╗██║   ██║██║
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗    ██║   ██║██║   ██║██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝
"""

import tkinter as tk
from tkinter import messagebox
from NewPassword import NewPassword
from EditPassword import EditPassword

class ManagerFrame(tk.Frame):
    def __init__(self, lokr_object):
        # init manager frame and pack to lokr window
        self.lokr = lokr_object
        tk.Frame.__init__(self, self.lokr)
        self.leftframe = tk.Frame(self, padx = 5, pady=5)
        self.leftframe.grid(row=0, column=0)
        self.rightframe = tk.Frame(self, padx = 5, pady=5)
        self.rightframe.grid(row=0, column=1)
        self.bottomframe = tk.Frame(self, padx = 5, pady=5)
        self.bottomframe.grid(row=1, column=0)
        self.brightframe = tk.Frame(self, padx = 5, pady=5)
        self.brightframe.grid(row=1, column=1)
        self.mtitle = tk.Label(self.leftframe, text="Lokr",  font =('Lucida Console', 40))
        self.logol = tk.Label(self.leftframe, text= '\n', image=self.lokr.logo, pady = 50)
        self.mtitle.pack()
        self.logol.pack()
        self.sellbl = tk.Label(self.rightframe, text = 'Lokr File associated with account :  ' )
        self.sellbl.config(text = 'You are logged in as: ' + self.lokr.user + '\nThe Lokr File that is associated with your account is: ' +  self.lokr.lokr_file)
        self.sellbl.pack(side='top')
        self.scrollbar = tk.Scrollbar(self.bottomframe)
        self.listboxtitle = tk.Label(self.leftframe, text='Passwords:', font = ("Verdana", 12))
        self.listbox = tk.Listbox(self.bottomframe, font = ("Verdana", 12), yscrollcommand=self.scrollbar.set)
        self.createPasswordsList()
        self.e = tk.Button(self.rightframe, text = 'ENCRYPT PASSWORD', width = 30, pady = 5, command = self.encryptPasswordPrompt)
        self.d = tk.Button(self.brightframe, text = 'SHOW DECRYPTED\nPASSWORD', width = 20, pady = 5, command = self.showDecryptedPassword)
        self.cp = tk.Button(self.brightframe, text = 'COPY PASSWORD\nTO CLIPBOARD', width = 20, pady = 5, command = self.copyPasswordToClipboard)
        self.delete = tk.Button(self.rightframe, text = 'DELETE PASSWORD', width = 30, pady = 5, command = self.deletePassword)
        self.change = tk.Button(self.rightframe, text = 'EDIT PASSWORD', width = 30, pady = 5, command = self.editPasswordPrompt)
        self.e.pack()
        self.delete.pack()
        self.change.pack()
        self.d.grid(row=0,column=2)
        self.cp.grid(row=1,column=2)
        self.listbox.bind("<<ListboxSelect>>", self.getPasswordSelection)
        self.lbllbl = tk.Label(self.brightframe, text='LABEL:\n')
        self.lbllbl.grid(row = 0 , column = 0)
        self.pwdlbl = tk.Label(self.brightframe, text='PASSWORD:\n')
        self.pwdlbl.grid(row =1, column = 0)
        self.keylbl = tk.Label(self.brightframe, text='KEY:\n')
        self.keylbl.grid(row=2, column =0)
        self.pack()

    def encryptPasswordPrompt(self):
        # display new password prompt
        self.listbox.unbind("<<ListboxSelect>>")
        NewPassword(self)
        self.listbox.bind("<<ListboxSelect>>", self.getPasswordSelection)

    def editPasswordPrompt(self):
        # display edit password prompt
        self.listbox.unbind("<<ListboxSelect>>")
        EditPassword(self)
        self.listbox.bind("<<ListboxSelect>>", self.getPasswordSelection)

    def deletePassword(self):
        # deletes selected password from pwd list and recreates the list
        lbls = self.lokr.decryptLokr('labels')
        confirmbox = tk.messagebox.askyesno(title='LOKR MANAGER', message='Are you sure you want to delete the password for ' + lbls[self.listbox.curselection()[0]])
        if confirmbox is True:
            self.lokr.deletePassword(self.listbox.curselection()[0])
            self.createPasswordsList()

    def copyPasswordToClipboard(self):
        # copies decrypted pwd to clipboard
        pwds = self.lokr.decryptLokr('pwds')
        self.lokr.clipboard_clear()
        self.lokr.clipboard_append(pwds[self.listbox.curselection()[0]])

    def hideDecryptedPassword(self):
        # changes display text of password label and button
        pwds = self.lokr.parseLokrFile('pwds')
        self.pwdlbl.config(text = '')
        self.pwdlbl.config(text = 'PASSWORD:\n' + pwds[self.listbox.curselection()[0]])
        self.d.config(text = 'SHOW DECRYPTED\nPASSWORD')
        self.d.config(command = self.showDecryptedPassword)
    
    def showDecryptedPassword(self):
        # changes password label and button display text, displayed decrypted pwd
        pwds = self.lokr.decryptLokr('pwds')
        self.pwdlbl.config(text = 'PASSWORD:\n' + pwds[self.listbox.curselection()[0]])
        self.d.config(text = 'HIDE DECRYPTED\nPASSWORD')
        self.d.config(command = self.hideDecryptedPassword)

    def createPasswordsList(self):
        # creates listbox w/ decrypted pwd labels
        self.listbox.delete(0,tk.END)
        lbls = self.lokr.decryptLokr('labels')
        self.scrollbar.pack(side='right', fill ='y')
        self.listboxtitle.pack()
        self.listbox.pack()
        self.scrollbar.config(command = self.listbox.yview)
        lblsd = dict(enumerate(lbls))
        for ind, lbl in list(lblsd.items()):
            self.listbox.insert(ind, lbl)

    def getPasswordSelection(self, event):
        # runs everytime a password in password list is clicked
        lbls = self.lokr.decryptLokr('labels')
        keys = self.lokr.parseLokrFile('keys')
        pwds = self.lokr.parseLokrFile('pwds')
        self.lbllbl.config(text='LABEL:\n' + lbls[self.listbox.curselection()[0]])
        self.pwdlbl.config(text='PASSWORD:\n' + pwds[self.listbox.curselection()[0]])
        self.keylbl.config(text='KEY:\n' + str(keys[self.listbox.curselection()[0]]))