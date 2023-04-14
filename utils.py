import sha
import tools
import RSA
import re

def sign(filename, priv):
    key = tools.readkeyfile(priv)
    N = int(key[1])
    d = int(key[2])

    if tools.getextension(filename) == '.txt':
        contents = tools.readtxt(filename)
    else:
        contents = tools.readbin(filename)

    start_ds = contents.find("\n<ds>")
    msgdigest = int.from_bytes(sha.hash(contents[:start_ds]), "big")
    sign = RSA.dekripsiRSA(msgdigest, d, N)
    digsign = f"""\n<ds>{sign}</ds>"""

    if tools.getextension(filename) == '.txt':
        tools.appendsignaturetxt(contents[:start_ds] + digsign, filename)
    else:
        tools.writefile(digsign, filename)


def validate(filename, publ, signfile=""):
    key = tools.readkeyfile(publ)
    N = int(key[1])
    # print(N.bit_length())
    e = int(key[2])
    if tools.getextension(filename) == ".txt":
        contents = tools.readtxt(filename)
        pisah = re.split(r'\n<ds>|</ds>', contents)
        msgdigest = sha.hash(pisah[0])
        # print(msgdigest)
    else:
        contents = tools.readbin(filename)
        pisah = re.split(r'<ds>|</ds>', tools.readtxt(signfile))
        msgdigest = sha.hash(pisah[0])
    sign = pisah[1]
    # print(sign)
    signdig = RSA.enkripsiRSA(int(sign), e, N)
    digest = int.from_bytes(msgdigest, "big")
    # print("digest:", digest, "sign:", signdig)
    if digest == signdig:
        return("VALID.")
    else:
        return("INVALID!")