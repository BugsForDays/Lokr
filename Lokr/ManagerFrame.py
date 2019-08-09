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
        self.left_frame = tk.Frame(self, padx=5, pady=5)
        self.left_frame.grid(row=0, column=0)
        self.right_frame = tk.Frame(self, padx=5, pady=5)
        self.right_frame.grid(row=0, column=1)
        self.bottom_frame = tk.Frame(self, padx=5, pady=5)
        self.bottom_frame.grid(row=1, column=0)
        self.bottom_right_frame = tk.Frame(self, padx=5, pady=5)
        self.bottom_right_frame.grid(row=1, column=1)
        self.title = tk.Label(self.left_frame, text="Lokr", font=('Lucida Console', 40))
        self.logo_label = tk.Label(self.left_frame, text='\n', image=self.lokr.logo, pady=50)
        self.title.pack()
        self.logo_label.pack()
        self.info_label = tk.Label(self.right_frame, text='Lokr File associated with account :  ')
        self.info_label.config(text='You are logged in as: ' + self.lokr.user + '\nThe Lokr File that is associated with your account is: ' +  self.lokr.lokr_file)
        self.info_label.pack(side='top')
        self.scrollbar = tk.Scrollbar(self.bottom_frame)
        self.password_list_title = tk.Label(self.left_frame, text='Passwords:', font=("Verdana", 12))
        self.password_list = tk.Listbox(self.bottom_frame, font=("Verdana", 12), yscrollcommand=self.scrollbar.set)
        self.createPasswordsList()
        self.encrypt_password_button = tk.Button(self.right_frame, text='ENCRYPT PASSWORD', width=30, pady=5, command=self.encryptPasswordPrompt)
        self.decrypt_password_button = tk.Button(self.bottom_right_frame, text='SHOW DECRYPTED\nPASSWORD', width=20, pady=5, command=self.showDecryptedPassword)
        self.copy_password_button = tk.Button(self.bottom_right_frame, text='COPY PASSWORD\nTO CLIPBOARD', width=20, pady=5, command=self.copyPasswordToClipboard)
        self.delete_password_button = tk.Button(self.right_frame, text='DELETE PASSWORD', width=30, pady=5, command=self.deletePassword)
        self.edit_password_button = tk.Button(self.right_frame, text='EDIT PASSWORD', width=30, pady=5, command=self.editPasswordPrompt)
        self.encrypt_password_button.pack()
        self.delete_password_button.pack()
        self.edit_password_button.pack()
        self.decrypt_password_button.grid(row=0, column=2)
        self.copy_password_button.grid(row=1, column=2)
        self.password_list.bind("<<ListboxSelect>>", self.getPasswordSelection)
        self.label_label = tk.Label(self.bottom_right_frame, text='LABEL:\n')
        self.label_label.grid(row=0, column=0)
        self.password_label = tk.Label(self.bottom_right_frame, text='PASSWORD:\n')
        self.password_label.grid(row=1, column=0)
        self.key_label = tk.Label(self.bottom_right_frame, text='KEY:\n')
        self.key_label.grid(row=2, column=0)
        self.password_list.select_set(0)
        self.getPasswordSelection()
        self.pack()

    def encryptPasswordPrompt(self):
        # display new password prompt
        self.password_list.unbind("<<ListboxSelect>>")
        NewPassword(self)
        self.password_list.bind("<<ListboxSelect>>", self.getPasswordSelection)

    def editPasswordPrompt(self):
        # display edit password prompt
        self.password_list.unbind("<<ListboxSelect>>")
        EditPassword(self)
        self.password_list.bind("<<ListboxSelect>>", self.getPasswordSelection)

    def deletePassword(self):
        # deletes selected password from pwd list and recreates the list
        labels = self.lokr.decryptLokr('labels')
        confirmation_box = tk.messagebox.askyesno(title='LOKR MANAGER', message='Are you sure you want to delete the password for ' + labels[self.password_list.curselection()[0]])
        if confirmation_box is True:
            self.lokr.deletePassword(self.password_list.curselection()[0])
            self.createPasswordsList()

    def copyPasswordToClipboard(self):
        # copies decrypted pwd to clipboard
        pwds = self.lokr.decryptLokr('pwds')
        self.lokr.clipboard_clear()
        self.lokr.clipboard_append(pwds[self.password_list.curselection()[0]])

    def hideDecryptedPassword(self):
        # changes display text of password label and button
        pwds = self.lokr.parseLokrFile('pwds')
        self.password_label.config(text='')
        self.password_label.config(text='PASSWORD:\n' + pwds[self.password_list.curselection()[0]])
        self.decrypt_password_button.config(text='SHOW DECRYPTED\nPASSWORD')
        self.decrypt_password_button.config(command=self.showDecryptedPassword)

    def showDecryptedPassword(self):
        # changes password label and button display text, displayed decrypted pwd
        pwds = self.lokr.decryptLokr('pwds')
        self.password_label.config(text='PASSWORD:\n' + pwds[self.password_list.curselection()[0]])
        self.decrypt_password_button.config(text='HIDE DECRYPTED\nPASSWORD')
        self.decrypt_password_button.config(command=self.hideDecryptedPassword)

    def createPasswordsList(self):
        # creates listbox w/ decrypted pwd labels
        self.password_list.delete(0, tk.END)
        labels = self.lokr.decryptLokr('labels')
        self.scrollbar.pack(side='right', fill='y')
        self.password_list_title.pack()
        self.password_list.pack()
        self.scrollbar.config(command=self.password_list.yview)
        enumerated_labels = dict(enumerate(labels))
        for index, lbl in list(enumerated_labels.items()):
            self.password_list.insert(index, lbl)

    def getPasswordSelection(self, event=None):
        # runs everytime a password in password list is clicked
        labels = self.lokr.decryptLokr('labels')
        keys = self.lokr.parseLokrFile('keys')
        pwds = self.lokr.parseLokrFile('pwds')
        selection = self.password_list.curselection()[0]
        self.label_label.config(text='LABEL:\n' + labels[selection])
        self.password_label.config(text='PASSWORD:\n' + pwds[selection])
        self.key_label.config(text='KEY:\n' + str(keys[selection]))
        