def f(): 
    s = "I love London!"
    print(s)
    t=locals()
    print(t)
    
s = "I love Paris!"
f()
print(s)
