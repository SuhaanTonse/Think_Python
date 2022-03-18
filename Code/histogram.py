#Program histogram 

def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

print(histogram('hello'))
t=['spam','spam','bat','cat','cat']
print(histogram(t))