import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, lokr_object):
        self.lokr = lokr_object
        self.ex = tk.Button(self, text = 'Exit', command=quit)
        self.logo = tk.PhotoImage(file='lock.png')
        self.logolbl = tk.Label(self, text= '\n', image=logo, pady = 50)
        self.title = tk.Label(self, text="Lokr",  font =('Lucida Console', 40))
        self.logtitle = tk.Label(self, text="\nVersion: " + str(ver) + "\n\nPlease Login:")
        self.usr = tk.Entry(self)
        self.pas = tk.Entry(self, show='*')
        self.usrl = tk.Label(self, text='Username:')
        self.pasl = tk.Label(self, text='Password:')
        self.login = tk.Button(self, text='Launch', command=checkusr)
        self.newusr = tk.Button(self, text = 'Register', command=self.newUserPrompt)
        self.clear = tk.Button(self, text = 'Clear', command=self.clearFields)
        self.confirm = tk.Label(self)
        # TODO: split this into another method
        self.logolbl.pack()
        self.title.pack()
        self.logtitle.pack()
        self.usrl.pack()
        self.usr.pack()
        self.pasl.pack()
        self.pas.pack()
        self.login.pack()
        self.newusr.pack()
        self.clear.pack()
        self.confirm.pack()
        self.bind("<Return>", checkusr) 
        
    def clearFields(self):
        self.usr.delete(0, tk.END)
        self.pas.delete(0, tk.END)
        self.confirm.config(text=' ' )

    def newUserPrompt(self):
        #shows prompts to create new user and create new SL locker
        newusrl = tk.Label(window, text='Create a username:')
        newusrl.pack()
        newusr = tk.Entry(window)
        newusr.pack()
        newpasl = tk.Label(window, text='Create a password:')
        newpasl.pack()
        newpas = tk.Entry(window, show='*')
        newpas.pack()
        newconl = tk.Label(window, text='Confirm password:')
        newconl.pack()
        newcon = tk.Entry(window, show='*')
        newcon.pack()
        window.unbind("<Return>")
        register = tk.Button(window, text="Register!", command=self.register)
        register.pack(expand = True)
    
    def register(self):
        #makes sure no two usr names are same, creates locker and displays success lbl
        if (newusr.get() in users) == False and newpas.get() == newcon.get():
            lokr.saveUser(newusr.get(), newpas.get())
            lokr.createLokr(newusr.get())
            confirm.config(text='You have successfully registered!\n A new Lokr has been created for you.')
            newusrl.pack_forget()
            newusr.pack_forget()
            newpasl.pack_forget()
            newpas.pack_forget()
            newconl.pack_forget()
            newcon.pack_forget()
            register.pack_forget()
            window.bind("<Return>")
        else:
            confirm.config(text='Username already exists or passwords do not match. Please retry.')
            window.bind("<Return>", checkusr)