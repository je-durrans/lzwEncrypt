import sys

ALPHABET = ' abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.'

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
            print('get returning', index - 1)
            return index - 1

def lzwCompress(message, dic):
    ret = []
    while message:
        if message in dic.keys():
            ret.append(dic[message])
            message = ''
        else:
            print('message is', message)
            index = getLongestEncodableIndex(message, dic)
            fragment = message[:index]
            print(index, fragment)
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
    file = open(filename, 'r')
    ret = file.read()
    file.close()
    return ret.strip()

if __name__ == '__main__':
    inf, out, pw = sys.argv[1:4]
    text = readf(inf)
    printf(lzwCompress(text, createDict(pw)), out)
    printf(lzwDecompress(readf(out), createDict(pw)), inf)
    print(inf, out, pw)
    
