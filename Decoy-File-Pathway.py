def is_target(lines):
    '''
    Parameter(s):
        lines: a list of strings
    Purpose:
        to determine if a list of strings is True or False, being True if every string within the list contains at least an "A",
        "C", "M", or "E", otherwise it is False
    Return Value(s):
        True: returned if every string within the list contains at least an "A", "C", "M", or "E"
        False: returned if at least 1 string within the list doesn't contain an "A", "C", "M", or "E"
        is_target(lines[1:]): a variation of the initial list that continiously loses its 0th element each iteration of the recursion
    '''

    if len(lines) == 0:
            return True
    else:
        if "A" not in lines[0] and "C" not in lines[0] and "M" not in lines[0] and "E" not in lines[0]:
            return False
        else:
            return is_target(lines[1:])
    
def all_targets(path,list=False):
    '''
    Parameter(s):
        path: a directory
        list: a list containing True files, according to the is_target function, currently known by the function
              this is automatically set to False as to give an oppurtunity for an empty list to be created, without it ever
              being overwritten by the recursion
    Purpose:
        to return a list containing every True file in a directory
    Return Value(s):
        list: a list containing True files, according to the is_target function, currently known by the function
    '''
    
    if list == False:
        list = []

    for file in os.listdir(path): 
        if os.path.isfile(path+'/'+file):
            print(path+'/'+file)  #This is a file, print out the path
            with open(path+'/'+file, 'r') as lines:
                if is_target(lines.readlines()) == True:
                    list.append(str((path+'/'+file)))
        else:
            list = all_targets(path+'/'+file,list)  #Go into a subdirectory
    
    return list
