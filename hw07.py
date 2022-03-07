def cg_pairs(dna):
    '''
    Purpose: to calculate the fraction of "cg" pairs of dinucleotides in a sequence of DNA
    Parameter(s): dna: a dna sequence consisting of (a's, c's, g's, and t's)
    Return Value: the fraction "cg" pairs of dinucleotides in the dna sequence
    '''

    cg_count = 0
    lcdna = dna.lower()

    for i in range(len(lcdna)):
        if lcdna[i] != "a" and lcdna[i] != "c" and lcdna[i] != "g" and lcdna[i] != "t":
            print("Error in DNA strand")
            return 0.0
        else:
            if lcdna[i:i+2] == "cg":
                cg_count +=1

    return cg_count / (len(dna)-1)

def segment(dna, frame):
    '''
    Purpose: to reorganize an inputed sequence of dna into codons based on a chosen reading frame
    Parameter(s): dna: a dna sequence consisting of (a's, c's, g's, and t's)
                  frame: a selection of a reading frame, either 0, 1, or 2
    Return Value: framelist: the original dna sequence reorganized as codons according to the reading frame
    '''

    framelist = []

    if frame == 0:
        for i in range(0, len(dna), 3):
            framelist.append(dna[i:i+3])
    if frame == 1:
        framelist.append(dna[0])
        for i in range(1, len(dna), 3):
            framelist.append(dna[i:i+3])
    if frame == 2:
        framelist.append(dna[0:2])
        for i in range(2, len(dna), 3):
            framelist.append(dna[i:i+3])

    return framelist

def mark_dna(dna, target):
    '''
    Purpose: to mark a specific target sequence each time it appears in an inputted dna sequence
    Parameter(s): dna: a dna sequence consisting of (a's, c's, g's, and t's)
                  target: a specific dna sub-sequence to be located in the dna sequence
    Return Value: searched_dna: the original dna sequence with each occurence of the target marked
    '''
    # this function was an absolute living nightmare to make
    searched_dna = ''
    i = 0
    slicesize = len(target)

    while i < len(dna):
        if dna[i: i + slicesize] == target:
            searched_dna += (">>" + dna[i:i+slicesize] + "<<")
            i += slicesize
        else:
            searched_dna += dna[i]
            i += 1

    return searched_dna

def find_url(html):
    '''
    Purpose: to find and return the url link within an inputted html source code
    Parameter(s): html: the html source code
    Return Value: url: the url link within the html source code
    '''

    url = ''

    for i in range(len(html)):
        if html[i:i+5] == "href=":
            for j in range(i+7, len(html)):
                if html[j] == "\"":
                    url += html[i+6: j]
                    break

    return str(url)
