def isPrima(x):
    if (x > 1):
        for i in range(2, int(x/2)+1):
            if (x % i) == 0:
                return True
                break
    else:
        return False

def relatifPrima(x,y):
   while(y):
       x, y = y, x % y
   if x == 1:
       return True
   else:
       return False

def kunciPrivatD(phi, e):
    k = 1
    found = False
    while not(found):
        d = ((1+k*phi)/e)
        if (d % 1) != 0:
            k += 1
        else:
            return d

def alphabetOnly(text):
    textUpperCase = text.upper()
    return ''.join(i for i in textUpperCase if i.isalpha())

def textToInt(text):
    listofText = []
    for i in range(len(text)):
        x = (ord(text[i]))
        listofText.append(x)
    return (listofText)

def enkripsiRSA(text, e, n):
    cipher = []
    for i in range (len(text)):
        temp = (text[i] ** e) % n
        cipher.append(temp)
    return cipher

def dekripsiRSA(text, d, n):
    plaintext = []
    for i in range (len(text)):
        temp = text[i]
        for j in range (int(d) - 1):
            temp = temp * text[i]
        temp = temp % n
        plaintext.append(chr(temp))

    return plaintext

text = "hah gimana alice?"
p = 47 #input user dicek dulu di isprima
q = 71 #input user dicek dulu di isprima
n = p*q
phi = (p-1)*(q-1)
e = 79 #input user dicek dulu di fungsi relatif prima
d = kunciPrivatD(phi, e)

print(n)
print(phi)
print(d)

#y = alphabetOnly(text)
x = textToInt(text)

print(x)

z = enkripsiRSA(x, e, n)
print(z)

a = dekripsiRSA(z, d, n)
print(a)