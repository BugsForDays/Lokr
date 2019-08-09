import tkinter as tk

class EditPassword(tk.Toplevel):
    def __init__(self, manager_frame_object):
        # init edit password toplevel
        self.manager_frame = manager_frame_object
        tk.Toplevel.__init__(self, self.manager_frame)
        self.selection = self.manager_frame.listbox.curselection()[0]
        self.lbls = self.manager_frame.lokr.decryptLokr('labels')
        self.pwds = self.manager_frame.lokr.decryptLokr('pwds')
        self.title("Edit Password for " + self.lbls[self.manager_frame.listbox.curselection()[0]])
        self.geometry('250x300')
        self.l = tk.Label(self, text = 'EDIT A PASSWORD:\n')
        self.newll = tk.Label(self, text = 'Edit label:')
        self.newl = tk.Entry(self)
        self.newl.insert(tk.INSERT, self.lbls[self.manager_frame.listbox.curselection()[0]])
        self.newpl = tk.Label(self, text='Edit password:')
        self.newp = tk.Entry(self, show='*')
        self.newp.insert(tk.INSERT, self.pwds[self.manager_frame.listbox.curselection()[0]])
        self.newpcl = tk.Label(self, text='Confirm password:')
        self.newpc = tk.Entry(self, show='*')
        self.eb = tk.Button(self, text='SAVE PASSWORD', command = self.save)
        self.cancel = tk.Button(self, text='Cancel', command=self.destroy)
        self.conf = tk.Label(self, text = '')
        self.l.pack()
        self.newll.pack()
        self.newl.pack()
        self.newpl.pack()
        self.newp.pack()
        self.newpcl.pack()
        self.newpc.pack()
        self.eb.pack()
        self.cancel.pack()
        self.conf.pack()

    def save(self):
        # saves edited password to .lokr file; edits password, saves, and recreates pwd list
        if self.newp.get() == self.newpc.get():
            self.manager_frame.lokr.editPassword(self.selection, self.newl.get(), self.newp.get())
            self.conf.config(text='Password has been successfully saved!')
            self.cb = tk.Button(self, text='CLOSE WINDOW', command = self.destroy)
            self.cb.pack()
            self.manager_frame.createPasswordsList()
        else:
            self.conf.config(text='Passwords do not match. Please retry.')

        