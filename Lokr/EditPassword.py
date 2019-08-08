import tkinter as tk
import pickle

class EditPassword(tk.Toplevel):
    def __init__(self, manager_frame_object):
        self.manager_frame = manager_frame_object
        tk.Toplevel.__init__(self, self.manager_frame)
        self.selection = self.manager_frame.listbox.curselection()[0]
        self.lbls = self.manager_frame.lokr.decryptLokr(self.manager_frame.lokr.lokr_file, 'labels')
        self.pwds = self.manager_frame.lokr.decryptLokr(self.manager_frame.lokr.lokr_file, 'pwds')
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
        self.cancel = tk.Button(self, text='Cancel', command=self.closeEditPrompt)
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
        
    def closeEditPrompt(self):
        #closes Toplevel
        self.destroy()

    def save(self):
        #saves password to .lokr file
        if self.newp.get() == self.newpc.get():
            lbls = self.manager_frame.lokr.parseLokrFile(self.manager_frame.lokr.lokr_file, 'labels')
            keys = self.manager_frame.lokr.parseLokrFile(self.manager_frame.lokr.lokr_file, "keys")
            # TODO: the following line can be a method with deletePassword(its repeating)
            fl = open(self.manager_frame.lokr.lokr_file, 'rb')
            fl.seek(0)
            info = pickle.load(fl)
            fl.close()
            del info[lbls[self.selection]]
            fl = open(self.manager_frame.lokr.lokr_file, 'wb')
            pickle.dump(info,fl)
            fl.close()
            self.manager_frame.lokr.savePassword(self.manager_frame.lokr.lokr_file, self.newl.get(), self.newp.get(), int(keys[self.selection]))
            self.conf.config(text='Password has been successfully saved!')
            self.cb = tk.Button(self, text='CLOSE WINDOW', command = self.closeEditPrompt)
            self.cb.pack()
            self.manager_frame.createPasswordsList()
        else:
            self.conf.config(text='Passwords do not match. Please retry.')

        