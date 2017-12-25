import sys

ALPHABET = ' abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.'

def createDict(passphrase=''):
    dic = {}
    for character in passphrase+ALPHABET:
        if character not in dic.keys():
            dic[character] = len(dic)
    return dic

def getLongestEncodableIndex(message, dic):
    
    for index in range(1, len(message)+1):
        if message[:index] not in dic.keys():
            return index - 1

def lzwCompress(message, dic):
    ret = []
    while message:
        if message in dic:
            ret.append(dic[message])
            message = ''
        else:
            index = getLongestEncodableIndex(message, dic)
            fragment = message[:index]
            newEntry = message[:index+1]
            message = message[index:]
            ret.append(dic[fragment])
            dic[newEntry] = len(dic)
    print(len(dic))
    return ret

def lzwDecompress(message, dic):
    ret = ""
    return ret

def printf(message, filename):
    file = open(filename, 'w')
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
    printf(lzwCompress(text, createDict()), sys.argv[2])
    print(inputFile, outputFile, passphrase)
    print(createDict(passphrase))
