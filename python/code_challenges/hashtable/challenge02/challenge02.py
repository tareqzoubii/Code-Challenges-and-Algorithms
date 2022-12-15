import re
# Write here the code challenge solution

def repeated_word(sentence):
    '''
    this function will repeat the repeated word in a specific sentence
    '''
    arr = sentence.split()
    dic = set()
    # x is the word will be repeated
    for x in arr:
        if x in dic:
            return x
        else:
            dic.add(x)
    return 'No Repetition'