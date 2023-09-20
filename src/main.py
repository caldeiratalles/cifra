from src.cypher.VigenereCipher import Encryptor, Decryptor
from src.cypher.VigenereCipherUnicodeData import VigenereCipher
from src.cypher.attackVCUD import FrequencyAnalysisAttack,FrequencyAnalysisAttackPT
from src.util.frequencia_util import ENGLISH_FREQ,PORTUGUES_FREQ

# #Mensagem a ser cifrada
# mensagem_cifrada = "quando estava escrevendo meu primeiro livro, comecei a hesitar se devia abri-lo com estas memórias pelo princípio ou pelo fim. isto é, se poria em primeiro lugar o meu nascimento ou a minha morte. suposto ou só vulgar, se começar pelo nascimento duas considerações me levaram a adotar diferente método. a primeira é que eu não sou propriamente um autor defunto, mas um defunto autor. para quem a campa foi outro berço. a segunda é que o escrito ficaria assim mais galante e mais novo. moisés que também contou a sua morte, não a pôs no introito, mas no cabo. diferença radical entre este livro e o pentateuco. isto é, entre as duas horas da tarde de uma sexta-feira do mês de agosto de 1869, que me vêem estreitar à cadeira do sr. lobato na chácara fluminense, e as palavras com que moises atabefinizou a sua alta obra. aqui começam as duas histórias."
#
# chave = "temporal"
#
# mensagem_cifrada = Encryptor(mensagem_cifrada, chave).processed_text()
# print("Mensagem cifrada:", mensagem_cifrada)
#
# mensagem_decifrada = Decryptor(mensagem_cifrada, chave).processed_text()
# print("Mensagem decifrada:", mensagem_decifrada)

# Sem unicode e em ingles
# mensagem_cifrada = "regulating the circulation.  whenever i find myself growing grim about the mouth; whenever it is a damp, drizzly november in my soul; whenever i find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral i meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off--then, i account it high time to get to sea as soon as i can.  this is my substitute for pistol and ball.  with a philosophical flourish cato throws himself upon his sword; i quietly take to the ship.  there is nothing surprising in this.  if they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
#
# chave = "arara"
# vigenere = VigenereCipher(chave)
#
# mensagem_cifrada = vigenere.encrypt(mensagem_cifrada)
# print("Mensagem cifrada:", mensagem_cifrada)
#
# mensagem_decifrada = vigenere.decrypt(mensagem_cifrada)
# print("Mensagem decifrada:", mensagem_decifrada)
#
# attack = FrequencyAnalysisAttack(mensagem_cifrada, ENGLISH_FREQ)
# print(attack)