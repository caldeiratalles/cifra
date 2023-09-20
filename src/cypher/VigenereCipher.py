from src.tools.cifra_tools import CipherTools

from src.tools.cifra_tools import CipherTools


class Cipher(CipherTools):
    def __init__(self, text, key, encrypt):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.text = self.replace_text(text)
        self.key = self.process_key(key, len(self.text))
        self.encrypt = encrypt

    def processed_text(self):
        result = ""
        for i, char in enumerate(self.text):
            if char.isalpha():  # se o caractere é uma letra
                char_index = self.alphabet.find(char.lower())  # encontra a posição da letra no alfabeto
                key_index = self.alphabet.find(self.key[i].lower())  # encontra a posição da letra da chave no alfabeto
                vigenere_table = self.create_vigenere_table()  # cria a tabela de Vigenère
                if self.encrypt:  # Criptografar
                    cipher_char = vigenere_table[key_index][
                        char_index]  # encontra a letra cifrada na interseção da linha da chave e da coluna do texto
                else:
                    cipher_char = self.alphabet[
                        vigenere_table[key_index].index(char.lower())]  # encontra a letra decifrada na tabela Vigenère
                if char.isupper():  # se o caractere original é maiúsculo
                    cipher_char = cipher_char.upper()  # converte a letra cifrada ou decifrada para maiúsculo
                result += cipher_char  # adiciona a letra cifrada ou decifrada ao resultado
            else:  # se o caractere não é uma letra
                result += char  # preserva o caractere original no resultado
        return result

    def __str__(self):
        return self.processed_text()

    def create_vigenere_table(self):
        table = []
        for i in range(26):
            table.append(self.shift_alphabet(self.alphabet, i))
        return table


class Encryptor(Cipher):
    def __init__(self, text, key):
        super().__init__(text, key, encrypt=True)


class Decryptor(Cipher):
    def __init__(self, text, key):
        super().__init__(text, key, encrypt=False)
