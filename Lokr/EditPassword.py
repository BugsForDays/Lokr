import tkinter as tk

class EditPassword(tk.Toplevel):
    def __init__(self, manager_frame_object):
        # init edit password toplevel
        self.manager_frame = manager_frame_object
        tk.Toplevel.__init__(self, self.manager_frame)
        self.selection = self.manager_frame.password_list.curselection()[0]
        self.labels = self.manager_frame.lokr.decryptLokr('labels')
        self.pwds = self.manager_frame.lokr.decryptLokr('pwds')
        self.title("Edit Password for " + self.labels[self.selection])
        self.geometry('250x300')
        self.title_label = tk.Label(self, text='EDIT A PASSWORD:\n')
        self.edit_label_label = tk.Label(self, text='Edit label:')
        self.edit_label_field = tk.Entry(self)
        self.edit_label_field.insert(tk.INSERT, self.labels[self.selection])
        self.edit_password_label = tk.Label(self, text='Edit password:')
        self.edit_password_field = tk.Entry(self, show='*')
        self.edit_password_field.insert(tk.INSERT, self.pwds[self.selection])
        self.password_confirmation_label = tk.Label(self, text='Confirm password:')
        self.password_confirmation_field = tk.Entry(self, show='*')
        self.save_password_button = tk.Button(self, text='SAVE PASSWORD', command=self.save)
        self.cancel_button = tk.Button(self, text='Cancel', command=self.destroy)
        self.confirmation_label = tk.Label(self, text='')
        self.title_label.pack()
        self.edit_label_label.pack()
        self.edit_label_field.pack()
        self.edit_password_label.pack()
        self.edit_password_field.pack()
        self.password_confirmation_label.pack()
        self.password_confirmation_field.pack()
        self.save_password_button.pack()
        self.cancel_button.pack()
        self.confirmation_label.pack()

    def save(self):
        # saves edited password to .lokr file; edits password, saves, and recreates pwd list
        if self.edit_password_field.get() == self.password_confirmation_field.get():
            self.manager_frame.lokr.editPassword(self.selection, self.edit_label_field.get(), self.edit_password_field.get())
            self.confirmation_label.config(text='Password has been successfully saved!')
            self.close_button = tk.Button(self, text='CLOSE WINDOW', command=self.destroy)
            self.close_button.pack()
            self.manager_frame.createPasswordsList()
        else:
            self.confirmation_label.config(text='Passwords do not match. Please retry.')
       