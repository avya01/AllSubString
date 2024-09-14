word = input("Enter a word:")
size = len(word)
PowerSetSize = 2**size

def SubStrings(size, PowerSetSize, word):
    for a in range(0, PowerSetSize):
        for b in range(0, size):
            if((a & (1<<b))>0):
                print(word[b],end="")
        print("")

print(SubStrings(size, PowerSetSize, word))