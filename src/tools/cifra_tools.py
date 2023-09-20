class CipherTools:
    def replace_text(self, text):
        # Remove punctuation and digits, and convert to lowercase
        punctuation_to_remove = " .,“”—-_:;?!/\\'\"()[]{}`*&#%$#@<>"
        text = ''.join(char.lower() for char in text if char not in punctuation_to_remove and not char.isdigit())
        return text

    def process_key(self, key, text_length):
        if len(key) < text_length:
            new_key = key * int((text_length / len(key)))
            if len(new_key):
                new_key = new_key + key[: len(new_key)]
            return new_key.lower()
        return key.lower()

    def shift_alphabet(self, alphabet, char_index):
        # Shift the alphabet cyclically by a given amount
        if char_index == 0: # se a posição for zero, não desloca o alfabeto
            return alphabet
        shifted_alphabet = alphabet[char_index:] + alphabet[:char_index]
        return shifted_alphabet