import itertools

from src.cypher.VigenereCipherUnicodeData import VigenereCipher
from src.util.frequencia_util import ENGLISH_FREQ, PORTUGUES_FREQ

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class FrequencyAnalysisAttack:
    def __init__(self, text, language_freq):
        self.FREQ = language_freq
        self.keys = self._solve_vigenere(text)

    def __str__(self):
        return str(self.keys)

    def get_keys(self):
        return self.keys

    def vigenere(self, plaintext, key, a_is_zero=True):
        key_iter = itertools.cycle(map(ord, key))
        decrypted_text = ""
        for letter in plaintext.lower():
            if letter in ALPHABET:
                shift = (next(key_iter) - ord('a') + ord(letter) - ord('a')) + (0 if a_is_zero else 2)
                decrypted_letter = chr(ord('a') + (shift % 26))
                decrypted_text += decrypted_letter
            else:
                decrypted_text += letter
        return decrypted_text

    def vigenere_decrypt(self, ciphertext, key, a_is_zero=True):
        inverse_key = "".join(chr(ord('a') + ((26 if a_is_zero else 22) - (ord(k) - ord('a'))) % 26) for k in key)
        return self.vigenere(ciphertext, inverse_key, a_is_zero)

    def compare_frequency(self, text):
        if not text:
            return None
        text = [t for t in text.lower() if t in ALPHABET]
        freq = [0] * 26
        total = float(len(text))
        for l in text:
            freq[ord(l) - ord('a')] += 1
        return sum(abs(f / total - E) for f, E in zip(freq, self.FREQ))

    def _solve_vigenere(self, text, min_key_size=None, max_key_size=None, a_is_zero=True):
        best_keys = []
        min_key_size = min_key_size or 1
        max_key_size = max_key_size or 20

        text_letters = [c for c in text.lower() if c in ALPHABET]

        for key_length in range(min_key_size, max_key_size):
            key = [None] * key_length
            for key_index in range(key_length):
                letters = "".join(itertools.islice(text_letters, key_index, None, key_length))
                shifts = []
                for key_char in ALPHABET:
                    shifts.append((self.compare_frequency(VigenereCipher(key_char).decrypt(letters)), key_char))
                key[key_index] = min(shifts, key=lambda x: x[0])[1]
            key_str = "".join(key)
            if key_str not in best_keys:  # Check if the key is not already in the list
                best_keys.append(key_str)

        best_keys.sort(key=lambda key: self.compare_frequency(self.vigenere_decrypt(text, key, True)))
        self.keys = best_keys[:2]
        return self.keys.__getitem__(0)


class FrequencyAnalysisAttackPT(FrequencyAnalysisAttack):
    def __init__(self, text, language_freq=PORTUGUES_FREQ):
        super().__init__(text, language_freq)


class FrequencyAnalysisAttackENG(FrequencyAnalysisAttack):
    def __init__(self, text, language_freq=ENGLISH_FREQ):
        super().__init__(text, language_freq)
