import string

def palindrome(word):
    """
    Prints whether word given as argumet is palidrome or not
    Argument:
    word
    """
    translation=word.maketrans("","",string.punctuation)
    text=word.translate(translation)
    text=text.lower()
    text=text.replace(" ","")
    text=text.replace("’","")
    for i in range(len(text)):
        if text[i]==text[-1-i]:
            pass
        elif text[i]!=text[-i]:
            return False
    else:
        return True