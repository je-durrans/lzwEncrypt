import sys

ALPHABET = ' abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def createDict(passphrase=''):
    dic = {}
    for character in passphrase+ALPHABET:
        if character not in dic.keys():
            dic[character] = len(dic)
    return dic

def lzwCompress(message, dic):
    ret = []
    return ret

def lzwDecompress(message, dic):
    ret = ""
    return ret

def printf(message, filename):
    file = open(filename, 'a')
    print(message, file=file)
    file.close()

def readf(filename):
    file = open(filename, 'r')
    ret = file.read()
    file.close()
    return ret

if __name__ == '__main__':
    inputFile, outputFile, passphrase = sys.argv[1:4]
    text = readf(sys.argv[1])
    printf(text, sys.argv[2])
    print(inputFile, outputFile, passphrase)
    print(createDict(passphrase))
