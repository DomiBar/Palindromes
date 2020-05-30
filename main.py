def palindrom(word):
    for i in range(len(word)):
        if word[i]==word[-1-i]:
            pass
        elif word[i]!=word[-i]:
            print (f"{word} nie jest palindromem")
            break
    else:
        print (f"{word} jest palindromem")
