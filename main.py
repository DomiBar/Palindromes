def palindrome(word):
    """
    Prints whether word given as argumet is palidrome or not
    Argument:
    word
    """
    for i in range(len(word)):
        if word[i]==word[-1-i]:
            pass
        elif word[i]!=word[-i]:
            return False
    else:
        return True