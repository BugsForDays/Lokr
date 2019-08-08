from Lokr import Lokr

class Manager:
    def __init__(self, lokr_object):
        lokr = lokr_object

    def deletePassword():
        #deletes selected password from listbox and recreates the listbox
        lbls = decryptLokr(f, 'labels')
        confirmbox = messagebox.askyesno(title='LOKR MANAGER', message='Are you sure you want to delete the password for ' + lbls[listbox.curselection()[0]])
        if confirmbox == True:
            lokr.deletePassword(listbox.curselection()[0])
            
            createlistbox()

    def copyPasswordToClipboard():
        #copies decrypted pwd to clipboard
        pwds = decryptLokr(f, 'pwds')
        window.clipboard_clear()
        window.clipboard_append(pwds[listbox.curselection()[0]])

    def hideDecryptedPassword():
        #changes display text of password label and button
        pwds = parseLokrFile(f, 'pwds')
        pwdlbl.config(text = '')
        pwdlbl.config(text = 'PASSWORD:\n' + pwds[listbox.curselection()[0]])
        d.config(text = 'SHOW DECRYPTED\nPASSWORD')
        d.config(command = showDecryptedPassword)
    
    def showDecryptedPassword():
        #changes password label and button display text, displayed decrypted pwd
        pwds = decryptLokr(f, 'pwds')
        pwdlbl.config(text = 'PASSWORD:\n' + pwds[listbox.curselection()[0]])
        d.config(text = 'HIDE DECRYPTED\nPASSWORD')
        d.config(command = hideDecryptedPassword)