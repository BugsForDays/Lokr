"""
██╗      ██████╗  ██████╗ ██╗███╗   ██╗     ██████╗ ██╗   ██╗██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔════╝ ██║   ██║██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██║  ███╗██║   ██║██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██║   ██║██║   ██║██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ╚██████╔╝╚██████╔╝██║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝     ╚═════╝  ╚═════╝ ╚═╝
"""

import tkinter as tk
from ManagerFrame import ManagerFrame

class LoginFrame(tk.Frame):

    def __init__(self, lokr_object):
        # init the login frame and pack it to the lokr obj
        self.lokr = lokr_object
        tk.Frame.__init__(self, self.lokr)
        self.logo_label = tk.Label(self, text='\n', image=self.lokr.logo, pady=50)
        self.title = tk.Label(self, text="Lokr", font=('Lucida Console', 40))
        self.login_title = tk.Label(self, text="\nVersion: " + str(self.lokr.ver) + "\n\nPlease Login:")
        self.username_field = tk.Entry(self)
        self.password_field = tk.Entry(self, show='*')
        self.username_label = tk.Label(self, text='Username:')
        self.password_label = tk.Label(self, text='Password:')
        self.launch_button = tk.Button(self, text='Launch', command=self.checkUser)
        self.new_user_button = tk.Button(self, text='Register', command=self.newUserPrompt)
        self.clear_button = tk.Button(self, text='Clear', command=self.clearFields)
        self.confirmation_label = tk.Label(self)
        self.logo_label.pack()
        self.title.pack()
        self.login_title.pack()
        self.username_label.pack()
        self.username_field.pack()
        self.password_label.pack()
        self.password_field.pack()
        self.launch_button.pack()
        self.new_user_button.pack()
        self.clear_button.pack()
        self.confirmation_label.pack()
        self.lokr.bind("<Return>", self.checkUser)
        self.pack()

    def checkUser(self, event=None):
        # check if the user/pwd input matches. if match: forget login window and display the manager frame; else: display error
        if (self.username_field.get() in self.lokr.readUsersFile()) is True and self.lokr.authenticate(self.username_field.get(), self.password_field.get()) is True:
            self.confirmation_label.config(text='You have successfully logged on!')
            self.lokr.setUserLokrFile(self.username_field.get())
            self.username_field.delete(0, tk.END)
            self.password_field.delete(0, tk.END)
            self.unbind("<Return>")
            self.lokr.title('LOKR MANAGER')
            self.pack_forget()
            ManagerFrame(self.lokr)
        else:
            self.confirmation_label.config(text='Your username and/or password is incorrect.')
            self.username_field.delete(0, tk.END)
            self.password_field.delete(0, tk.END)

    def clearFields(self):
        # clear user/pwd fields
        self.username_field.delete(0, tk.END)
        self.password_field.delete(0, tk.END)
        self.confirmation_label.config(text=' ')

    def newUserPrompt(self):
        # shows registration prompt
        self.new_username_label = tk.Label(self, text='Create a username:')
        self.new_username_label.pack()
        self.new_username_field = tk.Entry(self)
        self.new_username_field.pack()
        self.new_password_label = tk.Label(self, text='Create a password:')
        self.new_password_label.pack()
        self.new_password_field = tk.Entry(self, show='*')
        self.new_password_field.pack()
        self.password_confirmation_label = tk.Label(self, text='Confirm password:')
        self.password_confirmation_label.pack()
        self.password_confirmation_field = tk.Entry(self, show='*')
        self.password_confirmation_field.pack()
        self.lokr.bind("<Return>", self.register)
        self.register_button = tk.Button(self, text="Register!", command=self.register)
        self.register_button.pack(expand=True)

    def register(self, event=None):
        # makes sure no two usr names are same, creates .lokr and displays success
        if (self.new_username_field.get() in self.lokr.readUsersFile()) is False and self.new_password_field.get() is self.password_confirmation_field.get():
            self.lokr.saveUser(self.new_username_field.get(), self.new_password_field.get())
            self.lokr.createLokr(self.new_username_field.get())
            self.confirmation_label.config(text='You have successfully registered!\n A new Lokr has been created for you.')
            self.new_username_label.pack_forget()
            self.new_username_field.pack_forget()
            self.new_password_label.pack_forget()
            self.new_password_field.pack_forget()
            self.password_confirmation_label.pack_forget()
            self.password_confirmation_field.pack_forget()
            self.register_button.pack_forget()
            self.lokr.bind("<Return>", self.checkUser)
        else:
            self.confirmation_label.config(text='Username already exists or passwords do not match. Please retry.')
