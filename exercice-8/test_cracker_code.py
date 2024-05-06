"""Un texte a été chiffré avec une permutation de lettres
(en majuscules uniquement). Chaque lettre est remplacée par
une autre lettre, toujours la même.

Je vous donne un cryptogramme: vous connaissez une phrase chiffrée
avec ce code et sa version déchiffrée, à vous de déchiffrer l'autre
message.

Pour tester, je vous fournis le condensat (hash) du message à cracker.

Coverage: 100% et code testé

Mettez dans votre commit git le code cracké. Le test doit passer.

Ensuite, vous voulez produire vous-mêmes des messages: écrire la fonction.
"""
message_en_clair = "ON ETUDIE UNE FORME DE CODAGE PAR SUBSTITUTION"
message_chiffre = "JW XEDVLX DWX HJYUX VX CJVKBX MKY SDFSELEDELJW"

message_a_cracker = "ZX SXCYXE MJDY CYKCIXY DW CJVX CK YXSEX VX CJWELWDXY K XSSKGXY"

hash_du_message_dechiffre = 'b9aff3021b039a5923d11cb941d314c5ca0acd02'

from pprint import pprint
import hashlib
super_map_of_characters = {' ': ' ',
 'A': 'K',
 'B': 'F',
 'C': 'C',
 'D': 'V',
 'E': 'X',
 'F': 'H',
 'G': 'B',
 'H': 'A',
 'I': 'L',
 'J': 'N',
 'K': 'I',
 'L': 'Z',
 'M': 'U',
 'N': 'W',
 'O': 'J',
 'P': 'M',
 'Q': 'O',
 'R': 'Y',
 'S': 'S',
 'T': 'E',
 'U': 'D',
 'V': 'P',
 'W': 'Q',
 'X': 'R',
 'Y': 'G',
 'Z': 'T'}

def encrypt_text(cleartext: str) -> str:
    
    #map_of_characters = dict(zip(message_en_clair, message_chiffre))
    #print(map_of_characters)
    #alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #map_of_characters['L'] = 'Z'
    #map_of_characters['K'] = 'I'
    #map_of_characters['Y'] = 'G'
#
    #missing_source = [a for a in alphabet if a not in map_of_characters]
    #missing_dest = [a for a in alphabet if a not in map_of_characters.values()]
    #map_of_characters.update(dict(zip(missing_source, missing_dest)))
    #pprint(map_of_characters)
    #print("missing source", missing_source)
    #print("missing dest", missing_dest)
    map_of_characters = super_map_of_characters
    s = ""
    for c in cleartext:
        if c not in map_of_characters:
            raise ValueError(f"cannot encrypt because bad character [{c}]")
        s += map_of_characters[c]
    return s

print(encrypt_text('BONJOUR LES AMIS'))
def decrypt_text(encrypted: str) -> str:
    #map_of_characters = dict(zip(message_chiffre, message_en_clair))
    #map_of_characters['Z'] = 'L'
    #map_of_characters['I'] = 'K'
    #map_of_characters['G'] = 'Y'
    map_of_characters = {v: k for k, v in super_map_of_characters.items()}
    s = ""
    
    for c in encrypted:
        if c in map_of_characters:
            s += map_of_characters[c]
        else:
            s += f'[{c}]'
    print(s)
    return s

def test_crackage():
    assert decrypt_text(message_chiffre) == message_en_clair
    assert hashlib.sha1(decrypt_text(message_a_cracker).encode('utf-8')).hexdigest() == hash_du_message_dechiffre

def test_encodage():
    assert decrypt_text(encrypt_text('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert decrypt_text(encrypt_text('BONJOUR LES AMIS')) == 'BONJOUR LES AMIS'
