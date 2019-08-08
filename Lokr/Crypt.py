class Crypt:

    def __init__(self, cipher_text, plain_text):
        self.cipher_text = cipher_text
        self.plain_text = plain_text

    # ENCRYPTION/DECRYPTION METHODS
    def translateCipher(self, cp, key):
        #reorder cipher based on key, returns: cipher as new cipher list
        return cp[key:] + cp[0:key]

    def encrypt(self, text, key):
        #encrypt text with key via string construction, returns: encrypted text as string
        encrypted = ''
        newCharset = list(self.translateCipher(self.plain_text, key))
        for i in range(len(text)):
            if text[i] in newCharset:
                encrypted += self.cipher_text[newCharset.index(text[i])]
        return encrypted

    def decrypt(self, text, key):
        #inverse of encrypt(): decrypts text based on key, returns: decrypted text as string
        decrypted = ''
        newCharset = list(self.translateCipher(self.plain_text, int(key)))
        for i in range(len(text)):
            if text[i] in self.cipher_text:
                decrypted += newCharset[self.cipher_text.index(text[i])]
        return decrypted
