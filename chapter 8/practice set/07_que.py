def remove(l, word):
    n = []
    for i in l:
        if not(i == word):
            n.append(i.strip(word))
        return n
    
l = ["Rohan", "Animesh", "Abhi", "Akansha", "Khushbu"]

print(remove(l, "An"))