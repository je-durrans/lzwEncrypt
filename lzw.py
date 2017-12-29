import sys

ALPHABET = ' \nabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.,[]'

def createDict(passphrase=''):
    dic = {}
    for character in passphrase+ALPHABET:
        if character not in dic.keys():
            dic[character] = len(dic)
    return dic

def invertDict(dic):
    return {v: k for k, v in dic.items()}

def getLongestEncodableIndex(message, dic):
    
    for index in range(1, len(message)+1):
        if message[:index] not in dic.keys():
            return index - 1

def lzwCompress(message, dic):
    ret = []
    while message:
        if message in dic.keys():
            ret.append(dic[message])
            message = ''
        else:
            index = getLongestEncodableIndex(message, dic)
            if not index: break
            fragment = message[:index]
            newEntry = message[:index+1]
            message = message[index:]
            ret.append(dic[fragment])
            dic[newEntry] = len(dic)
    return ret

def lzwDecompress(message, dic):
    ret = ""
    dic = invertDict(dic)
    message = eval(message)
    print(message)
    while message:
        num = message.pop(0)
        add = dic[num]
        ret += add
        if not message: break
        try:
            dic[len(dic)] = add+dic[message[0]][0] 
        except KeyError:
            dic[len(dic)] = add+add[0] 
    return ret

def printf(message, filename):
    file = open(filename, 'w')
    print(message, file=file)
    file.close()

def readf(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print('File not found, exiting')
        sys.exit()
    ret = file.read()
    file.close()
    return ret.strip()

def usage():
    print('Usage text')

if __name__ == '__main__':
    n = len(sys.argv)-1
    passphrase = ''
    if not n: usage(), sys.exit() 
    decode = sys.argv[1]=='-d'
    if decode:
        sys.argv.pop(1)
        n-=1
    inf, out = sys.argv[1:3]
    if n == 3: passphrase = sys.argv[3]

    text = readf(inf)
    function = lzwDecompress if decode else lzwCompress
    printf(function(text, createDict(passphrase)), out)
