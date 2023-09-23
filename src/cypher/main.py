from VigenereCipherUnicodeData import VigenereCipher
from attackVCUD import FrequencyAnalysisAttackPT, FrequencyAnalysisAttackENG
from frequencia_util import ENGLISH_FREQ, PORTUGUES_FREQ


def cifrar():
    chave = input("Digite a chave de cifragem: ")
    mensagem = input("Digite a mensagem a ser cifrada: ")
    idioma = input("Digite o idioma (portugues ou ingles): ")

    if idioma.lower() == "portugues":
        vigenere = VigenereCipher(chave)
    elif idioma.lower() == "ingles":
        vigenere = VigenereCipher(chave)
    else:
        print("Idioma não suportado. Use 'portugues' ou 'ingles'.")
        return

    mensagem_cifrada = vigenere.encrypt(mensagem)
    print("Mensagem cifrada:", mensagem_cifrada)


def decifrar():
    chave = input("Digite a chave de decifragem: ")
    mensagem_cifrada = input("Digite a mensagem cifrada: ")
    idioma = input("Digite o idioma (portugues ou ingles): ")

    if idioma.lower() == "portugues":
        vigenere = VigenereCipher(chave)
    elif idioma.lower() == "ingles":
        vigenere = VigenereCipher(chave)
    else:
        print("Idioma não suportado. Use 'portugues' ou 'ingles'.")
        return

    mensagem_decifrada = vigenere.decrypt(mensagem_cifrada)
    print("Mensagem decifrada:", mensagem_decifrada)


def ataque_frequencia():
    texto = input("Digite o texto cifrado: ")
    idioma = input("Digite o idioma do texto (portugues ou ingles): ")

    if idioma.lower() == "portugues":
        attack = FrequencyAnalysisAttackPT(texto, PORTUGUES_FREQ)
    elif idioma.lower() == "ingles":
        attack = FrequencyAnalysisAttackENG(texto, ENGLISH_FREQ)
    else:
        print("Idioma não suportado. Use 'portugues' ou 'ingles'.")
        return

    keys = attack.get_keys()
    print("Chaves possíveis:", keys)


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cifrar")
        print("2. Decifrar")
        print("3. Ataque de Frequência")
        print("4. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cifrar()
        elif opcao == "2":
            decifrar()
        elif opcao == "3":
            ataque_frequencia()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
