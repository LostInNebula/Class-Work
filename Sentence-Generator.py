def follow_words(text):
    '''
    Purpose: to return a dictionary that equates each word to all the words that have been seen to follow the said word in the string
    Parameter(s): text: a string
    Return Value(s): word_dict: a dictionary of words in the string and what words have been seen to follow said word
    '''
    textlist = text.split()
    word_dict = {}
    next_word_list = []

    for  word in (textlist):
        for i in range(len(textlist)):
            if textlist[i] == word:
                if i != len(textlist) - 1:
                    next_word_list.append(textlist[i+1])
        
        word_dict[word] = next_word_list
        next_word_list = []
    
    for word in word_dict.copy():
        if word_dict.copy()[word] == []:
            del word_dict[word]

    

    return word_dict

def auto_complete(follows_dict, current):
    '''
    Purpose: returns a list of all the words that have been seen to follow a target word 
    Parameter(s): follows_dict: a dictionary of each word in a string and the words that have been seen to follow said word
                  current: a word (preferably within follows_dict)
    Return Value(s): follows_dict[current]: the list of all the words that have been seen to follow the target word
                     keyslist: a list of all the keys in follows_dict which are the possible choices for the target word
    '''
    keyslist = []

    if current in follows_dict:
        return follows_dict[current]
    else:
        for keys in follows_dict:
            keyslist.append(keys)
        return keyslist

def random_sent(fname, max_length):
    '''
    Purpose: to return a string that is at most a user requested length long that has been randomly generated via analyizing a given text file
             and the words within said file based on what words tend to follow each word.
    Parameter(s): fname: a text file
                  max_length: the maximum length of the sentence that is to be generated
    Return Value(s): setnence: a randomly generated string
    '''
    word_string = ""
    sentence = ""
    count = 0
    
    with open(fname, 'r') as words:
        word_list =  words.read().split()

        for i in range(len(word_list)):
            word_string += word_list[i]
            word_string += " "

        follow = follow_words(word_string)
        current_word = random.choice(word_list)
        sentence += current_word
        sentence += " "
        count += 1

        while count < max_length:
            random_choice = random.choice(auto_complete(follow, current_word))
            current_word = random_choice

            if count == max_length - 1:
                sentence += random_choice
                count += 1
            else: 
                if "." in random_choice or "?" in random_choice or "!" in random_choice:
                    sentence += random_choice
                    break
                else:
                    sentence += random_choice
                    sentence += " "
                    count += 1
            
        return sentence
