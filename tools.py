import pathlib
import RSA

# read key file
def readkeyfile(filename):
    with open(filename, "r") as file:
        contents = file.read().split(",")
    return contents

# read txt file
def readtxt(filename):
    with open(filename, "r") as file:
        contents = file.read()
    return contents

# read non-txt file in bin
def readbin(filename):
    with open(filename, "rb") as file:
        contents = file.read()
    return contents

# get file extension
def getextension(filename):
    extension = pathlib.Path(filename).suffix
    return extension

# append key to txt file
def appendsignaturetxt(sign, filename):
    with open(f'''{pathlib.Path(filename).stem}.txt''', "w") as file:
        file.write(sign)
    file.close()

# write file
def writefile(contents, filename):
    with open(f'''{pathlib.Path(filename).stem}.txt''', "w") as file:
        file.write(contents)
    file.close()

# write key
def writekey(filename):
    keySize = 512
    e, d, N = RSA.keyGenerator()

    filepub = open(filename + ".pub", 'w')
    filepub.write(f"""{str(keySize)},{str(N)},{str(e)}""")
    filepub.close()
    
    filepri = open(filename + ".pri", 'w')
    filepri.write(f"""{str(keySize)},{str(N)},{str(d)}""")
    filepri.close()