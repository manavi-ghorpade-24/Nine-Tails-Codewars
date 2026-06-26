def spin_words(sentence):
    # Your code goes here
    lst = sentence.split()
    ans = []
    for w in lst:
        if len(w)>=5:
            ans.append(w[::-1])
        else:
            ans.append(w)
            
    return " ".join(ans)