try:
    f = open('ashish.txt','r')
    f.write("hello i am there whi i am")
except IOError:
    print("input output error")
else:
    print("suucesfully created file")
    f.close()       
finally:
    print (" i will execute every time no matter whats")    