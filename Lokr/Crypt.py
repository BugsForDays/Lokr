class Crypt:

    def __init__(self, cipher_text, plain_text):
        self.cipher_text = cipher_text
        self.plain_text = plain_text

    # ENCRYPTION/DECRYPTION METHODS
    def translateCipher(self, cipher_text, key):
        # reorder cipher based on key, returns: cipher as new cipher list
        return cipher_text[key:] + cipher_text[0:key]

    def encrypt(self, text, key):
        # encrypt text with key via string construction, returns: encrypted text as string
        encrypted = ''
        translated_cipher = list(self.translateCipher(self.plain_text, key))
        for char in range(len(text)):
            if text[char] in translated_cipher:
                encrypted += self.cipher_text[translated_cipher.index(text[char])]
        return encrypted

    def decrypt(self, text, key):
        # inverse of encrypt(): decrypts text based on key, returns: decrypted text as string
        decrypted = ''
        translated_plain = list(self.translateCipher(self.plain_text, int(key)))
        for char in range(len(text)):
            if text[char] in self.cipher_text:
                decrypted += translated_plain[self.cipher_text.index(text[char])]
        return decrypted
