import unicodedata

IS_NOT_ACCENTED = "Mn"

FORM_NORMALIZE = "NFKD"


class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        result = []
        key_index = 0
        for char in text:
            if char.isalpha():
                char = unicodedata.normalize("%s" % FORM_NORMALIZE, char)
                for letterDiacritical in char:
                    if unicodedata.category(letterDiacritical) != IS_NOT_ACCENTED:
                        char = "".join(letterDiacritical)
                    else:
                        continue
                shift = ord(self.key[key_index % len(self.key)].lower()) - ord('a')
                if char.isupper():
                    result_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                else:
                    result_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                key_index += 1
            else:
                result_char = char
            result.append(result_char)
        return ''.join(result)

    def decrypt(self, text):
        result = []
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].lower()) - ord('a')
                if char.isupper():
                    result_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
                else:
                    result_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
                key_index += 1
            else:
                result_char = char
            result.append(result_char)
        return ''.join(result)
