import tkinter as tk
import random


class NewPassword(tk.Toplevel):
    #creates new window w/ encrypt pwd prompts, stores pwd, lbl, and key to lokr file
    def __init__(self, manager_frame_object):
        # init new password toplevel
        self.manager_frame = manager_frame_object
        tk.Toplevel.__init__(self, self.manager_frame)
        self.random_key = tk.IntVar()
        self.geometry('250x300')
        self.title_label = tk.Label(self, text='ENCRYPT A NEW PASSWORD:\n')
        self.new_label_label = tk.Label(self, text='Enter password identifier/label:')
        self.new_label_field = tk.Entry(self)
        self.new_key_label = tk.Label(self, text='Enter an encryption key(1 - 26):')
        self.new_key_field = tk.Entry(self)
        self.random_key_checkbutton = tk.Checkbutton(self, text="Auto select a random key", variable=self.random_key, command=self.checkRandomKey)
        self.new_password_label = tk.Label(self, text='Enter password:')
        self.new_password_field = tk.Entry(self, show='*')
        self.password_confirmation_label = tk.Label(self, text='Confirm password:')
        self.password_confirmation_field = tk.Entry(self, show='*')
        self.encrypt_password_button = tk.Button(self, text='ENCRYPT PASSWORD', command=self.storePassword)
        self.confirmation_label = tk.Label(self, text='')
        self.title_label.pack()
        self.new_label_label.pack()
        self.new_label_field.pack()
        self.new_key_label.pack()
        self.new_key_field.pack()
        self.random_key_checkbutton.pack()
        self.new_password_label.pack()
        self.new_password_field.pack()
        self.password_confirmation_label.pack()
        self.password_confirmation_field.pack()
        self.encrypt_password_button.pack()
        self.confirmation_label.pack()

    def checkRandomKey(self):
        # checks the random key checkbutton, whether 1 or 0 and blanks out key field or unblanks
        if self.random_key.get() == 1:
            self.new_key_field.delete(0, tk.END)
            self.new_key_field.configure(state=tk.DISABLED)
        else:
            self.new_key_field.configure(state=tk.NORMAL)

    def storePassword(self):
        # makes sure new pwds match and updates pwds
        if self.new_password_field.get() == self.password_confirmation_field.get():
            if self.random_key.get() == 1:
                key = random.randint(1, 26)
            else:
                key = int(self.new_key_field.get())
            self.manager_frame.lokr.savePassword(self.new_label_field.get(), self.new_password_field.get(), key)
            self.confirmation_label.config(text='Password has been successfully encrypted!')
            self.manager_frame.createPasswordsList()
            self.close_button = tk.Button(self, text='CLOSE WINDOW', command=self.destroy)
            self.close_button.pack()
        else:
            self.confirmation_label.config(text='Passwords do not match. Please retry.')
    