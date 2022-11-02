# creating my code 
def new (func):
    print("hello i am there")
    def hello():
        print ("write code here")
        print ("function has been called")
        func()
    return hello
@new    
def function_need_decorator():
    print("function need decorator")    
function_need_decorator()
