def idk():
    word = '0123wow!'
    p = '0123456789'
    ch = ''
    for i in range(len(word)):
        if word[i] not in p:
            ch += word[i]
    return ch

def doubleletters():
    list = []
    list2 = []
    word = input("enter a word ")
    while word != "":
        list.append(word)
        word = input("enter a word ")
    for i in range(len(list)):
        if list[i][0] in list[i][1:]:
            list2.append(list[i])
    return list2

def palindrome(word):
    if len(word) % 2 == 0:
        n = int(len(word)/2)
        half = word[:n]
        rest = word[n:]
    else:
        n = int(len(word)/2)
        half = word[:n]
        rest = word[n+1:]
    counter = 0
    for i in range(len(half)):
        if str(half[i]).lower() in str(rest).lower():
            counter += 1
    if counter == len(rest):
        return True
    else:
        return False

def igpay(word):
    if word[0] != "a" and word[0] != "e" and word[0] != "i" and word[0] != "o" and word[0] != "u":
        word = word[1:] + word[0] + "ay"
    else:
        word = word + "ay"

    return word
