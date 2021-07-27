i=0
def x():
    while True:
        global i
        if i%2 == 1:
            print(i)
        i+=1
y=x()
print(list(y))


   
