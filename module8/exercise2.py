# word counter dictionary

def word_count(n):
    countt={}
    for i in n:
       countt[i.lower()]= n.lower().count(i.lower())
    return countt
print(word_count("Anjali"))  