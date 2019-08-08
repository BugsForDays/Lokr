import tkinter as tk
import random


class NewPassword(tk.Toplevel):
    #creates new window w/ encrypt pwd prompts, stores pwd, lbl, and key to lokr file
    def __init__(self, manager_frame_object):
        self.manager_frame = manager_frame_object
        tk.Toplevel.__init__(self, self.manager_frame)
        self.cv = tk.IntVar()
        # self.self = tk.Toplevel()
        self.geometry('250x300')
        self.l = tk.Label(self, text = 'ENCRYPT A NEW PASSWORD:\n')
        self.newll = tk.Label(self, text = 'Enter password identifier/label:')
        self.newl = tk.Entry(self)
        self.kl = tk.Label(self, text = 'Enter an encryption key(1 - 26):')
        self.k = tk.Entry(self)
        self.kc = tk.Checkbutton(self, text="Auto select a random key", variable = self.cv, command=self.checkRandomKey)
        self.newpl = tk.Label(self, text='Enter password:')
        self.newp = tk.Entry(self, show='*')
        self.newpcl = tk.Label(self, text='Confirm password:')
        self.newpc = tk.Entry(self, show='*',)
        self.eb = tk.Button(self, text='ENCRYPT PASSWORD', command = self.storePassword)
        self.conf = tk.Label(self, text = '')
        self.l.pack()
        self.newll.pack()
        self.newl.pack()
        self.kl.pack()
        self.k.pack()
        self.kc.pack()
        self.newpl.pack()
        self.newp.pack()
        self.newpcl.pack()
        self.newpc.pack()
        self.eb.pack()
        self.conf.pack()

    def checkRandomKey(self):
        #checks the checkbutton, whether 1 or 0 and blanks out key field or unblanks
        if self.cv.get() == 1:
            self.k.delete(0, tk.END)
            self.k.configure(state=tk.DISABLED)
        else:
            self.k.configure(state=tk.NORMAL)

    def storePassword(self):
        #makes sure pwds match and stores pwds
        if self.newp.get() == self.newpc.get():
            if self.cv.get() == 1:
                pk = random.randint(1, 26)
            else:
                pk = int(self.k.get())
            self.manager_frame.lokr.savePassword(self.manager_frame.lokr.lokr_file, self.newl.get(), self.newp.get(), pk)
            self.conf.config(text='Password has been successfully encrypted!')
            self.manager_frame.createPasswordsList()
            self.c = tk.Button(self, text='CLOSE WINDOW', command = self.destroy)
            self.c.pack()
        else:
            self.conf.config(text='Passwords do not match. Please retry.')

    