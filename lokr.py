"""
██╗      ██████╗ ██╗  ██╗██████╗
██║     ██╔═══██╗██║ ██╔╝██╔══██╗
██║     ██║   ██║█████╔╝ ██████╔╝
██║     ██║   ██║██╔═██╗ ██╔══██╗
███████╗╚██████╔╝██║  ██╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

****************************************************************************
|                   LOKR PASSWORD ENCRYTION MANAGER                        |
|   Created by petabite aka Philip Z(https://github.com/petabite)          |                                                            |
#***************************************************************************
"""
import random
import pickle
import tkinter as tk
from tkinter import messagebox
import os

import Crypt

ver = 1.0

# csetfile = open('cset.dlokr', 'rb')
# cpcsetfile = open('cpcset.dlokr', 'rb')
# charset = pickle.load(csetfile)
# cpCharset = pickle.load(cpcsetfile)
# csetfile.close()
# cpcsetfile.close()

crypt = Crypt.Crypt(cpCharset, charset)

# newCharset = ''
#
# #ENCRYPTION/DECRYPTION METHODS
# def cpreorderencrypt(cp, key):
#     #reorder cp based on key, returns: cp as new cp list
#     return cp[key:] + cp[0:key]
#
# # def findindex(the_list, substring):
# #     #finds index of string in list, returns: index of string as int
# #     for i, s in enumerate(the_list):
# #         if substring in s:
# #             return i
# #     return -1
#
# def encrypt(text, key):
#     #encrypt text with key via string construction, returns: encrypted text as string
#     encrypted = ''
#     global newCharset
#     newCharset = list(cpreorderencrypt(charset, key))
#     for i in range(len(text)):
#         if text[i] in newCharset:
#             encrypted += cpCharset[newCharset.index(text[i])]
#     return encrypted
#
# def decrypt(text, key):
#     #inverse of encrypt(): decrypts text based on key, returns: decrypted text as string
#     newCharset = ''
#     newCharset = list(cpreorderencrypt(charset, int(key)))
#     decrypted = ''
#     for i in range(len(text)):
#         if text[i] in cpCharset:
#             decrypted += newCharset[cpCharset.index(text[i])]
#     text = ''
#     key = 0
#     return decrypted

# STORAGE + MAGAGEMENT METHODS
# def appendtousrfile(filename, contents):
#     #appends contents to USR file
#     f = open(filename + '.ulokr', 'a')
#     f.write(contents + '\n')
#     f.close()

# def striplist(list):
#     #strips each element in list, returns: stripped newlist as a list
#     newlist = []
#     for i in list:
#         ele = ''
#         ele = i.rstrip()
#         newlist.append(ele)
#     return newlist

# def parseLokrFile(filename, call):
#     #reads .lokr, input: file, call('keys', 'labels, or 'pwds'), returns: info in file as a list
#     if filename.endswith('.lokr'):
#         pcfn = filename
#     else:
#         pcfn = filename + '.lokr'
#     f = open(pcfn, 'rb')
#     f.seek(0)
#     info = pickle.load(f)
#     labels = list(info.keys())
#     keys = []
#     pwds = []
#     for k, i in enumerate(list(info.keys())):
#         keys.append((list(list(info.values())[k].keys())[0]))
#     for k, i in enumerate(list(info.keys())):
#         pwds.append((list(list(info.values())[k].values())[0]))
#     if call == 'keys':
#         return keys
#     if call == 'labels':
#         return labels
#     if call == 'pwds':
#         return pwds
#     f.close()

# def saveUser(usr, pwd):
#     #appends usrname and pwd to USR file
#     f = open('usrs.ulokr','rb')
#     usrfile = pickle.load(f)
#     f.close()
#     usrfile[usr] = pwd
#     f = open('usrs.ulokr','wb')
#     pickle.dump(usrfile, f)
#     f.close()

# def readUsersFile():
#     #reads USR file, returns: usr info as a dict in format: usr:pwd
#     f = open('usrs.ulokr', 'rb')
#     usrinfo = pickle.load(f)
#     f.close()
#     newdict = {}
#     for k , v in usrinfo.items():
#         newdict[crypt.decrypt(k, 7)] = crypt.decrypt(v, 7)
#     return newdict

# def savePassword(filename, label, pwd, key):
#     #appends encrypted pass, key, lbl to SL file
#     enclbl = crypt.encrypt(label, key)
#     encpwd = crypt.encrypt(pwd, key)
#     f = open(filename + '.lokr', 'rb')
#     f.seek(0)
#     whatsinside = pickle.load(f)
#     f.close()
#     whatsinside[enclbl] = {str(key) : encpwd}
#     f = open(filename + '.lokr', 'wb')
#     pickle.dump(whatsinside, f)
#     f.close()

# def decryptLokr(filename, info):
#     #decrypts SL file, input: file, info('labels' or 'pwds'), returns: info as a list
#     keys = parseLokrFile(filename, 'keys')
#     labels =  parseLokrFile(filename,"labels")
#     pwds = parseLokrFile(filename,"pwds")
#     newlabels = [crypt.decrypt(labels[x], keys[x]) for x in range(len(keys))]
#     newpwds = [crypt.decrypt(pwds[x], keys[x]) for x in range(len(keys))]
#     if info == 'labels':
#         return newlabels
#     if info == 'pwds':
#         return newpwds

"""
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗██╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗    ██╔════╝ ██║   ██║██║
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝    ██║  ███╗██║   ██║██║
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗    ██║   ██║██║   ██║██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝
"""

window = tk.Tk()
users = readUsersFile()

#WINDOW SETTINGS
window.minsize(350,200)

#FUNCTIONS
# def authenticate(usr, pwd):
#     #checks if usrname and pwd match, returns True if correct
#     for user, password in readUsersFile():
#         if user == usr and password == pwd:
#             return True

# def filestrip(text):
#     #returns text w/o last chars
#     return text[:-6]

# def createLokr(name):
#     #creates new SL locker file with defaults
#     f = open(name + '.lokr', 'wb')
#     pickle.dump({'ExampleLabel':{5:'ExamplePassword'}}, f)
#     f.close()

def checkusr(event=None):
    #runs authenticate() and loads next screen with pwds
    # users = readUsersFile()
    # if (usr.get() in users) == True and authenticate(usr.get(), pas.get()) == True:
    #     usrname = str(usr.get())
    #     confirm.config(text='You have successfully logged on!' )
    #     usr.delete(0, tk.END)
    #     pas.delete(0, tk.END)
    #     logolbl.pack_forget()
    #     title.pack_forget()
    #     logtitle.pack_forget()
    #     usrl.pack_forget()
    #     usr.pack_forget()
    #     pasl.pack_forget()
    #     pas.pack_forget()
    #     login.pack_forget()
    #     newusr.pack_forget()
    #     clear.pack_forget()
    #     confirm.pack_forget()
    #     window.unbind("<Return>")
    #     window.title('LOKR MANAGER')

        #LAUCH LOKR MANAGER
        # leftframe = tk.Frame(window, padx = 5, pady=5)
        # leftframe.grid(row=0, column=0)
        # rightframe = tk.Frame(window, padx = 5, pady=5)
        # rightframe.grid(row=0, column=1)
        # bottomframe = tk.Frame(window, padx = 5, pady=5)
        # bottomframe.grid(row=1, column=0)
        # brightframe = tk.Frame(window, padx = 5, pady=5)
        # brightframe.grid(row=1, column=1)
        # mtitle = tk.Label(leftframe, text="Lokr",  font =('Lucida Console', 40))
        # logol = tk.Label(leftframe, text= '\n', image=logo, pady = 50)
        # mtitle.pack()
        # logol.pack()
        # results = []

        #GUI METHODS: CALLED WHEN BUTTONS ARE CLICKED
        # def copyPasswordToClipboard():
        #     #copies decrypted pwd to clipboard
        #     pwds = decryptLokr(f, 'pwds')
        #     window.clipboard_clear()
        #     window.clipboard_append(pwds[listbox.curselection()[0]])

        # def hideDecryptedPassword():
        #     #changes display text of password label and button
        #     pwds = parseLokrFile(f, 'pwds')
        #     pwdlbl.config(text = '')
        #     pwdlbl.config(text = 'PASSWORD:\n' + pwds[listbox.curselection()[0]])
        #     d.config(text = 'SHOW DECRYPTED\nPASSWORD')
        #     d.config(command = showDecryptedPassword)

        # def hideDecryptedPassword():
        #     #runs hideDecryptedPassword and changes password button display text
        #     hideDecryptedPassword()
        #     d.config(text = 'SHOW DECRYPTED\nPASSWORD')

        # def showDecryptedPassword():
        #     #changes password label and button display text, displayed decrypted pwd
        #     pwds = decryptLokr(f, 'pwds')
        #     pwdlbl.config(text = 'PASSWORD:\n' + pwds[listbox.curselection()[0]])
        #     d.config(text = 'HIDE DECRYPTED\nPASSWORD')
        #     d.config(command = hideDecryptedPassword)

        # def deletePassword():
        #     #deletes selected password from listbox and recreates the listbox
        #     lbls = decryptLokr(f, 'labels')
        #     confirmbox = messagebox.askyesno(title='LOKR MANAGER', message='Are you sure you want to delete the password for ' + lbls[listbox.curselection()[0]])
        #     if confirmbox == True:
        #         lbls = parseLokrFile(f, 'labels')
        #         fl = open(f, 'rb')
        #         fl.seek(0)
        #         info = pickle.load(fl)
        #         fl.close()
        #         del info[lbls[listbox.curselection()[0]]]
        #         fl = open(f, 'wb')
        #         pickle.dump(info,fl)
        #         fl.close()
        #         createPasswordsList()

        # def editPassword():
        #     #edits password, saves, and recreates listbox
        #     listbox.unbind("<<ListboxSelect>>")
        #     selection = listbox.curselection()[0]
        #     def closec():
        #         #closes Toplevel
        #         c.destroy()

        #     def save():
        #         #saves password to .lokr file
        #         if newp.get() == newpc.get():
        #             lbls = parseLokrFile(f, 'labels')
        #             keys = parseLokrFile(f, "keys")
        #             #COMBAK the following line can be a method with deletePassword(its repeating)
        #             fl = open(f, 'rb')
        #             fl.seek(0)
        #             info = pickle.load(fl)
        #             fl.close()
        #             del info[lbls[selection]]
        #             fl = open(f, 'wb')
        #             pickle.dump(info,fl)
        #             fl.close()
        #             savePassword(f[:-5], newl.get(), newp.get(), int(keys[selection]))
        #             conf.config(text='Password has been successfully saved!')
        #             createPasswordsList()
        #             cb = tk.Button(c, text='CLOSE WINDOW', command = closec)
        #             cb.pack()
        #         else:
        #             conf.config(text='Passwords do not match. Please retry.')
        #         createPasswordsList()

            # lbls = decryptLokr(f, 'labels')
            # pwds = decryptLokr(f, 'pwds')
            # c = tk.Toplevel(takefocus=True)
            # c.title("Edit Password for " + lbls[listbox.curselection()[0]])
            # c.geometry('250x300')
            # l = tk.Label(c, text = 'EDIT A PASSWORD:\n')
            # newll = tk.Label(c, text = 'Edit label:')
            # newl = tk.Entry(c)
            # newl.insert(tk.INSERT, lbls[listbox.curselection()[0]])
            # newpl = tk.Label(c, text='Edit password:')
            # newp = tk.Entry(c, show='*')
            # newp.insert(tk.INSERT, pwds[listbox.curselection()[0]])
            # newpcl = tk.Label(c, text='Confirm password:')
            # newpc = tk.Entry(c, show='*')
            # eb = tk.Button(c, text='SAVE PASSWORD', command = save)
            # cancel = tk.Button(c, text='Cancel', command=closec)
            # conf = tk.Label(c, text = '')
            # l.pack()
            # newll.pack()
            # newl.pack()
            # newpl.pack()
            # newp.pack()
            # newpcl.pack()
            # newpc.pack()
            # eb.pack()
            # cancel.pack()
            # conf.pack()
            # listbox.bind("<<ListboxSelect>>", getPasswordSelection)

        # def encryptPassword():
        #     #creates new window w/ encrypt pwd prompts, stores pwd, lbl, and key to lokr file
        #     def checkcheck():
        #         #checks the checkbutton, whether 1 or 0 and blanks out key field or unblanks
        #         if cv.get() == 1:
        #             k.delete(0, tk.END)
        #             k.configure(state=tk.DISABLED)
        #         else:
        #             k.configure(state=tk.NORMAL)

        #     def storeencpass():
        #         #makes sure pwds match and stores pwds
        #         if newp.get() == newpc.get():
        #             if cv.get() == 1:
        #                 pk = random.randint(1, 26)
        #             else:
        #                 pk = int(k.get())
        #             savePassword(f[:-5], newl.get(), newp.get(), pk)
        #             conf.config(text='Password has been successfully encrypted!')
        #             createPasswordsList()
        #             def closet():
        #                 t.destroy()
        #             c = tk.Button(t, text='CLOSE WINDOW', command = closet)
        #             c.pack()
        #         else:
        #             conf.config(text='Passwords do not match. Please retry.')

        #     listbox.unbind("<<ListboxSelect>>")
        #     cv = tk.IntVar()
        #     t = tk.Toplevel()
        #     t.geometry('250x300')
        #     l = tk.Label(t, text = 'ENCRYPT A NEW PASSWORD:\n')
        #     newll = tk.Label(t, text = 'Enter password identifier/label:')
        #     newl = tk.Entry(t)
        #     kl = tk.Label(t, text = 'Enter an encryption key(1 - 26):')
        #     k = tk.Entry(t)
        #     kc = tk.Checkbutton(t, text="Auto select a random key", variable = cv, command=checkcheck)
        #     newpl = tk.Label(t, text='Enter password:')
        #     newp = tk.Entry(t, show='*')
        #     newpcl = tk.Label(t, text='Confirm password:')
        #     newpc = tk.Entry(t, show='*',)
        #     eb = tk.Button(t, text='ENCRYPT PASSWORD', command = storeencpass)
        #     conf = tk.Label(t, text = '')
        #     l.pack()
        #     newll.pack()
        #     newl.pack()
        #     kl.pack()
        #     k.pack()
        #     kc.pack()
        #     newpl.pack()
        #     newp.pack()
        #     newpcl.pack()
        #     newpc.pack()
        #     eb.pack()
        #     conf.pack()
        #     listbox.bind("<<ListboxSelect>>", getPasswordSelection)
        # for file in os.listdir(os.getcwd()):
        #     #finds all lokr files in cwd
        #     if file.endswith(".lokr"):
        #         results.append(file)
        # for file in results:
        #     #sets f the current users' filename
        #     if file.startswith(crypt.encrypt(usrname, 11)):
        #         f = file
        # pwds = parseLokrFile(f, 'pwds')
        # sellbl = tk.Label(rightframe, text = 'Lokr File associated with account :  ' )
        # sellbl.config(text = 'You are logged in as: ' + usrname + '\nThe Lokr File that is associated with your account is: ' +  f)
        # sellbl.pack(side='top')
        # scrollbar = tk.Scrollbar(bottomframe)
        # listboxtitle = tk.Label(leftframe, text='Passwords:', font = ("Verdana", 12))
        # listbox = tk.Listbox(bottomframe, font = ("Verdana", 12), yscrollcommand=scrollbar.set)

        # def createPasswordsList():
        #     #creates listbox w/ decrypted pwd labels
        #     listbox.delete(0,tk.END)
        #     lbls = decryptLokr(f, 'labels')
        #     scrollbar.pack(side='right', fill ='y')
        #     listboxtitle.pack()
        #     listbox.pack()
        #     scrollbar.config(command = listbox.yview)
        #     lblsd = dict(enumerate(lbls))
        #     for ind, lbl in list(lblsd.items()):
        #         listbox.insert(ind, lbl)

        # def getPasswordSelection(event):
        #     #runs everytime an item in listbox is clicked
        #     lbls = decryptLokr(f, 'labels')
        #     keys = parseLokrFile(f, 'keys')
        #     pwds = parseLokrFile(f, 'pwds')
        #     lbllbl.config(text='LABEL:\n' + lbls[listbox.curselection()[0]])
        #     pwdlbl.config(text='PASSWORD:\n' + pwds[listbox.curselection()[0]])
        #     keylbl.config(text='KEY:\n' + str(keys[listbox.curselection()[0]]))

        if pwds is not None:
            createPasswordsList()
        #create and place button on screen
        # e = tk.Button(rightframe, text = 'ENCRYPT PASSWORD', width = 30, pady = 5, command = encryptPassword)
        # d = tk.Button(brightframe, text = 'SHOW DECRYPTED\nPASSWORD', width = 20, pady = 5, command = showDecryptedPassword)
        # cp = tk.Button(brightframe, text = 'COPY PASSWORD\nTO CLIPBOARD', width = 20, pady = 5, command = copyPasswordToClipboard)
        # delete = tk.Button(rightframe, text = 'DELETE PASSWORD', width = 30, pady = 5, command = deletePassword)
        # change = tk.Button(rightframe, text = 'EDIT PASSWORD', width = 30, pady = 5, command = editPassword)
        # e.pack()
        # delete.pack()
        # change.pack()
        # d.grid(row=0,column=2)
        # cp.grid(row=1,column=2)
        # listbox.bind("<<ListboxSelect>>", getPasswordSelection)
        # lbllbl = tk.Label(brightframe, text='LABEL:\n')
        # lbllbl.grid(row = 0 , column = 0)
        # pwdlbl = tk.Label(brightframe, text='PASSWORD:\n')
        # pwdlbl.grid(row =1, column = 0)
        # keylbl = tk.Label(brightframe, text='KEY:\n')
        # keylbl.grid(row=2, column =0,)
    # else:
    #     confirm.config(text='Your username and/or password is incorrect.' )
    #     usr.delete(0, tk.END)
    #     pas.delete(0, tk.END)

#LOGIN GUI METHODS
# def cleart():
#     #clears entry fields
#     usr.delete(0, tk.END)
#     pas.delete(0, tk.END)
#     confirm.config(text=' ' )

# def ee():
#     #exits
#     quit()

# def newuser():
#     #shows prompts to create new user and create new SL locker
#     newusrl = tk.Label(window, text='Create a username:')
#     newusrl.pack()
#     newusr = tk.Entry(window)
#     newusr.pack()
#     newpasl = tk.Label(window, text='Create a password:')
#     newpasl.pack()
#     newpas = tk.Entry(window, show='*')
#     newpas.pack()
#     newconl = tk.Label(window, text='Confirm password:')
#     newconl.pack()
#     newcon = tk.Entry(window, show='*')
#     newcon.pack()
#     window.unbind("<Return>")
#     def reg():
#         #makes sure no two usr names are same, creates locker and displays success lbl
#         if (newusr.get() in users) == False and newpas.get() == newcon.get():
#             un = newusr.get()
#             pw = newpas.get()
#             saveUser(crypt.encrypt(un, 7), crypt.encrypt(pw, 7))
#             createLokr(crypt.encrypt(un, 11))
#             confirm.config(text='You have successfully registered!\n A new Lokr has been created for you.')
#             newusrl.pack_forget()
#             newusr.pack_forget()
#             newpasl.pack_forget()
#             newpas.pack_forget()
#             newconl.pack_forget()
#             newcon.pack_forget()
#             register.pack_forget()
#             window.bind("<Return>")
#         else:
#             confirm.config(text='Username already exists or passwords do not match. Please retry.')
#             window.bind("<Return>", checkusr)
#     register = tk.Button(window, text="Register!", command=reg)
#     register.pack(expand = True)

"""
██╗      ██████╗  ██████╗ ██╗███╗   ██╗     ██████╗ ██╗   ██╗██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔════╝ ██║   ██║██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██║  ███╗██║   ██║██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██║   ██║██║   ██║██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ╚██████╔╝╚██████╔╝██║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝     ╚═════╝  ╚═════╝ ╚═╝
"""

# ex = tk.Button(window, text = 'Exit', command= ee)
# logo = tk.PhotoImage(file='lock.png')
# logolbl = tk.Label(window, text= '\n', image=logo, pady = 50)
# title = tk.Label(window, text="Lokr",  font =('Lucida Console', 40))
# logtitle = tk.Label(window, text="\nVersion: " + str(ver) + "\n\nPlease Login:")
# usr = tk.Entry(window)
# pas = tk.Entry(window, show='*')
# usrl = tk.Label(window, text='Username:')
# pasl = tk.Label(window, text='Password:')
# login = tk.Button(window, text='Launch', command=checkusr)
# newusr = tk.Button(window, text = 'Register', command=newuser)
# clear = tk.Button(window, text = 'Clear', command=cleart)
# confirm = tk.Label(window)
# logolbl.pack()
# title.pack()
# logtitle.pack()
# usrl.pack()
# usr.pack()
# pasl.pack()
# pas.pack()
# login.pack()
# newusr.pack()
# clear.pack()
# confirm.pack()
# window.bind("<Return>", checkusr)

#START WINDOW
window.wm_iconbitmap(window, default ='closedlock.ico')
window.title('LOKR LOGIN')
window.mainloop()
